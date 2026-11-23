#!/usr/bin/env python3
"""Per-function forward constant propagation (basic-block-local; state is dropped at branch targets).

For every function it records
  * memory accesses whose effective address could be resolved (peripheral registers, RAM globals, flash tables)
  * call-sites with the known values of r0-r3 and a snapshot of the stack (for SPL-style init structs)
Registers hold ('c', value) or ('sp', offset). Everything unknown is simply absent (=> no false constants).
"""
import re
from thumb2 import RN

REG = {n: i for i, n in enumerate(RN)}

NOWRITE = {'cmp', 'cmn', 'tst', 'teq', 'str', 'strb', 'strh', 'strd', 'strex', 'strexb', 'strexh', 'push', 'b', 'bx',
           'cbz', 'cbnz', 'it', 'nop', 'msr', 'svc', 'bkpt', 'dsb', 'dmb', 'isb', 'cpsid', 'cpsie', 'wfi', 'wfe', 'sev',
           'stm', 'stmdb', 'pld', 'yield', 'hint', 'tbb', 'tbh'}


def split_ops(ops):
    out = []; depth = 0; cur = ''
    for ch in ops:
        if ch in '[{': depth += 1
        if ch in ']}': depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur.strip()); cur = ''
        else:
            cur += ch
    if cur.strip(): out.append(cur.strip())
    return out


def pimm(s):
    s = s.strip()
    if not s.startswith('#'): return None
    s = s[1:]
    try:
        return int(s, 0)
    except ValueError:
        return None


def base_mnem(m):
    """strip '.w', condition and 's' suffixes -> canonical operation name, plus flag-setting info is dropped."""
    m = m.replace('.w', '')
    for cand in ('movw', 'movt', 'mov', 'mvn', 'addw', 'subw', 'adds', 'subs', 'add', 'sub', 'adcs', 'adc', 'rsbs', 'rsb',
                 'ands', 'and', 'orrs', 'orr', 'eors', 'eor', 'bics', 'bic', 'lsls', 'lsl', 'lsrs', 'lsr', 'asrs', 'asr',
                 'rors', 'ror', 'muls', 'mul', 'mla', 'mls', 'sdiv', 'udiv', 'ubfx', 'sbfx', 'bfi', 'bfc', 'sxth', 'sxtb',
                 'uxth', 'uxtb', 'rev16', 'revsh', 'rev', 'rbit', 'clz', 'adr', 'ldrsb', 'ldrsh', 'ldrb', 'ldrh', 'ldrd',
                 'ldr', 'strb', 'strh', 'strd', 'str', 'pop', 'ldmdb', 'ldm', 'stmdb', 'stm', 'push', 'cmp', 'cmn', 'tst', 'teq'):
        if m.startswith(cand):
            return cand
    return m


def mask32(v):
    return v & 0xFFFFFFFF


class FuncFlow:
    def __init__(self, fw, entry):
        self.fw = fw; self.entry = entry
        self.mem = []      # dict(addr=, ea=, rw=, size=, val=, reg=)
        self.calls = []    # dict(addr=, target=, args=, stack=)
        self.icalls = []   # dict(addr=, reg=, target=)


def mem_operand(opstr):
    """returns (base_reg, off_imm_or_None, off_reg_or_None, shift) or None"""
    m = re.match(r'\[(\w+)(?:, (.+?))?\]!?$', opstr)
    if not m: return None
    base = REG.get(m.group(1)); rest = m.group(2)
    if base is None: return None
    if rest is None: return (base, 0, None, 0)
    parts = [x.strip() for x in rest.split(',')]
    if parts[0].startswith('#'):
        return (base, pimm(parts[0]), None, 0)
    rm = REG.get(parts[0])
    sh = 0
    if len(parts) > 1 and parts[1].startswith('lsl'):
        sh = int(parts[1].split('#')[1])
    return (base, None, rm, sh)


def stack_read(stack, off, size):
    v = 0
    for i in range(size):
        if off + i not in stack: return None
        v |= stack[off + i] << (8 * i)
    return v


def analyze_function(fw, entry):
    r = fw.funcs[entry]
    ff = FuncFlow(fw, entry)
    ins = sorted(r['insns'].items())
    leaders = set()
    for a, I in ins:
        if I.target is not None and I.kind in ('jump', 'cjump'):
            leaders.add(I.target)
    for t in r['tables'].values():
        leaders.update(t['targets'])
    regs = {}; stack = {}; sptr = {}
    prev_end = None; prev_kind = 'seq'
    for a, I in ins:
        if a in leaders or prev_kind in ('jump', 'ret', 'ijump', 'tbb', 'tbh') or (prev_end is not None and a != prev_end):
            regs = {}; stack = {}; sptr = {}
        prev_end = a + I.size; prev_kind = I.kind
        k = I.kind
        m = I.mnem
        bm = base_mnem(m)
        ops = split_ops(I.ops) if I.ops else []
        conditional = I.cond is not None
        # ---- calls
        if k in ('call', 'ccall'):
            args = {i: regs.get(i) for i in range(4)}
            snap = dict(stack)
            ff.calls.append(dict(addr=a, target=I.target, args=args, stack=snap, ptrs=dict(sptr), cond=conditional))
            for i in (0, 1, 2, 3, 12, 14): regs.pop(i, None)
            continue
        if k in ('icall', 'cicall'):
            reg = REG[I.ops]
            ff.icalls.append(dict(addr=a, reg=I.ops, target=regs.get(reg)))
            for i in (0, 1, 2, 3, 12, 14): regs.pop(i, None)
            continue
        if k in ('jump', 'cjump', 'ret', 'cret', 'ijump', 'tbb', 'tbh', 'it'):
            continue
        # ---- literal loads
        if I.lit is not None and bm in ('ldr', 'ldrb', 'ldrh', 'ldrsb', 'ldrsh') and ops and ops[0] in REG:
            rd = REG[ops[0]]
            v = None
            if I.litsize == 4: v = fw.u32(I.lit)
            elif I.litsize == 2: v = fw.u16(I.lit)
            elif I.litsize == 1: v = fw.d[I.lit - fw.base]
            if conditional or v is None: regs.pop(rd, None)
            else: regs[rd] = ('c', v)
            continue
        if bm == 'adr' and I.lit is not None:
            regs[REG[ops[0]]] = ('c', I.lit) if not conditional else None
            if conditional: regs.pop(REG[ops[0]], None)
            continue
        # ---- loads/stores
        if bm in ('ldr', 'ldrb', 'ldrh', 'ldrsb', 'ldrsh', 'str', 'strb', 'strh', 'ldrd', 'strd') and len(ops) >= 2:
            is_load = bm.startswith('ldr')
            size = 4 if bm in ('ldr', 'ldrd', 'str', 'strd') else (2 if bm.endswith('h') else 1)
            opstr = ops[-1] if bm in ('ldr', 'ldrb', 'ldrh', 'ldrsb', 'ldrsh', 'str', 'strb', 'strh') else ops[2] if len(ops) > 2 else ops[-1]
            if bm in ('ldrd', 'strd'):
                opstr = [o for o in ops if o.startswith('[')][0] if any(o.startswith('[') for o in ops) else ops[-1]
            mo = mem_operand(opstr)
            if bm in ('ldrd', 'strd') and not mo:
                # post-index form '[rn], #imm'
                mm = re.match(r'\[(\w+)\]', ops[2]) if len(ops) > 2 else None
                mo = (REG[mm.group(1)], 0, None, 0) if mm else None
            rt = REG.get(ops[0])
            ea = None; sp_off = None
            if mo:
                bs, off, rmx, sh = mo
                b = regs.get(bs) if bs != 15 else None
                if bs == 13: b = ('sp', 0)
                if b is not None:
                    if off is not None:
                        if b[0] == 'c': ea = mask32(b[1] + off)
                        else: sp_off = b[1] + off
                    elif rmx is not None and regs.get(rmx) and regs[rmx][0] == 'c' and b[0] == 'c':
                        ea = mask32(b[1] + (regs[rmx][1] << sh))
            wb = opstr.endswith(']!') or (len(ops) > 2 and bm not in ('ldrd', 'strd') and not opstr.endswith(']'))
            if ea is not None:
                val = None
                if not is_load and rt is not None and regs.get(rt) and regs[rt][0] == 'c' and not conditional:
                    val = regs[rt][1]
                ff.mem.append(dict(addr=a, ea=ea, rw='R' if is_load else 'W', size=size, val=val,
                                   reg=I.ops.split('[')[1].split(',')[0].strip(']!') if '[' in I.ops else ''))
            if is_load:
                dests = [rt] + ([REG[ops[1]]] if bm == 'ldrd' else [])
                for d in dests: regs.pop(d, None)
                if not conditional and ea is not None and fw.in_flash(ea) and bm == 'ldr' and ea % 4 == 0:
                    v = fw.u32(ea)
                    if v is not None: regs[rt] = ('c', v)
                if not conditional and sp_off is not None and bm in ('ldr', 'ldrh', 'ldrb') and rt is not None:
                    v = stack_read(stack, sp_off, size)
                    if v is not None: regs[rt] = ('c', v)
                    elif size == 4 and sp_off in sptr: regs[rt] = ('sp', sptr[sp_off])
            else:
                if sp_off is not None:
                    v = None
                    if rt is not None and regs.get(rt) and regs[rt][0] == 'c' and not conditional:
                        v = regs[rt][1]
                    for i in range(size):
                        if v is None: stack.pop(sp_off + i, None)
                        else: stack[sp_off + i] = (v >> (8 * i)) & 0xFF
                    for o in list(sptr):
                        if sp_off - 3 <= o < sp_off + size: sptr.pop(o, None)
                    if size == 4 and rt is not None and regs.get(rt) and regs[rt][0] == 'sp' and not conditional:
                        sptr[sp_off] = regs[rt][1]
            if bs_wb := (mo and wb and mo[0] != 13):
                regs.pop(mo[0], None)
            continue
        # ---- stack / multi
        if bm in ('push', 'stm', 'stmdb', 'stm.w'):
            continue
        if bm in ('pop', 'ldm', 'ldmdb'):
            lst = re.search(r'\{(.*)\}', I.ops)
            if lst:
                for rname in lst.group(1).split(','):
                    rname = rname.strip()
                    if rname in REG: regs.pop(REG[rname], None)
            if bm != 'pop' and ops and ops[0].endswith('!'): regs.pop(REG.get(ops[0][:-1]), None)
            continue
        if bm in NOWRITE or m in NOWRITE:
            continue
        # ---- data processing
        if not ops or ops[0] not in REG:
            continue
        rd = REG[ops[0]]

        def val(o):
            if o in REG:
                return regs.get(REG[o]) if REG[o] != 13 else ('sp', 0)
            i = pimm(o)
            return ('c', i) if i is not None else None
        res = None
        if not conditional:
            try:
                if bm in ('mov', 'movw') and len(ops) == 2:
                    res = val(ops[1])
                elif bm == 'mvn' and len(ops) == 2:
                    v = val(ops[1]); res = ('c', mask32(~v[1])) if v and v[0] == 'c' else None
                elif bm == 'movt':
                    c = regs.get(rd); i = pimm(ops[1])
                    if c and c[0] == 'c' and i is not None: res = ('c', (c[1] & 0xFFFF) | (i << 16))
                elif bm in ('add', 'adds', 'addw', 'sub', 'subs', 'subw'):
                    sgn = 1 if bm.startswith('add') else -1
                    if len(ops) == 2: a1, a2 = val(ops[0]), val(ops[1])
                    else: a1, a2 = val(ops[1]), val(ops[2])
                    if a1 and a2:
                        if a1[0] == 'c' and a2[0] == 'c': res = ('c', mask32(a1[1] + sgn * a2[1]))
                        elif a1[0] == 'sp' and a2[0] == 'c': res = ('sp', a1[1] + sgn * a2[1])
                elif bm in ('orr', 'orrs', 'and', 'ands', 'eor', 'eors', 'bic', 'bics'):
                    if len(ops) == 2: a1, a2 = val(ops[0]), val(ops[1])
                    else: a1, a2 = val(ops[1]), val(ops[2])
                    if a1 and a2 and a1[0] == 'c' and a2[0] == 'c':
                        x, y = a1[1], a2[1]
                        res = ('c', mask32({'orr': x | y, 'and': x & y, 'eor': x ^ y, 'bic': x & ~y}[bm.rstrip('s') if bm not in ('bics',) else 'bic']))
                elif bm in ('lsl', 'lsls', 'lsr', 'lsrs', 'asr', 'asrs'):
                    if len(ops) == 2: a1, a2 = val(ops[0]), val(ops[1])
                    else: a1, a2 = val(ops[1]), val(ops[2])
                    if a1 and a2 and a1[0] == 'c' and a2[0] == 'c':
                        s = a2[1]
                        if bm.startswith('lsl'): res = ('c', mask32(a1[1] << s) if s < 32 else 0)
                        elif bm.startswith('lsr'): res = ('c', a1[1] >> s if s < 32 else 0)
                elif bm in ('mul', 'muls', 'rsb', 'rsbs') and False:
                    pass
                elif bm in ('uxtb', 'uxth', 'sxtb', 'sxth'):
                    a1 = val(ops[1])
                    if a1 and a1[0] == 'c':
                        x = a1[1]
                        res = ('c', {'uxtb': x & 0xFF, 'uxth': x & 0xFFFF, 'sxtb': mask32((x & 0xFF) - 256 if x & 0x80 else x & 0xFF),
                                     'sxth': mask32((x & 0xFFFF) - 65536 if x & 0x8000 else x & 0xFFFF)}[bm])
                elif bm == 'ubfx':
                    a1 = val(ops[1])
                    if a1 and a1[0] == 'c':
                        lsb = pimm(ops[2]); w = pimm(ops[3]); res = ('c', (a1[1] >> lsb) & ((1 << w) - 1))
            except (KeyError, ValueError, TypeError):
                res = None
        if res is None: regs.pop(rd, None)
        else: regs[rd] = res
        if bm in ('umull', 'smull', 'umlal', 'smlal') and len(ops) >= 2 and ops[1] in REG:
            regs.pop(REG[ops[1]], None)
    return ff


def analyze_all(fw):
    out = {}
    for e, r in fw.funcs.items():
        if r['ok']:
            out[e] = analyze_function(fw, e)
    return out


# ------------------------------------------------------------------ peripheral map
PERIPH = [
    (0x40000000, 0x400, 'TIM2'), (0x40000400, 0x400, 'TIM3'), (0x40000800, 0x400, 'TIM4'), (0x40000C00, 0x400, 'TIM5'),
    (0x40001000, 0x400, 'TIM6'), (0x40001400, 0x400, 'TIM7'), (0x40002800, 0x400, 'RTC'), (0x40002C00, 0x400, 'WWDG'),
    (0x40003000, 0x400, 'IWDG'), (0x40003800, 0x400, 'SPI2'), (0x40003C00, 0x400, 'SPI3'), (0x40004400, 0x400, 'USART2'),
    (0x40004800, 0x400, 'USART3'), (0x40004C00, 0x400, 'UART4'), (0x40005000, 0x400, 'UART5'), (0x40005400, 0x400, 'I2C1'),
    (0x40005800, 0x400, 'I2C2'), (0x40005C00, 0x400, 'USB'), (0x40006400, 0x400, 'CAN1'), (0x40006C00, 0x400, 'BKP'),
    (0x40007000, 0x400, 'PWR'), (0x40007400, 0x400, 'DAC'),
    (0x40010000, 0x400, 'AFIO'), (0x40010400, 0x400, 'EXTI'), (0x40010800, 0x400, 'GPIOA'), (0x40010C00, 0x400, 'GPIOB'),
    (0x40011000, 0x400, 'GPIOC'), (0x40011400, 0x400, 'GPIOD'), (0x40011800, 0x400, 'GPIOE'), (0x40011C00, 0x400, 'GPIOF'),
    (0x40012000, 0x400, 'GPIOG'), (0x40012400, 0x400, 'ADC1'), (0x40012800, 0x400, 'ADC2'), (0x40012C00, 0x400, 'TIM1'),
    (0x40013000, 0x400, 'SPI1'), (0x40013400, 0x400, 'TIM8'), (0x40013800, 0x400, 'USART1'), (0x40013C00, 0x400, 'ADC3'),
    (0x40018000, 0x400, 'SDIO'), (0x40020000, 0x400, 'DMA1'), (0x40020400, 0x400, 'DMA2'), (0x40021000, 0x400, 'RCC'),
    (0x40022000, 0x400, 'FLASH_IF'), (0x40023000, 0x400, 'CRC'),
    (0xA0000000, 0x1000, 'FSMC_REGS'), (0xE000E010, 0x10, 'SysTick'), (0xE000E100, 0x400, 'NVIC'),
    (0xE000ED00, 0x100, 'SCB'), (0xE0042000, 0x10, 'DBGMCU'), (0x1FFFF800, 0x10, 'OptionBytes'),
]
FSMC_BANKS = [(0x60000000, 0x10000000, 'FSMC_BANK1(NOR/SRAM/LCD)'), (0x70000000, 0x10000000, 'FSMC_BANK2(NAND)'),
              (0x80000000, 0x10000000, 'FSMC_BANK3(NAND)'), (0x90000000, 0x10000000, 'FSMC_BANK4(PCCARD)')]

REGNAMES = {
    'RCC': {0x00: 'CR', 0x04: 'CFGR', 0x08: 'CIR', 0x0C: 'APB2RSTR', 0x10: 'APB1RSTR', 0x14: 'AHBENR', 0x18: 'APB2ENR',
            0x1C: 'APB1ENR', 0x20: 'BDCR', 0x24: 'CSR'},
    'GPIO': {0x00: 'CRL', 0x04: 'CRH', 0x08: 'IDR', 0x0C: 'ODR', 0x10: 'BSRR', 0x14: 'BRR', 0x18: 'LCKR'},
    'AFIO': {0x00: 'EVCR', 0x04: 'MAPR', 0x08: 'EXTICR1', 0x0C: 'EXTICR2', 0x10: 'EXTICR3', 0x14: 'EXTICR4', 0x1C: 'MAPR2'},
    'EXTI': {0x00: 'IMR', 0x04: 'EMR', 0x08: 'RTSR', 0x0C: 'FTSR', 0x10: 'SWIER', 0x14: 'PR'},
    'SPI': {0x00: 'CR1', 0x04: 'CR2', 0x08: 'SR', 0x0C: 'DR', 0x10: 'CRCPR', 0x14: 'RXCRCR', 0x18: 'TXCRCR', 0x1C: 'I2SCFGR', 0x20: 'I2SPR'},
    'USART': {0x00: 'SR', 0x04: 'DR', 0x08: 'BRR', 0x0C: 'CR1', 0x10: 'CR2', 0x14: 'CR3', 0x18: 'GTPR'},
    'TIM': {0x00: 'CR1', 0x04: 'CR2', 0x08: 'SMCR', 0x0C: 'DIER', 0x10: 'SR', 0x14: 'EGR', 0x18: 'CCMR1', 0x1C: 'CCMR2',
            0x20: 'CCER', 0x24: 'CNT', 0x28: 'PSC', 0x2C: 'ARR', 0x30: 'RCR', 0x34: 'CCR1', 0x38: 'CCR2', 0x3C: 'CCR3',
            0x40: 'CCR4', 0x44: 'BDTR', 0x48: 'DCR', 0x4C: 'DMAR'},
    'ADC': {0x00: 'SR', 0x04: 'CR1', 0x08: 'CR2', 0x0C: 'SMPR1', 0x10: 'SMPR2', 0x14: 'JOFR1', 0x18: 'JOFR2', 0x1C: 'JOFR3',
            0x20: 'JOFR4', 0x24: 'HTR', 0x28: 'LTR', 0x2C: 'SQR1', 0x30: 'SQR2', 0x34: 'SQR3', 0x38: 'JSQR', 0x3C: 'JDR1',
            0x40: 'JDR2', 0x44: 'JDR3', 0x48: 'JDR4', 0x4C: 'DR'},
    'FLASH_IF': {0x00: 'ACR', 0x04: 'KEYR', 0x08: 'OPTKEYR', 0x0C: 'SR', 0x10: 'CR', 0x14: 'AR', 0x1C: 'OBR', 0x20: 'WRPR'},
    'PWR': {0x00: 'CR', 0x04: 'CSR'},
    'IWDG': {0x00: 'KR', 0x04: 'PR', 0x08: 'RLR', 0x0C: 'SR'},
    'WWDG': {0x00: 'CR', 0x04: 'CFR', 0x08: 'SR'},
    'SysTick': {0x00: 'CTRL', 0x04: 'LOAD', 0x08: 'VAL', 0x0C: 'CALIB'},
    'SCB': {0x00: 'CPUID', 0x04: 'ICSR', 0x08: 'VTOR', 0x0C: 'AIRCR', 0x10: 'SCR', 0x14: 'CCR', 0x18: 'SHPR1', 0x1C: 'SHPR2',
            0x20: 'SHPR3', 0x24: 'SHCSR', 0x28: 'CFSR', 0x2C: 'HFSR'},
    'FSMC_REGS': {0x00: 'BCR1', 0x04: 'BTR1', 0x08: 'BCR2', 0x0C: 'BTR2', 0x10: 'BCR3', 0x14: 'BTR3', 0x18: 'BCR4', 0x1C: 'BTR4',
                  0x60: 'PCR2', 0x64: 'SR2', 0x68: 'PMEM2', 0x6C: 'PATT2', 0x74: 'ECCR2', 0x80: 'PCR3', 0x84: 'SR3',
                  0x88: 'PMEM3', 0x8C: 'PATT3', 0x94: 'ECCR3', 0xA0: 'PCR4', 0xA4: 'SR4', 0xA8: 'PMEM4', 0xAC: 'PATT4', 0xB0: 'PIO4',
                  0x104: 'BWTR1', 0x10C: 'BWTR2', 0x114: 'BWTR3', 0x11C: 'BWTR4'},
    'RTC': {0x00: 'CRH', 0x04: 'CRL', 0x08: 'PRLH', 0x0C: 'PRLL', 0x10: 'DIVH', 0x14: 'DIVL', 0x18: 'CNTH', 0x1C: 'CNTL', 0x20: 'ALRH', 0x24: 'ALRL'},
    'DMA': {0x00: 'ISR', 0x04: 'IFCR'},
}


def classify(ea):
    """ea -> (periph, regname, detail) or None. Handles bit-band alias."""
    note = ''
    if 0x42000000 <= ea < 0x44000000:
        off = ea - 0x42000000
        byte = off >> 5; bit = (off >> 2) & 31
        ea = 0x40000000 + byte; note = ' bit%d(bitband)' % bit
        ea &= ~3 if False else 0xFFFFFFFF
    for lo, size, name in PERIPH:
        if lo <= ea < lo + size:
            off = ea - lo
            fam = name
            if name.startswith('GPIO'): fam = 'GPIO'
            elif name.startswith('SPI'): fam = 'SPI'
            elif name.startswith(('USART', 'UART')): fam = 'USART'
            elif name.startswith('TIM'): fam = 'TIM'
            elif name.startswith('ADC'): fam = 'ADC'
            elif name.startswith('DMA'): fam = 'DMA'
            if fam == 'DMA' and off >= 8:
                ch = (off - 8) // 20 + 1; r = (off - 8) % 20
                rn = 'CH%d_%s' % (ch, {0: 'CCR', 4: 'CNDTR', 8: 'CPAR', 12: 'CMAR'}.get(r, '+%d' % r))
                return (name, rn + note, off)
            rn = REGNAMES.get(fam, {}).get(off & ~3 if fam not in ('USART',) else off - (off % 4), '+0x%X' % off)
            if off % 4 and fam != 'x': rn = '%s+%d' % (rn, off % 4)
            return (name, rn + note, off)
    for lo, size, name in FSMC_BANKS:
        if lo <= ea < lo + size:
            return (name, '+0x%X' % (ea - lo), ea - lo)
    return None
