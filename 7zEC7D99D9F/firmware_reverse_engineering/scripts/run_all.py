#!/usr/bin/env python3
"""Regenerate every machine-readable result and the auto-generated Markdown tables.

Usage:  python3 run_all.py [dump.bin] [outdir]
Defaults: ../original/dump_full.bin  and the parent directory of scripts/.
Outputs (under outdir):
  disassembly/{full_disassembly.asm,functions.json,references.json,cross_references.csv}
  resources/{strings.txt,binary_regions.csv}
  FUNCTION_INDEX.md CALL_GRAPH.md PERIPHERALS.md GPIO_MAP.md VECTOR_TABLE.md MEMORY_MAP.md (auto parts)
"""
import sys, os, json, csv, re, collections, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze, dataflow, disassemble
from annotations import FUNC_NAMES_FULL, EVIDENCE

dump = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'original', 'dump_full.bin')
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, '..')
for sub in ('disassembly', 'resources', 'generated', os.path.join('resources', 'extracted_assets')):
    os.makedirs(os.path.join(out, sub), exist_ok=True)

fw = analyze.build(dump, verbose=False)
flows = dataflow.analyze_all(fw)
BASE = fw.base
SHA = hashlib.sha256(fw.d).hexdigest()
imgs = sorted(o + BASE for o in analyze.find_images(fw))


def image_of(a):
    r = 'A'
    for i, s in enumerate(imgs):
        if a >= s: r = 'AB'[i] if i < 2 else str(i)
    return r


def hx(a): return '0x%08X' % a


ok = {e: r for e, r in fw.funcs.items() if r['ok']}
called_by = collections.defaultdict(set)
tail_by = collections.defaultdict(set)
for e, r in ok.items():
    for t in r['calls'].values(): called_by[t].add(e)
    for t in r['tails'].values(): tail_by[t].add(e)
for e, f in flows.items():
    for ic in f.icalls: pass
vec_entries = {int(v.split('@')[0].split(':')[1]) if False else e: v for e, v in fw.entries.items() if v.startswith('vector')}


def func_end(e):
    r = ok[e]; last = max(a + I.size for a, I in r['insns'].items())
    for a, I in r['lits'].items():
        if I.litsize and I.lit >= e and I.lit - last < 64: last = max(last, I.lit + I.litsize)
    return last


def string_refs(e):
    out = []
    for a, I in ok[e]['insns'].items():
        if I.lit is None: continue
        v = None
        if I.mnem.startswith('adr'): v = I.lit
        elif I.litsize == 4: v = fw.u32(I.lit)
        if v and fw.in_flash(v):
            s = disassemble.string_at(fw, v)
            if s: out.append((a, v, s))
    return out


# ---------------------------------------------------------------- signature matching A<->B
def signature(e):
    r = ok[e]; ins = sorted(r['insns'].items()); sig = []
    for a, I in ins:
        t = I.mnem + ' ' + re.sub(r'0x[0-9A-F]{6,8}', 'T', I.ops) if I.kind != 'seq' or I.lit is None else I.mnem + ' ' + I.ops
        if I.kind in ('cjump', 'jump') and I.target is not None: t = I.mnem + ' %+d' % (I.target - e)
        if I.kind == 'call': t = 'bl'
        sig.append(t)
    return hash(tuple(sig))


sigs = collections.defaultdict(list)
for e in ok:
    if len(ok[e]['insns']) >= 4: sigs[signature(e)].append(e)
dup = {}
for s, l in sigs.items():
    if len(l) > 1:
        for e in l: dup[e] = [x for x in l if x != e]

# ---------------------------------------------------------------- functions.json
funcs_json = []
for e in sorted(ok):
    r = ok[e]; ff = flows[e]
    per = collections.OrderedDict(); regs = set()
    for m in ff.mem:
        c = dataflow.classify(m['ea'])
        if c:
            per.setdefault(c[0], set()).add(c[1]); regs.add(hx(m['ea']))
    sr = string_refs(e)
    ram = sorted({fw.u32(I.lit) for I in r['lits'].values() if I.litsize == 4 and 0x20000000 <= (fw.u32(I.lit) or 0) < 0x20010000})
    nm = FUNC_NAMES_FULL.get(e)
    auto = []
    if per: auto.append('touches ' + ', '.join(per))
    if sr: auto.append('strings: ' + '; '.join(repr(s[2][:30]) for s in sr[:3]))
    if not called_by[e] and not tail_by[e] and e not in vec_entries: auto.append('no static callers (dead code or called via pointer)')
    desc = nm[1] if nm else ('auto: ' + ' | '.join(auto) if auto else 'unknown')
    funcs_json.append(dict(
        address=hx(e), end_address=hx(func_end(e)), size=func_end(e) - e,
        name=nm[0] if nm else 'sub_%08X' % e, confidence=nm[2] if nm else 'auto',
        description=desc, image=image_of(e), source=fw.entries.get(e), n_instructions=len(r['insns']),
        arguments=None, returns=None,
        calls=sorted({hx(t) for t in r['calls'].values()}), tail_calls=sorted({hx(t) for t in r['tails'].values()}),
        indirect_calls=[hx(a) for a in r['icalls']], indirect_jumps=[hx(a) for a in r['ijumps']],
        jump_tables=[dict(insn=hx(a), table=hx(t['table']), entries=t['entries'], size=t['entry_size']) for a, t in r['tables'].items()],
        called_by=sorted(hx(c) for c in called_by[e]), peripheral_registers=sorted(regs),
        peripherals={k: sorted(v) for k, v in per.items()}, ram_literals=[hx(x) for x in ram],
        strings=[dict(insn=hx(a), addr=hx(v), text=s) for a, v, s in sr],
        duplicate_of=[hx(x) for x in dup.get(e, [])],
        evidence=[hx(x) for x in EVIDENCE.get(e, [])]))
json.dump(dict(sha256_of_dump=SHA, base=hx(BASE), images=[hx(i) for i in imgs], functions=funcs_json),
          open(os.path.join(out, 'disassembly', 'functions.json'), 'w'), indent=1)

# ---------------------------------------------------------------- references / xrefs
xrefs = []   # (from, to, type, from_func, to_func)
fn_of = {}
for e, r in ok.items():
    for a in r['insns']:
        fn_of.setdefault(a, e)
for e, r in ok.items():
    for a, t in r['calls'].items(): xrefs.append((a, t, 'call', e, t))
    for a, t in r['tails'].items(): xrefs.append((a, t, 'tailcall', e, t))
    for a, I in r['insns'].items():
        if I.kind in ('jump', 'cjump') and I.target is not None and I.target not in r['insns']: xrefs.append((a, I.target, 'jump_out', e, None))
        if I.lit is not None and I.litsize:
            v = fw.u32(I.lit) if I.litsize == 4 else None
            xrefs.append((a, I.lit, 'literal_load', e, None))
            if v is not None and fw.in_flash(v & ~1) and (v & 1) and (v & ~1) in ok: xrefs.append((a, v & ~1, 'funcptr_literal', e, v & ~1))
            elif v is not None and fw.in_flash(v):
                if disassemble.string_at(fw, v): xrefs.append((a, v, 'string_ref', e, None))
        elif I.mnem.startswith('adr') and I.lit and disassemble.string_at(fw, I.lit): xrefs.append((a, I.lit, 'string_ref', e, None))
    for a, t in r['tables'].items():
        for x in t['targets']: xrefs.append((a, x, 'jumptable_target', e, None))
for off, vt in fw.vectors.items():
    for i, nm, v in vt:
        if v and i > 0: xrefs.append((BASE + off + 4 * i, v & ~1, 'vector:' + nm, None, v & ~1))
with open(os.path.join(out, 'disassembly', 'cross_references.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['from_addr', 'to_addr', 'type', 'from_function', 'to_function'])
    for a, t, ty, ef, et in sorted(xrefs): w.writerow([hx(a), hx(t), ty, hx(ef) if ef else '', hx(et) if et else ''])

refs = dict(peripheral_accesses=[], call_sites=[], literals=[])
for e, ff in sorted(flows.items()):
    for m in ff.mem:
        c = dataflow.classify(m['ea'])
        if c: refs['peripheral_accesses'].append(dict(insn=hx(m['addr']), function=hx(e), address=hx(m['ea']), peripheral=c[0], register=c[1],
                                                       rw=m['rw'], size=m['size'], value=hx(m['val']) if m['val'] is not None else None))
    for c in ff.calls:
        args = {}
        for i in range(4):
            v = c['args'].get(i)
            if v: args['r%d' % i] = hx(v[1]) if v[0] == 'c' else 'sp+%d' % v[1]
        refs['call_sites'].append(dict(insn=hx(c['addr']), function=hx(e), target=hx(c['target']), known_args=args))
    for a, I in ok[e]['lits'].items():
        v = fw.u32(I.lit) if I.litsize == 4 else None
        refs['literals'].append(dict(insn=hx(a), literal_addr=hx(I.lit), size=I.litsize, value=hx(v) if v is not None else None,
                                     note=disassemble.annotate_value(fw, v, None) if v is not None else ''))
json.dump(refs, open(os.path.join(out, 'disassembly', 'references.json'), 'w'), indent=0)

# ---------------------------------------------------------------- full disassembly
disassemble.write_full(fw, flows, os.path.join(out, 'disassembly', 'full_disassembly.asm'))

# ---------------------------------------------------------------- strings
strings = []
d = fw.d
_cov = fw.covered()
for m in re.finditer(rb'[\x20-\x7e\n\r\t]{4,}', d):
    s = m.group()
    a = BASE + m.start()
    terminated = d[m.end():m.end() + 1] == b'\x00'
    letters = sum(1 for c in s if chr(c).isalpha())
    if a in _cov or (a + len(s) - 1) in _cov: continue
    if terminated and len(s.strip()) >= 4 and (re.search(rb'[A-Za-z]{2,}', s) or re.search(rb'%[dfsc.]', s)) and letters >= 1 and len(s.strip()) >= 4 and (sum(1 for c in s if chr(c) in ' %.:_-+\n\r0123456789') + letters) / len(s) > 0.85:
        strings.append((a, s.decode('ascii')))
users = collections.defaultdict(list)
for x in xrefs:
    if x[2] == 'string_ref':
        users[x[1]].append(x[0])
with open(os.path.join(out, 'resources', 'strings.txt'), 'w') as f:
    f.write('# addr | len | image | referenced_by(insn addrs) | text   (ASCII, NUL terminated; UTF-16 scan found none)\n')
    for a, s in strings:
        f.write('%s | %d | %s | %s | %r\n' % (hx(a), len(s), image_of(a), ','.join('%08X' % u for u in users.get(a, [])[:6]), s))

# ---------------------------------------------------------------- regions
reg = []   # start,end,type,image,note
def add(a, b, ty, note=''):
    if b > a: reg.append((a, b, ty, note))
for o in imgs: add(o, o + 0xC0 if True else o, 'vector_table', 'MSP + Reset + 16 system + IRQ vectors (up to IRQ59 are defined by STM32F103 high-density)')
codeset = {}
for e in ok:
    for a, I in ok[e]['insns'].items(): codeset[a] = I.size
lits = set(); jt = set()
for e, r in ok.items():
    for a, I in r['lits'].items():
        for i in range(I.litsize or 0): lits.add(I.lit + i)
    for a, t in r['tables'].items():
        for i in range(t['entries'] * t['entry_size']): jt.add(t['table'] + i)
strset = set()
for a, s in strings:
    for i in range(len(s) + 1): strset.add(a + i)
last = len(d)
while last and d[last - 1] == 0xFF: last -= 1
covered = fw.covered()
kind = {}
for a in range(BASE, BASE + len(d)):
    if a in covered: kind[a] = 'code'
    elif a in lits: kind[a] = 'literal_pool'
    elif a in jt: kind[a] = 'jump_table'
    elif a in strset: kind[a] = 'string'
    elif d[a - BASE] == 0xFF: kind[a] = 'erased_0xFF'
    else: kind[a] = 'data_unclassified'
for o in imgs:
    for a in range(o, o + 0x130):
        if kind[a] != 'erased_0xFF': kind[a] = 'vector_table_or_pad'
rows = []; a = BASE
while a < BASE + len(d):
    k = kind[a]; b = a
    while b < BASE + len(d) and kind[b] == k: b += 1
    rows.append([a, b, k]); a = b
# merge: code/literal/jump-table runs (and <=3-byte alignment gaps between them) -> 'code+literal_pools'
CP = ('code', 'literal_pool', 'jump_table')
merged = []
for r in rows:
    k = 'code+literal_pools' if r[2] in CP else r[2]
    if merged and merged[-1][2] == k: merged[-1][1] = r[1]
    elif merged and k == 'code+literal_pools' and merged[-2:-1] and merged[-1][1] - merged[-1][0] <= 3 and merged[-1][2] == 'data_unclassified' and merged[-2][2] == k:
        merged[-2][1] = r[1]; merged.pop()
    else: merged.append([r[0], r[1], k])
merged = [tuple(x) for x in merged]
# ---- image-level structure derived from the vector tables + scatter tables (parsed from the dump)
def parse_scatter(lo, hi):
    import struct
    return [struct.unpack_from('<IIII', d, o - BASE) for o in range(lo, hi, 16)]
SC = {}
for img, (lo, hi) in {'A': (0x0800ED54, 0x0800ED74), 'B': (0x08023308, 0x08023328)}.items():
    SC[img] = parse_scatter(lo, hi)
code_end = {}
for img in 'AB':
    ends = [func_end(e) for e in ok if image_of(e) == img]
    code_end[img] = max(ends)
plan = []
plan.append((imgs[0], imgs[0] + 0x130, 'vector_table_or_pad', 'A', 'MSP,Reset,exceptions,IRQ0-59 vectors at 0x08000000; scatter/startup stub begins at 0x130'))
for img, lo_s in (('A', imgs[0]), ('B', imgs[1])):
    pass
rows_final = []
def clip(a, b, k, im, note=''): rows_final.append((a, b, k, im, note))
# A
rows_final.append((imgs[0], imgs[0] + 0x130, 'vector_table_or_pad', 'A', 'initial MSP + 59 vectors (see VECTOR_TABLE.md)'))
for a, b, k in merged:
    if imgs[0] + 0x130 <= a < code_end['A'] and k != 'erased_0xFF' : rows_final.append((a, min(b, code_end['A']), k, 'A', ''))
    elif imgs[1] + 0x130 <= a < code_end['B'] and k != 'erased_0xFF': rows_final.append((a, min(b, code_end['B']), k, 'B', ''))
rows_final.append((imgs[1], imgs[1] + 0x130, 'vector_table_or_pad', 'B', 'initial MSP + 59 vectors (see VECTOR_TABLE.md)'))
rows_final += [
    (code_end['A'], 0x0800ED54, 'rodata_unclassified', 'A', 'glyph bitmaps / code-page tables (box-drawing UCS pairs seen at 0x0800A0B3); layout not fully decoded, see UNRESOLVED.md'),
    (0x0800ED54, 0x0800ED74, 'scatter_load_table', 'A', 'entry0: src 0x0800ED74 -> 0x20000000 len 0x10C (copy, handler 0x08009E68); entry1: ZI 0x2000010C len 0x7EBC (handler 0x08009E78)'),
    (0x0800ED74, 0x0800EE80, 'rw_initial_data', 'A', 'initialised globals copied to RAM 0x20000000..0x2000010C'),
    (0x0800EE80, 0x0800F000, 'erased_0xFF', '', 'free (end of bootloader image)'),
    (0x0800F000, 0x08010000, 'erased_0xFF', '', 'free 4 KiB gap between bootloader and application'),
    (code_end['B'], 0x08023308, 'rodata_unclassified', 'B', 'code-page/Unicode tables (e.g. 0x0801EC00 monotone 16-bit table), font bitmaps 0x0801F000..0x08023118, UI string table 0x080231A0..; see STRINGS_AND_RESOURCES.md'),
    (0x08023308, 0x08023328, 'scatter_load_table', 'B', 'entry0: src 0x08023328 -> 0x20000000 len 0x1F0 (copy, handler 0x0801E08A); entry1: ZI 0x200001F0 len 0x6A18 (handler 0x0801E14C)'),
    (0x08023328, 0x08023518, 'rw_initial_data', 'B', 'initialised globals copied to RAM 0x20000000..0x200001F0'),
    (0x08023518, 0x0803E860, 'erased_0xFF', '', 'free'),
    (0x0803E860, 0x0803E8C8, 'param_data', '', 'settings/parameter block; base 0x0803E864 is read by Param_ReadFlash 0x0801CF40 (words)'),
    (0x0803E8C8, 0x08040000, 'erased_0xFF', '', 'free'),
]
rows_final.sort()
with open(os.path.join(out, 'resources', 'binary_regions.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['start', 'end_exclusive', 'size', 'type', 'image', 'note'])
    for a, b, k, im, note in rows_final:
        if b > a: w.writerow([hx(a), hx(b), b - a, k, im, note])
# ---------------------------------------------------------------- GPIO map
GP = {0x40010800: 'A', 0x40010C00: 'B', 0x40011000: 'C', 0x40011400: 'D', 0x40011800: 'E', 0x40011C00: 'F', 0x40012000: 'G'}
MODE = {0x0: 'AIN', 0x4: 'IN_FLOATING', 0x28: 'IPD', 0x48: 'IPU', 0x14: 'OUT_OD', 0x10: 'OUT_PP', 0x1C: 'AF_OD', 0x18: 'AF_PP'}
SPD = {1: '10MHz', 2: '2MHz', 3: '50MHz'}
gpio_targets = {e for e, f in FUNC_NAMES_FULL.items() if f[0] == 'GPIO_Init'}
gpio_targets |= {t for e in ok for t in dup.get(0x08011112, [])} if 0x08011112 in dup else set()
gpio_targets.add(0x08011112)
gp_rows = []
for e, ff in sorted(flows.items()):
    for c in ff.calls:
        if c['target'] in gpio_targets or c['target'] in dup.get(0x08011112, []):
            a0 = c['args'].get(0); a1 = c['args'].get(1)
            port = GP.get(a0[1], hx(a0[1])) if a0 and a0[0] == 'c' else '?'
            pin = spd = mode = None
            if a1 and a1[0] == 'sp':
                pin = dataflow.stack_read(c['stack'], a1[1], 2); spd = dataflow.stack_read(c['stack'], a1[1] + 2, 1)
                mode = dataflow.stack_read(c['stack'], a1[1] + 3, 1)
            pins = ', '.join('P%s%d' % (port, i) for i in range(16) if pin is not None and pin >> i & 1) if pin is not None else 'UNRESOLVED(computed)'
            gp_rows.append((image_of(e), c['addr'], e, port, pin, pins, MODE.get(mode, hex(mode) if mode is not None else '?'), SPD.get(spd, spd)))
open(os.path.join(out, 'generated', '_gpio_rows.json'), 'w').write(json.dumps(gp_rows))

# ---------------------------------------------------------------- Markdown tables
def fname(a):
    n = FUNC_NAMES_FULL.get(a)
    return n[0] if n else 'sub_%08X' % a

with open(os.path.join(out, 'generated', '_auto_function_index.md'), 'w') as f:
    f.write('| Address | End | Size | Img | Name | Conf. | Calls (n) | Called by (n) | Peripherals | Description |\n|---|---|---|---|---|---|---|---|---|---|\n')
    for j in funcs_json:
        f.write('| %s | %s | %d | %s | %s | %s | %d | %d | %s | %s |\n' % (
            j['address'], j['end_address'], j['size'], j['image'], j['name'], j['confidence'], len(j['calls']), len(j['called_by']),
            ','.join(j['peripherals']) or '-', j['description'].replace('|', '/')[:110]))

# vectors
with open(os.path.join(out, 'generated', '_auto_vectors.md'), 'w') as f:
    for off, vt in sorted(fw.vectors.items()):
        f.write('\n### Vector table at 0x%08X (image %s)\n\n| # | Name | Raw | Handler | Handler name | Note |\n|---|---|---|---|---|---|\n' % (BASE + off, image_of(BASE + off)))
        default = collections.Counter(v for i, n, v in vt[16:]).most_common(1)[0][0]
        for i, nm, v in vt:
            if nm.startswith('rsv') and v == 0: continue
            note = 'default/empty handler (infinite loop)' if v == default and i >= 16 else ''
            f.write('| %d | %s | 0x%08X | %s | %s | %s |\n' % (i, nm, v, hx(v & ~1) if i else '-(MSP)', fname(v & ~1) if i else '-', note))

# call graph: main body of image B and A
def callees(e): return sorted({t for t in ok[e]['calls'].values()} | set(ok[e]['tails'].values()))
def mermaid(root, depth=2):
    lines = ['graph TD']; seen = set(); q = [(root, 0)]
    while q:
        e, d_ = q.pop(0)
        if e in seen or e not in ok: continue
        seen.add(e)
        if d_ >= depth: continue
        for t in callees(e):
            if t in ok:
                lines.append('  %s --> %s' % ('f%X["%s"]' % (e, fname(e)), 'f%X["%s"]' % (t, fname(t))))
                q.append((t, d_ + 1))
    return '\n'.join(sorted(set(lines[1:])) and ([lines[0]] + sorted(set(lines[1:]))))
open(os.path.join(out, 'generated', '_mermaid_B.md'), 'w').write('```mermaid\n' + mermaid(0x08010144, 1) + '\n```\n')
open(os.path.join(out, 'generated', '_mermaid_A.md'), 'w').write('```mermaid\n' + mermaid(0x08000174, 1) + '\n```\n')

# peripherals table
per_tab = collections.defaultdict(lambda: collections.defaultdict(set))
for e, ff in flows.items():
    for m in ff.mem:
        c = dataflow.classify(m['ea'])
        if c: per_tab[c[0]][c[1].split(' bit')[0].split('+')[0]].add(e)
with open(os.path.join(out, 'generated', '_auto_peripherals.md'), 'w') as f:
    f.write('| Peripheral | Registers touched (resolved by const-propagation) | Functions (img) |\n|---|---|---|\n')
    for p in sorted(per_tab):
        regs = sorted(per_tab[p]); fl = sorted({e for r in per_tab[p].values() for e in r})
        f.write('| %s | %s | %s |\n' % (p, ', '.join(regs), ', '.join('%08X(%s)' % (e, image_of(e)) for e in fl[:14]) + (' …(+%d)' % (len(fl) - 14) if len(fl) > 14 else '')))

# raw assets (no interpretation)
EA = os.path.join(out, 'resources', 'extracted_assets')
def dump_range(name, lo, hi): open(os.path.join(EA, name), 'wb').write(fw.d[lo - BASE:hi - BASE])
dump_range('A_rodata_0800A03E_0800ED54.bin', 0x0800A03E, 0x0800ED54)
dump_range('B_rodata_0801EA8A_08023308.bin', 0x0801EA8A, 0x08023308)
dump_range('B_fonts_candidate_0801F000_08023118.bin', 0x0801F000, 0x08023118)
dump_range('A_scatter_and_rw_0800ED54_0800EE80.bin', 0x0800ED54, 0x0800EE80)
dump_range('B_scatter_and_rw_08023308_08023518.bin', 0x08023308, 0x08023518)
dump_range('B_param_block_0803E860_0803E8C8.bin', 0x0803E860, 0x0803E8C8)
dump_range('A_image_08000000_0800EE80.bin', 0x08000000, 0x0800EE80)
dump_range('B_image_08010000_08023518.bin', 0x08010000, 0x08023518)
stat = dict(sha256=SHA, functions=len(ok), code_bytes=len(fw.covered()), strings=len(strings), xrefs=len(xrefs),
            noreturn=[hx(x) for x in sorted(fw.noreturn)], duplicate_funcs=len(dup))
json.dump(stat, open(os.path.join(out, 'generated', '_stats.json'), 'w'), indent=1)
print(json.dumps(stat, indent=1))
