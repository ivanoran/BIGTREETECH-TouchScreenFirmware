#!/usr/bin/env python3
"""Static analysis engine for Cortex-M3 flash dumps (Thumb-2).

Usage:  python3 analyze.py <dump.bin> [--base 0x08000000] [--out <dir>]

Pipeline
  1. parse the vector table(s) found at 0x0 and at any 4 KiB-aligned offset that looks like one;
  2. recursive-descent disassembly from vectors; BL targets; function pointers found in literal
     pools / data tables; PUSH{..,LR} prologue scan in remaining gaps;
  3. fixed-point iteration (tail-call detection and no-return detection);
  4. constant propagation inside functions -> peripheral register accesses and call-site arguments;
  5. region classification and JSON/CSV/ASM output.
Everything is evidence based: every record keeps the instruction addresses that justify it.
"""
import sys, os, json, struct, argparse, hashlib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thumb2 import decode_at, Insn, RN, COND

BASE = 0x08000000


class Firmware:
    def __init__(self, data, base=BASE):
        self.d = data; self.base = base; self.end = base + len(data)
        self.insns = {}                 # addr -> Insn
        self.lits = {}                  # literal addr -> {'size','value','refs':[insn addrs]}
        self.funcs = {}                 # entry -> dict
        self.entries = {}               # entry -> source
        self.noreturn = set()
        self.jtables = {}               # tbb/tbh insn addr -> dict(table, targets, size)
        self.bad_entries = {}
        self.vectors = {}

    # --- raw access
    def u32(self, a):
        o = a - self.base
        return struct.unpack_from('<I', self.d, o)[0] if 0 <= o <= len(self.d) - 4 else None

    def u16(self, a):
        o = a - self.base
        return struct.unpack_from('<H', self.d, o)[0] if 0 <= o <= len(self.d) - 2 else None

    def in_flash(self, a):
        return self.base <= a < self.end

    def erased(self, a, n=4):
        o = a - self.base
        return all(b == 0xFF for b in self.d[o:o + n])

    def ascii_len(self, a, minlen=3):
        o = a - self.base; n = 0
        while o + n < len(self.d) and (0x20 <= self.d[o + n] < 0x7F or self.d[o + n] in (9, 10, 13)): n += 1
        if n >= minlen and o + n < len(self.d) and self.d[o + n] == 0: return n
        return 0

    def refresh_data_ranges(self, trusted=('bl', 'vector', 'tail', 'prologue', 'gapscan', 'data_ptr', 'lit_ptr')):
        """Strings referenced by ADR / literal pointers from trusted functions are data, never code."""
        rng = []
        for e, r in self.funcs.items():
            if not r['ok'] or self.entries.get(e, '').split(':')[0].split('@')[0] not in trusted: continue
            for a, I in r['insns'].items():
                t = None
                if I.mnem.startswith('adr') and I.lit: t = I.lit
                elif I.lit is not None and I.litsize == 4:
                    v = self.u32(I.lit)
                    if v is not None and self.in_flash(v): t = v
                if t is not None:
                    n = self.ascii_len(t)
                    seg = self.d[t - self.base:t - self.base + n]
                    if n >= 4 and sum(1 for c in seg if chr(c).isalnum()) >= 3 and not (t in self.funcs):
                        rng.append((t, t + n + 1))
        self.data_ranges = sorted(set(rng))
        return len(self.data_ranges)

    def hits_data(self, r):
        dr = getattr(self, 'data_ranges', [])
        if not dr: return False
        for a, I in r['insns'].items():
            for (x, y) in dr:
                if a < y and a + I.size > x: return True
        return False

    def purge_untrusted(self):
        n = 0
        for e in list(self.funcs):
            src = self.entries.get(e, '').split(':')[0].split('@')[0]
            if src in ('gapscan', 'prologue', 'data_ptr', 'lit_ptr') and self.funcs[e]['ok'] and self.hits_data(self.funcs[e]):
                del self.funcs[e]; del self.entries[e]; n += 1
        return n

    # --- tracing one function
    def trace(self, entry):
        """Returns dict(insns=set, calls=dict addr->target, ok=bool, reasons=[...], ...)"""
        seen = {}                       # addr -> Insn
        calls = {}                      # insn addr -> target
        icalls = []; ijumps = []; tails = {}; tbl = {}
        lits = {}
        has_ret = False; self_loop = False
        ok = True; reason = []
        work = [entry]
        queued = {entry}
        while work:
            a = work.pop()
            it = None
            while True:
                if a in seen:
                    break
                if not (self.base <= a < self.end) or a & 1:
                    ok = False; reason.append('branch outside flash/odd 0x%X' % a); break
                I, it2 = decode_at(self.d, a - self.base, self.base, it)
                if I is None or I.kind == 'undef':
                    ok = False; reason.append('undefined opcode at 0x%X' % a); break
                if self.erased(a, 2) and I.raw == 0xFFFF:
                    ok = False; reason.append('erased flash at 0x%X' % a); break
                seen[a] = I
                if I.lit is not None and I.litsize:
                    lits[a] = I
                k = I.kind
                nxt = a + I.size
                if k in ('seq', 'it'):
                    a = nxt; it = it2; continue
                if k in ('call', 'ccall'):
                    calls[a] = I.target
                    if I.target in self.noreturn and k == 'call':
                        break
                    a = nxt; it = it2; continue
                if k in ('icall', 'cicall'):
                    icalls.append(a); a = nxt; it = it2; continue
                if k == 'jump':
                    t = I.target
                    if t == a:
                        self_loop = True
                    elif t in self.entries and t != entry:
                        tails[a] = t
                    elif t not in queued:
                        queued.add(t); work.append(t)
                    break
                if k == 'cjump':
                    t = I.target
                    if t in self.entries and t != entry and I.mnem.startswith('b') and False:
                        pass
                    if t not in queued and t not in seen:
                        queued.add(t); work.append(t)
                    a = nxt; it = it2; continue
                if k == 'ret':
                    has_ret = True; break
                if k == 'cret':
                    has_ret = True; a = nxt; it = it2; continue
                if k in ('tbb', 'tbh'):
                    targets, info = self.parse_jumptable(seen, a, I)
                    tbl[a] = info
                    for t in targets:
                        if t not in queued:
                            queued.add(t); work.append(t)
                    break
                if k == 'ijump':
                    # thunk:  ldr rN,[pc,#x] ; bx rN   -> resolved tail call
                    pa = a - 2
                    P = seen.get(pa)
                    if (I.mnem == 'bx' and P is not None and P.mnem == 'ldr' and P.lit is not None
                            and RN[P.rt] == I.ops):
                        v = self.u32(P.lit)
                        if v is not None and (v & 1) and self.in_flash(v & ~1):
                            tails[a] = v & ~1
                            break
                    ijumps.append(a); break
                a = nxt; it = it2
        return dict(insns=seen, calls=calls, icalls=icalls, ijumps=ijumps, tails=tails, tables=tbl,
                    lits=lits, ok=ok, reason=reason, has_ret=has_ret, self_loop=self_loop)

    def parse_jumptable(self, seen, a, I):
        """tbb/tbh at a: table starts at a+4. Count from preceding `cmp rX,#N` if possible."""
        size = 1 if I.kind == 'tbb' else 2
        tstart = a + 4
        n = None
        prev = sorted(k for k in seen if a - 40 <= k < a)[-8:]
        for k in reversed(prev):
            p = seen[k]
            if p.mnem.startswith('cmp') and '#' in p.ops:
                try:
                    n = int(p.ops.split('#')[1], 0) + 1
                except ValueError:
                    pass
                break
        targets = []
        if n is None:
            n = 0; lim = 256; mn = 1 << 40
            while n < lim and tstart + n * size < mn:
                v = self.d[tstart + n * size - self.base] if size == 1 else self.u16(tstart + n * size)
                t = tstart + v * 2
                mn = min(mn, t); n += 1
        for i in range(n):
            v = self.d[tstart + i * size - self.base] if size == 1 else self.u16(tstart + i * size)
            targets.append(a + 4 + v * 2)
        return targets, dict(table=tstart, entries=n, entry_size=size, targets=targets)

    # --- whole-image discovery
    def discover(self, seeds):
        for a, src in seeds:
            self.entries.setdefault(a, src)
        for rnd in range(6):
            changed = True; passes = 0
            while changed and passes < 30:
                changed = False; passes += 1
                for e in sorted(list(self.entries)):
                    if e in self.funcs and self.funcs[e].get('_round') == (rnd, passes - 1) and False:
                        continue
                    r = self.trace(e)
                    prev = self.funcs.get(e)
                    self.funcs[e] = r
                    if not r['ok']:
                        self.bad_entries[e] = r['reason'][:3]
                    else:
                        self.bad_entries.pop(e, None)
                    for c in r['calls'].values():
                        if c not in self.entries and self.in_flash(c):
                            self.entries[c] = 'bl'; changed = True
                    for t in r['tails'].values():
                        if t not in self.entries and self.in_flash(t):
                            self.entries[t] = 'tail'; changed = True
                # no-return detection
                nr = set()
                for e, r in self.funcs.items():
                    if not r['ok'] or r['has_ret'] or r['ijumps'] or r['tables']:
                        continue
                    if r['self_loop'] and not r['tails']:
                        nr.add(e)
                for _ in range(4):          # propagate through thunks
                    for e, r in self.funcs.items():
                        if (r['ok'] and not r['has_ret'] and not r['ijumps'] and not r['tables'] and r['tails']
                                and all(t in nr for t in r['tails'].values())):
                            nr.add(e)
                if nr != self.noreturn:
                    self.noreturn = nr; changed = True
                # unconditional jumps that went into the middle of another function's entry -> tails
                # (handled by entries lookup in trace)
            # collect literal function pointers + data pointers
            newp = self.find_pointer_entries()
            if not newp:
                break
        # final
        for e in list(self.funcs):
            if not self.funcs[e]['ok']:
                pass

    def covered(self):
        cov = set()
        for e, r in self.funcs.items():
            if not r['ok']:
                continue
            for a, I in r['insns'].items():
                for i in range(I.size):
                    cov.add(a + i)
        return cov

    def find_pointer_entries(self):
        """Odd aligned words that point at flash -> candidate callbacks (from literal pools and data)."""
        found = {}
        # literal values
        for e, r in self.funcs.items():
            if not r['ok']:
                continue
            for a, I in r['lits'].items():
                if I.litsize != 4:
                    continue
                v = self.u32(I.lit)
                if v is not None and self.in_flash(v & ~1) and (v & 1) and (v & ~1) not in self.entries:
                    found[v & ~1] = 'lit_ptr@0x%X' % a
        cov = self.covered()
        litbytes = set()
        for r in self.funcs.values():
            for a, I in r['lits'].items():
                for i in range(I.litsize or 0):
                    litbytes.add(I.lit + i)
        # data tables: aligned words outside code
        for a in range(self.base, self.end - 3, 4):
            if a in cov or (a + 2) in cov or a in litbytes:
                continue
            v = self.u32(a)
            if v and (v & 1) and self.in_flash(v & ~1):
                t = v & ~1
                if t not in self.entries and t not in found:
                    # require sibling pointer (vector/callback table) or plain pointer into already-known code region start
                    found[t] = 'data_ptr@0x%X' % a
        newc = 0
        for t, src in found.items():
            r = self.trace(t)
            if r['ok'] and len(r['insns']) >= 2 and self.plausible(r) and not self.hits_data(r):
                self.entries[t] = src; newc += 1
        return newc

    def plausible(self, r):
        """Reject traces that look like data decoded as code."""
        ins = list(r['insns'].values())
        if len(ins) < 2:
            return False
        bad = sum(1 for I in ins if I.mnem in ('hint', 'cps?', 'barrier?', 'srs/rfe', 'undef'))
        if bad:
            return False
        if not (r['has_ret'] or r['tails'] or r['self_loop'] or r['ijumps'] or r['tables']):
            return False
        return True

    def prologue_scan(self):
        cov = self.covered()
        n = 0
        a = self.base
        while a < self.end - 2:
            if a in cov or (a + 1) in cov:
                a += 2; continue
            h = self.u16(a)
            is_push = (h & 0xFF00) == 0xB500 or (h == 0xE92D and False)
            if is_push and a not in self.entries and not self.erased(a, 2):
                r = self.trace(a)
                if r['ok'] and self.plausible(r) and len(r['insns']) >= 4 and not self.hits_data(r):
                    ov = sum(1 for k in r['insns'] if k in cov)
                    if ov == 0:
                        self.entries[a] = 'prologue'; n += 1
                        for k, I in r['insns'].items():
                            for i in range(I.size):
                                cov.add(k + i)
            a += 2
        return n


def _gap_scan(self, zones):
    """Scan uncovered bytes inside code zones for functions never reached by recursion
    (unreferenced library functions, leaf functions). Accept only strict-plausibility traces."""
    added = 0
    for (lo, hi) in zones:
        p = lo
        cov = self.covered()
        litb = set(); jt = set()
        for r in self.funcs.values():
            for a, I in r['lits'].items():
                for i in range(I.litsize or 0): litb.add(I.lit + i)
            for a, t in r['tables'].items():
                for i in range(t['entries'] * t['entry_size']): jt.add(t['table'] + i)
        used = cov | litb | jt
        while p < hi:
            if p in used or (p + 1) in used or self.erased(p, 4):
                p += 2; continue
            h = self.u16(p)
            if h == 0x0000 or h == 0xFFFF:
                p += 2; continue
            r = self.trace(p)
            ok = r['ok'] and self.plausible(r) and len(r['insns']) >= 3 and not self.hits_data(r)
            if ok:
                ov = sum(1 for k, I in r['insns'].items() if k in used or (k + 1) in used)
                ok = ov == 0
            if ok:
                self.entries[p] = 'gapscan'; added += 1
                for k, I in r['insns'].items():
                    for i in range(I.size): used.add(k + i)
                for a, I in r['lits'].items():
                    for i in range(I.litsize or 0): used.add(I.lit + i)
                p = max(k + I.size for k, I in r['insns'].items()) if False else p + 2
            else:
                p += 2
    return added


Firmware.gap_scan = _gap_scan


def parse_vectors(fw, off):
    names = ['MSP', 'Reset', 'NMI', 'HardFault', 'MemManage', 'BusFault', 'UsageFault', 'rsv7', 'rsv8', 'rsv9', 'rsv10',
             'SVCall', 'DebugMon', 'rsv13', 'PendSV', 'SysTick']
    irq = ['WWDG', 'PVD', 'TAMPER', 'RTC', 'FLASH', 'RCC', 'EXTI0', 'EXTI1', 'EXTI2', 'EXTI3', 'EXTI4', 'DMA1_Ch1', 'DMA1_Ch2',
           'DMA1_Ch3', 'DMA1_Ch4', 'DMA1_Ch5', 'DMA1_Ch6', 'DMA1_Ch7', 'ADC1_2', 'USB_HP_CAN_TX', 'USB_LP_CAN_RX0', 'CAN_RX1',
           'CAN_SCE', 'EXTI9_5', 'TIM1_BRK', 'TIM1_UP', 'TIM1_TRG_COM', 'TIM1_CC', 'TIM2', 'TIM3', 'TIM4', 'I2C1_EV', 'I2C1_ER',
           'I2C2_EV', 'I2C2_ER', 'SPI1', 'SPI2', 'USART1', 'USART2', 'USART3', 'EXTI15_10', 'RTCAlarm', 'USBWakeup', 'TIM8_BRK',
           'TIM8_UP', 'TIM8_TRG_COM', 'TIM8_CC', 'ADC3', 'FSMC', 'SDIO', 'TIM5', 'SPI3', 'UART4', 'UART5', 'TIM6', 'TIM7',
           'DMA2_Ch1', 'DMA2_Ch2', 'DMA2_Ch3', 'DMA2_Ch4_5']
    out = []
    for i in range(16 + len(irq)):
        v = fw.u32(fw.base + off + 4 * i)
        nm = names[i] if i < 16 else 'IRQ%d_%s' % (i - 16, irq[i - 16])
        out.append((i, nm, v))
    return out


def find_images(fw):
    """Locate vector tables: offset 0 and any 0x1000-aligned offset with plausible MSP+reset."""
    imgs = []
    for off in range(0, len(fw.d), 0x1000):
        msp = fw.u32(fw.base + off); rst = fw.u32(fw.base + off + 4)
        if msp is None or rst is None:
            continue
        if 0x20000000 <= msp <= 0x2000C000 and (rst & 1) and fw.in_flash(rst & ~1):
            ok = 0
            for i in range(2, 16):
                v = fw.u32(fw.base + off + 4 * i)
                if v == 0 or (v & 1 and fw.in_flash(v & ~1)):
                    ok += 1
            if ok >= 12:
                imgs.append(off)
    return imgs


def build(path, base=BASE, verbose=True):
    data = open(path, 'rb').read()
    fw = Firmware(data, base)
    imgs = find_images(fw)
    if verbose: print('vector tables at offsets:', [hex(i) for i in imgs])
    seeds = []
    for off in imgs:
        vt = parse_vectors(fw, off)
        fw.vectors[off] = vt
        for i, nm, v in vt[1:]:
            if v and v & 1 and fw.in_flash(v & ~1):
                seeds.append((v & ~1, 'vector:%s@0x%X' % (nm, fw.base + off)))
    fw.discover(seeds)
    fw.refresh_data_ranges(); fw.purge_untrusted()
    n = fw.prologue_scan()
    if verbose: print('prologue-scan new entries:', n)
    fw.discover([])
    fw.refresh_data_ranges(); fw.purge_untrusted(); fw.discover([])
    zones = code_zones(fw)
    for i in range(4):
        g = fw.gap_scan(zones)
        if verbose: print('gap-scan round', i, 'new entries:', g)
        if not g: break
        fw.discover([])
        fw.refresh_data_ranges(); fw.purge_untrusted()
    fw.discover([])
    return fw


def code_zones(fw):
    """Code zone = [image start, last recursively-covered address + 0x40) for each image."""
    cov = sorted(fw.covered())
    zones = []
    starts = sorted(o + fw.base for o in find_images(fw))
    bounds = starts[1:] + [fw.end]
    for st, nb in zip(starts, bounds):
        c = [a for a in cov if st <= a < nb]
        if c: zones.append((st, min(max(c) + 0x40, nb)))
    return zones


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dump'); ap.add_argument('--base', default='0x08000000')
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'disassembly'))
    a = ap.parse_args()
    fw = build(a.dump, int(a.base, 0))
    ok = [e for e, r in fw.funcs.items() if r['ok']]
    print('functions ok:', len(ok), 'bad:', len(fw.bad_entries), 'noreturn:', len(fw.noreturn))
    print('code bytes covered:', len(fw.covered()))


if __name__ == '__main__':
    main()
