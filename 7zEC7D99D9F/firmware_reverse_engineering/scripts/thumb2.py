#!/usr/bin/env python3
"""Minimal-but-broad ARMv7-M (Cortex-M3) Thumb/Thumb-2 disassembler, pure Python.
Written because capstone / arm-objdump were not available in the analysis sandbox.
Covers: all 16-bit Thumb, and the 32-bit ARMv7-M integer instructions
(data processing, ld/st, ldm/stm, branches, mul/div, bit-field, misc control, tbb/tbh, ldrex/strex).
Not covered: coprocessor / FP / DSP extensions (absent on Cortex-M3); those print as 'udf.w'.
"""

COND = ['eq','ne','hs','lo','mi','pl','vs','vc','hi','ls','ge','lt','gt','le','al','nv']
RN = ['r0','r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','sp','lr','pc']
SYSM = {0:'apsr',1:'iapsr',2:'eapsr',3:'xpsr',5:'ipsr',6:'epsr',7:'iepsr',8:'msp',9:'psp',
        16:'primask',17:'basepri',18:'basepri_max',19:'faultmask',20:'control'}


def sx(v, bits):
    return v - (1 << bits) if v & (1 << (bits - 1)) else v


def hexs(v):
    v &= 0xFFFFFFFF
    return str(v) if v < 10 else '0x%X' % v


def imm_s(v):
    return ('#-' + hexs(-v)) if v < 0 else '#' + hexs(v)


def reglist(mask):
    return '{' + ', '.join(RN[i] for i in range(16) if mask >> i & 1) + '}'


def thumb_expand_imm(imm12):
    if (imm12 >> 10) == 0:
        b = imm12 & 0xFF
        m = (imm12 >> 8) & 3
        if m == 0:
            return b
        if m == 1:
            return (b << 16) | b
        if m == 2:
            return (b << 24) | (b << 8)
        return b * 0x01010101
    un = 0x80 | (imm12 & 0x7F)
    rot = imm12 >> 7
    return ((un >> rot) | (un << (32 - rot))) & 0xFFFFFFFF


class Insn:
    """kind: seq | call | jump | cjump | ret | cret | icall | ijump | tbb | tbh | it | undef"""
    __slots__ = ('addr', 'size', 'raw', 'mnem', 'ops', 'kind', 'target', 'lit', 'litsize', 'cond',
                 'reglist', 'rt', 'mem')

    def __init__(s, addr, size, raw):
        s.addr = addr; s.size = size; s.raw = raw
        s.mnem = ''; s.ops = ''; s.kind = 'seq'
        s.target = None; s.lit = None; s.litsize = 4; s.cond = None; s.reglist = 0
        s.rt = None; s.mem = None

    @property
    def text(s):
        return s.mnem + (' ' + s.ops if s.ops else '')


def shift_name(t, imm5):
    if t == 0: return ('lsl', imm5)
    if t == 1: return ('lsr', imm5 or 32)
    if t == 2: return ('asr', imm5 or 32)
    if imm5 == 0: return ('rrx', 0)
    return ('ror', imm5)


def sh_str(t, imm5):
    n, i = shift_name(t, imm5)
    if n == 'lsl' and i == 0: return ''
    if n == 'rrx': return ', rrx'
    return ', %s #%d' % (n, i)


# ---------------------------------------------------------------- 16-bit
def d16(h, a, in_it):
    I = Insn(a, 2, h)
    S = '' if in_it else 's'
    t = h >> 13
    if t == 0:
        op = (h >> 11) & 3
        if op != 3:
            imm = (h >> 6) & 31; rm = (h >> 3) & 7; rd = h & 7
            if op == 0 and imm == 0:
                I.mnem = 'mov' + S; I.ops = '%s, %s' % (RN[rd], RN[rm])
            else:
                nm = ['lsl', 'lsr', 'asr'][op]
                if op and imm == 0: imm = 32
                I.mnem = nm + S; I.ops = '%s, %s, #%d' % (RN[rd], RN[rm], imm)
        else:
            opc = (h >> 9) & 3; rn = (h >> 3) & 7; rd = h & 7; x = (h >> 6) & 7
            nm = 'add' if opc in (0, 2) else 'sub'
            I.mnem = nm + S
            I.ops = '%s, %s, %s' % (RN[rd], RN[rn], RN[x] if opc < 2 else '#%d' % x)
    elif t == 1:
        op = (h >> 11) & 3; rd = (h >> 8) & 7; imm = h & 255
        if op == 0: I.mnem = 'mov' + S; I.ops = '%s, #%s' % (RN[rd], hexs(imm))
        elif op == 1: I.mnem = 'cmp'; I.ops = '%s, #%s' % (RN[rd], hexs(imm))
        elif op == 2: I.mnem = 'add' + S; I.ops = '%s, #%s' % (RN[rd], hexs(imm))
        else: I.mnem = 'sub' + S; I.ops = '%s, #%s' % (RN[rd], hexs(imm))
    elif (h >> 10) == 0b010000:
        op = (h >> 6) & 15; rm = (h >> 3) & 7; rd = h & 7
        nm = ['and', 'eor', 'lsl', 'lsr', 'asr', 'adc', 'sbc', 'ror', 'tst', 'rsb', 'cmp', 'cmn', 'orr', 'mul', 'bic', 'mvn'][op]
        flagless = op in (8, 10, 11)
        I.mnem = nm + ('' if flagless else S)
        if op == 9: I.ops = '%s, %s, #0' % (RN[rd], RN[rm])
        elif op == 13: I.ops = '%s, %s, %s' % (RN[rd], RN[rm], RN[rd])
        else: I.ops = '%s, %s' % (RN[rd], RN[rm])
    elif (h >> 10) == 0b010001:
        op = (h >> 8) & 3
        if op == 3:
            rm = (h >> 3) & 15
            if h & 0x80:
                I.mnem = 'blx'; I.ops = RN[rm]; I.kind = 'icall'
            else:
                I.mnem = 'bx'; I.ops = RN[rm]; I.kind = 'ret' if rm == 14 else 'ijump'
        else:
            rd = ((h >> 4) & 8) | (h & 7); rm = (h >> 3) & 15
            I.mnem = ['add', 'cmp', 'mov'][op]; I.ops = '%s, %s' % (RN[rd], RN[rm])
            if op != 1 and rd == 15: I.kind = 'ijump'
    elif (h >> 11) == 0b01001:
        rt = (h >> 8) & 7; imm = (h & 255) * 4
        I.mnem = 'ldr'; I.lit = ((a + 4) & ~3) + imm; I.rt = rt
        I.ops = '%s, [pc, #%d]' % (RN[rt], imm)
    elif (h >> 12) == 0b0101:
        opc = (h >> 9) & 7; rm = (h >> 6) & 7; rn = (h >> 3) & 7; rt = h & 7
        I.mnem = ['str', 'strh', 'strb', 'ldrsb', 'ldr', 'ldrh', 'ldrb', 'ldrsh'][opc]
        I.ops = '%s, [%s, %s]' % (RN[rt], RN[rn], RN[rm]); I.rt = rt
    elif t == 3:
        B = (h >> 12) & 1; L = (h >> 11) & 1; imm = (h >> 6) & 31; rn = (h >> 3) & 7; rt = h & 7
        off = imm if B else imm * 4
        I.mnem = ('ldr' if L else 'str') + ('b' if B else '')
        I.ops = '%s, [%s%s]' % (RN[rt], RN[rn], (', #%d' % off) if off else ''); I.rt = rt
        I.mem = (rn, off)
    elif (h >> 12) == 0b1000:
        L = (h >> 11) & 1; imm = ((h >> 6) & 31) * 2; rn = (h >> 3) & 7; rt = h & 7
        I.mnem = 'ldrh' if L else 'strh'
        I.ops = '%s, [%s%s]' % (RN[rt], RN[rn], (', #%d' % imm) if imm else ''); I.rt = rt
        I.mem = (rn, imm)
    elif (h >> 12) == 0b1001:
        L = (h >> 11) & 1; rt = (h >> 8) & 7; imm = (h & 255) * 4
        I.mnem = 'ldr' if L else 'str'
        I.ops = '%s, [sp%s]' % (RN[rt], (', #%d' % imm) if imm else ''); I.rt = rt
        I.mem = (13, imm)
    elif (h >> 12) == 0b1010:
        rd = (h >> 8) & 7; imm = (h & 255) * 4
        if h & 0x800:
            I.mnem = 'add'; I.ops = '%s, sp, #%d' % (RN[rd], imm)
        else:
            I.mnem = 'adr'; I.lit = ((a + 4) & ~3) + imm; I.litsize = 0
            I.ops = '%s, 0x%X' % (RN[rd], I.lit)
    elif (h >> 12) == 0b1011:
        b = (h >> 8) & 15
        if b == 0:
            imm = (h & 127) * 4
            I.mnem = 'sub' if h & 0x80 else 'add'; I.ops = 'sp, sp, #%d' % imm
        elif b in (1, 3, 9, 11):
            imm = (((h >> 9) & 1) << 6) | (((h >> 3) & 31) << 1)
            I.mnem = 'cbnz' if h & 0x800 else 'cbz'
            I.target = a + 4 + imm; I.kind = 'cjump'
            I.ops = '%s, 0x%X' % (RN[h & 7], I.target)
        elif b == 2:
            I.mnem = ['sxth', 'sxtb', 'uxth', 'uxtb'][(h >> 6) & 3]; I.ops = '%s, %s' % (RN[h & 7], RN[(h >> 3) & 7])
        elif b == 6:
            if (h & 0xFFEC) == 0xB660:
                I.mnem = 'cpsid' if h & 0x10 else 'cpsie'
                I.ops = ('i' if h & 2 else '') + ('f' if h & 1 else '')
            else:
                I.mnem = 'cps?'
        elif b in (4, 5):
            m = (h & 255) | ((1 << 14) if h & 0x100 else 0)
            I.mnem = 'push'; I.ops = reglist(m); I.reglist = m
        elif b in (12, 13):
            m = (h & 255) | ((1 << 15) if h & 0x100 else 0)
            I.mnem = 'pop'; I.ops = reglist(m); I.reglist = m
            if m & 0x8000: I.kind = 'ret'
        elif b == 10:
            op = (h >> 6) & 3
            I.mnem = {0: 'rev', 1: 'rev16', 3: 'revsh'}.get(op, 'undef'); I.ops = '%s, %s' % (RN[h & 7], RN[(h >> 3) & 7])
        elif b == 14:
            I.mnem = 'bkpt'; I.ops = '#%d' % (h & 255)
        elif b == 15:
            if h & 15:
                I.mnem = 'it'; I.kind = 'it'; I.cond = ((h >> 4) & 15, h & 15)
            else:
                op = (h >> 4) & 15
                I.mnem = {0: 'nop', 1: 'yield', 2: 'wfe', 3: 'wfi', 4: 'sev'}.get(op, 'hint')
        else:
            I.mnem = 'undef'; I.kind = 'undef'
    elif (h >> 12) == 0b1100:
        L = (h >> 11) & 1; rn = (h >> 8) & 7; m = h & 255
        I.mnem = 'ldm' if L else 'stm'
        wb = '' if (L and (m >> rn) & 1) else '!'
        I.ops = '%s%s, %s' % (RN[rn], wb, reglist(m)); I.reglist = m
    elif (h >> 12) == 0b1101:
        c = (h >> 8) & 15
        if c == 15:
            I.mnem = 'svc'; I.ops = '#%d' % (h & 255)
        elif c == 14:
            I.mnem = 'udf'; I.ops = '#%d' % (h & 255); I.kind = 'undef'
        else:
            tgt = a + 4 + sx(h & 255, 8) * 2
            I.mnem = 'b' + COND[c]; I.target = tgt; I.kind = 'cjump'; I.ops = '0x%X' % tgt
    elif (h >> 11) == 0b11100:
        tgt = a + 4 + sx(h & 0x7FF, 11) * 2
        I.mnem = 'b'; I.target = tgt; I.kind = 'jump'; I.ops = '0x%X' % tgt
    else:
        I.mnem = 'undef'; I.kind = 'undef'
    return I


# ---------------------------------------------------------------- 32-bit
DP_OPS = {0: 'and', 1: 'bic', 2: 'orr', 3: 'orn', 4: 'eor', 6: 'pkh', 8: 'add', 10: 'adc', 11: 'sbc', 13: 'sub', 14: 'rsb'}


def mem_fmt(rn, off, mode='off'):
    if mode == 'off':
        return '[%s%s]' % (RN[rn], (', ' + imm_s(off)) if off else '')
    if mode == 'pre':
        return '[%s, %s]!' % (RN[rn], imm_s(off))
    return '[%s], %s' % (RN[rn], imm_s(off))


def d32(h1, h2, a):
    I = Insn(a, 4, (h1 << 16) | h2)
    # ------- 11110 : branches, misc control, immediate data processing
    if (h1 >> 11) == 0b11110:
        if h2 & 0x8000:
            S = (h1 >> 10) & 1
            if (h2 & 0x5000) in (0x1000, 0x5000):          # B.W (T4) / BL
                J1 = (h2 >> 13) & 1; J2 = (h2 >> 11) & 1
                I1 = (~(J1 ^ S)) & 1; I2 = (~(J2 ^ S)) & 1
                imm = (S << 24) | (I1 << 23) | (I2 << 22) | ((h1 & 0x3FF) << 12) | ((h2 & 0x7FF) << 1)
                tgt = (a + 4 + sx(imm, 25)) & 0xFFFFFFFF
                I.target = tgt; I.ops = '0x%X' % tgt
                if h2 & 0x4000:
                    I.mnem = 'bl'; I.kind = 'call'
                else:
                    I.mnem = 'b.w'; I.kind = 'jump'
                return I
            if (h2 & 0x5000) == 0x0000:
                c = (h1 >> 6) & 15
                if c < 14:
                    J1 = (h2 >> 13) & 1; J2 = (h2 >> 11) & 1
                    imm = (S << 20) | (J2 << 19) | (J1 << 18) | ((h1 & 0x3F) << 12) | ((h2 & 0x7FF) << 1)
                    tgt = (a + 4 + sx(imm, 21)) & 0xFFFFFFFF
                    I.mnem = 'b' + COND[c] + '.w'; I.target = tgt; I.kind = 'cjump'; I.ops = '0x%X' % tgt
                    return I
                if (h1 & 0xFFF0) == 0xF380 and (h2 & 0xFF00) == 0x8800:
                    I.mnem = 'msr'; I.ops = '%s, %s' % (SYSM.get(h2 & 0xFF, 'sysm%d' % (h2 & 0xFF)), RN[h1 & 15]); return I
                if h1 == 0xF3EF and (h2 & 0xF000) == 0x8000:
                    I.mnem = 'mrs'; I.ops = '%s, %s' % (RN[(h2 >> 8) & 15], SYSM.get(h2 & 0xFF, 'sysm%d' % (h2 & 0xFF))); return I
                if h1 == 0xF3BF and (h2 & 0xFF00) == 0x8F00:
                    I.mnem = {0x40: 'dsb', 0x50: 'dmb', 0x60: 'isb'}.get(h2 & 0xF0, 'barrier?'); return I
            I.mnem = 'udf.w'; I.kind = 'undef'; return I
        i = (h1 >> 10) & 1; imm3 = (h2 >> 12) & 7; imm8 = h2 & 255
        rd = (h2 >> 8) & 15; rn = h1 & 15
        if not (h1 & 0x200):                                # modified immediate
            op = (h1 >> 5) & 15; Sb = (h1 >> 4) & 1
            imm12 = (i << 11) | (imm3 << 8) | imm8
            val = thumb_expand_imm(imm12)
            nm = DP_OPS.get(op)
            if nm is None:
                I.mnem = 'udf.w'; I.kind = 'undef'; return I
            iv = '#' + hexs(val)
            if op == 0 and rd == 15 and Sb: I.mnem = 'tst'; I.ops = '%s, %s' % (RN[rn], iv)
            elif op == 4 and rd == 15 and Sb: I.mnem = 'teq'; I.ops = '%s, %s' % (RN[rn], iv)
            elif op == 8 and rd == 15 and Sb: I.mnem = 'cmn'; I.ops = '%s, %s' % (RN[rn], iv)
            elif op == 13 and rd == 15 and Sb: I.mnem = 'cmp.w'; I.ops = '%s, %s' % (RN[rn], iv)
            elif op == 2 and rn == 15: I.mnem = 'mov' + ('s' if Sb else '') + '.w'; I.ops = '%s, %s' % (RN[rd], iv)
            elif op == 3 and rn == 15: I.mnem = 'mvn' + ('s' if Sb else ''); I.ops = '%s, %s' % (RN[rd], iv)
            else:
                I.mnem = nm + ('s' if Sb else '') + '.w'; I.ops = '%s, %s, %s' % (RN[rd], RN[rn], iv)
            return I
        op = (h1 >> 4) & 31
        imm12 = (i << 11) | (imm3 << 8) | imm8
        if op == 0 or op == 10:
            sub = (op == 10)
            if rn == 15:
                base = (a + 4) & ~3
                I.lit = (base - imm12) if sub else (base + imm12); I.litsize = 0
                I.mnem = 'adr.w'; I.ops = '%s, 0x%X' % (RN[rd], I.lit)
            else:
                I.mnem = 'subw' if sub else 'addw'; I.ops = '%s, %s, #%s' % (RN[rd], RN[rn], hexs(imm12))
        elif op == 4 or op == 12:
            imm16 = (rn << 12) | (i << 11) | (imm3 << 8) | imm8
            I.mnem = 'movw' if op == 4 else 'movt'; I.ops = '%s, #%s' % (RN[rd], hexs(imm16))
        elif op in (16, 18, 24, 26):
            sat = (h2 & 31) + (0 if op in (24, 26) else 1); sh = (h1 >> 5) & 1; im5 = (imm3 << 2) | ((h2 >> 6) & 3)
            I.mnem = 'usat' if op in (24, 26) else 'ssat'
            I.ops = '%s, #%d, %s%s' % (RN[rd], sat, RN[rn], (', %s #%d' % ('asr' if sh else 'lsl', im5)) if im5 else '')
        elif op in (20, 28):
            lsb = (imm3 << 2) | ((h2 >> 6) & 3); w = (h2 & 31) + 1
            I.mnem = 'sbfx' if op == 20 else 'ubfx'; I.ops = '%s, %s, #%d, #%d' % (RN[rd], RN[rn], lsb, w)
        elif op == 22:
            lsb = (imm3 << 2) | ((h2 >> 6) & 3); msb = h2 & 31
            if rn == 15:
                I.mnem = 'bfc'; I.ops = '%s, #%d, #%d' % (RN[rd], lsb, msb - lsb + 1)
            else:
                I.mnem = 'bfi'; I.ops = '%s, %s, #%d, #%d' % (RN[rd], RN[rn], lsb, msb - lsb + 1)
        else:
            I.mnem = 'udf.w'; I.kind = 'undef'
        return I
    # ------- 0xE8/0xE9 : ldm/stm, ldrd/strd, exclusive, tbb
    if (h1 >> 9) == 0b1110100:
        op = (h1 >> 7) & 3; W = (h1 >> 5) & 1; L = (h1 >> 4) & 1; rn = h1 & 15
        if not (h1 & 0x40):
            m = h2
            if op == 1:
                if W and L and rn == 13:
                    I.mnem = 'pop.w'; I.ops = reglist(m)
                else:
                    I.mnem = ('ldm' if L else 'stm') + '.w'; I.ops = '%s%s, %s' % (RN[rn], '!' if W else '', reglist(m))
            elif op == 2:
                if W and not L and rn == 13:
                    I.mnem = 'push.w'; I.ops = reglist(m)
                else:
                    I.mnem = ('ldmdb' if L else 'stmdb'); I.ops = '%s%s, %s' % (RN[rn], '!' if W else '', reglist(m))
            else:
                I.mnem = 'srs/rfe'; I.kind = 'undef'; return I
            I.reglist = m
            if L and (m & 0x8000): I.kind = 'ret'
            return I
        o2 = (h1 >> 4) & 3
        rt = (h2 >> 12) & 15; rt2 = (h2 >> 8) & 15; imm = (h2 & 255) * 4
        if op == 0 and o2 == 0:
            I.mnem = 'strex'; I.ops = '%s, %s, %s' % (RN[rt2], RN[rt], mem_fmt(rn, imm)); return I
        if op == 0 and o2 == 1:
            I.mnem = 'ldrex'; I.ops = '%s, %s' % (RN[rt], mem_fmt(rn, imm)); return I
        if op == 1 and o2 == 1 and (h2 & 0xFFE0) == 0xF000:
            rm = h2 & 15
            if h2 & 0x10:
                I.mnem = 'tbh'; I.ops = '[%s, %s, lsl #1]' % (RN[rn], RN[rm]); I.kind = 'tbh'
            else:
                I.mnem = 'tbb'; I.ops = '[%s, %s]' % (RN[rn], RN[rm]); I.kind = 'tbb'
            return I
        if op == 1 and o2 in (0, 1):
            t = h2 & 0xF0
            if o2 == 1:
                I.mnem = {0x40: 'ldrexb', 0x50: 'ldrexh'}.get(t, 'ldrex?'); I.ops = '%s, [%s]' % (RN[rt], RN[rn])
            else:
                I.mnem = {0x40: 'strexb', 0x50: 'strexh'}.get(t, 'strex?'); I.ops = '%s, %s, [%s]' % (RN[h2 & 15], RN[rt], RN[rn])
            return I
        P = (h1 >> 8) & 1; U = (h1 >> 7) & 1
        off = imm if U else -imm
        if rn == 15 and L:
            I.lit = (((a + 4) & ~3) + off) & 0xFFFFFFFF; I.litsize = 8
            I.mnem = 'ldrd'; I.ops = '%s, %s, [pc, %s]' % (RN[rt], RN[rt2], imm_s(off)); return I
        mode = 'off' if (P and not W) else ('pre' if (P and W) else 'post')
        I.mnem = 'ldrd' if L else 'strd'; I.ops = '%s, %s, %s' % (RN[rt], RN[rt2], mem_fmt(rn, off, mode))
        return I
    # ------- 0xEA/0xEB : data processing, shifted register
    if (h1 >> 9) == 0b1110101:
        op = (h1 >> 5) & 15; Sb = (h1 >> 4) & 1; rn = h1 & 15
        imm3 = (h2 >> 12) & 7; rd = (h2 >> 8) & 15; imm2 = (h2 >> 6) & 3; ty = (h2 >> 4) & 3; rm = h2 & 15
        sh = sh_str(ty, (imm3 << 2) | imm2)
        nm = DP_OPS.get(op)
        if nm is None:
            I.mnem = 'udf.w'; I.kind = 'undef'; return I
        if op == 0 and rd == 15 and Sb: I.mnem = 'tst.w'; I.ops = '%s, %s%s' % (RN[rn], RN[rm], sh)
        elif op == 4 and rd == 15 and Sb: I.mnem = 'teq'; I.ops = '%s, %s%s' % (RN[rn], RN[rm], sh)
        elif op == 8 and rd == 15 and Sb: I.mnem = 'cmn.w'; I.ops = '%s, %s%s' % (RN[rn], RN[rm], sh)
        elif op == 13 and rd == 15 and Sb: I.mnem = 'cmp.w'; I.ops = '%s, %s%s' % (RN[rn], RN[rm], sh)
        elif op == 2 and rn == 15:
            n, iv = shift_name(ty, (imm3 << 2) | imm2)
            if n == 'lsl' and iv == 0:
                I.mnem = 'mov' + ('s' if Sb else '') + '.w'; I.ops = '%s, %s' % (RN[rd], RN[rm])
            elif n == 'rrx':
                I.mnem = 'rrx' + ('s' if Sb else ''); I.ops = '%s, %s' % (RN[rd], RN[rm])
            else:
                I.mnem = n + ('s' if Sb else '') + '.w'; I.ops = '%s, %s, #%d' % (RN[rd], RN[rm], iv)
        elif op == 3 and rn == 15:
            I.mnem = 'mvn' + ('s' if Sb else '') + '.w'; I.ops = '%s, %s%s' % (RN[rd], RN[rm], sh)
        elif op == 6:
            I.mnem = 'pkhbt' if not (ty & 2) else 'pkhtb'; I.ops = '%s, %s, %s%s' % (RN[rd], RN[rn], RN[rm], sh)
        else:
            I.mnem = nm + ('s' if Sb else '') + '.w'; I.ops = '%s, %s, %s%s' % (RN[rd], RN[rn], RN[rm], sh)
        return I
    # ------- 0xF8/0xF9 : load/store single
    if (h1 >> 9) == 0b1111100:
        Sg = (h1 >> 8) & 1; im12 = (h1 >> 7) & 1; sz = (h1 >> 5) & 3; L = (h1 >> 4) & 1; rn = h1 & 15
        rt = (h2 >> 12) & 15
        if sz == 3:
            I.mnem = 'udf.w'; I.kind = 'undef'; return I
        suf = ['b', 'h', ''][sz]
        nm = ('ldr' + ('s' if Sg else '') + suf) if L else ('str' + suf)
        if L and rt == 15 and sz != 2:
            I.mnem = 'pld'; I.ops = '[%s]' % RN[rn]; return I
        I.rt = rt
        if rn == 15 and L:
            off = h2 & 0xFFF
            if not im12: off = -off
            I.lit = (((a + 4) & ~3) + off) & 0xFFFFFFFF; I.litsize = [1, 2, 4][sz]
            I.mnem = nm + '.w'; I.ops = '%s, [pc, %s]' % (RN[rt], imm_s(off))
            if rt == 15: I.kind = 'ijump'
            return I
        if im12:
            off = h2 & 0xFFF
            I.mnem = nm + '.w'; I.ops = '%s, %s' % (RN[rt], mem_fmt(rn, off)); I.mem = (rn, off)
        elif h2 & 0x800:
            P = (h2 >> 10) & 1; U = (h2 >> 9) & 1; Wb = (h2 >> 8) & 1; off = h2 & 255
            if not U: off = -off
            if (h2 & 0xF00) == 0xE00:
                I.mnem = nm + 't'; I.ops = '%s, [%s, #%d]' % (RN[rt], RN[rn], h2 & 255)
            else:
                mode = 'off' if (P and not Wb) else ('pre' if (P and Wb) else 'post')
                I.mnem = nm + '.w' if mode == 'off' else nm
                I.ops = '%s, %s' % (RN[rt], mem_fmt(rn, off, mode))
                if mode == 'off': I.mem = (rn, off)
        else:
            rm = h2 & 15; sh = (h2 >> 4) & 3
            I.mnem = nm + '.w'; I.ops = '%s, [%s, %s%s]' % (RN[rt], RN[rn], RN[rm], (', lsl #%d' % sh) if sh else '')
        if L and rt == 15: I.kind = 'ijump'
        return I
    # ------- 0xFA : register shifts, extends, misc
    if (h1 >> 8) == 0xFA:
        rd = (h2 >> 8) & 15; rm = h2 & 15; rn = h1 & 15
        if (h2 & 0xF000) == 0xF000:
            if (h2 & 0xF0) == 0 and not (h1 & 0x80):
                ty = (h1 >> 5) & 3; Sb = (h1 >> 4) & 1
                I.mnem = ['lsl', 'lsr', 'asr', 'ror'][ty] + ('s' if Sb else '') + '.w'
                I.ops = '%s, %s, %s' % (RN[rd], RN[rn], RN[rm]); return I
            if (h2 & 0xC0) == 0x80 and not (h1 & 0x80):
                o = (h1 >> 4) & 7; rot = ((h2 >> 4) & 3) * 8
                nm = {0: 'sxth', 1: 'uxth', 2: 'sxtb16', 3: 'uxtb16', 4: 'sxtb', 5: 'uxtb'}.get(o)
                if nm and rn == 15:
                    I.mnem = nm + '.w'; I.ops = '%s, %s%s' % (RN[rd], RN[rm], (', ror #%d' % rot) if rot else ''); return I
                if nm:
                    I.mnem = nm.replace('xt', 'xta'); I.ops = '%s, %s, %s' % (RN[rd], RN[rn], RN[rm]); return I
            if (h1 & 0xF0) == 0x90 and (h2 & 0xF0) in (0x80, 0x90, 0xA0, 0xB0):
                I.mnem = {0x80: 'rev.w', 0x90: 'rev16.w', 0xA0: 'rbit', 0xB0: 'revsh.w'}[h2 & 0xF0]
                I.ops = '%s, %s' % (RN[rd], RN[rm]); return I
            if (h1 & 0xF0) == 0xB0 and (h2 & 0xF0) == 0x80:
                I.mnem = 'clz'; I.ops = '%s, %s' % (RN[rd], RN[rm]); return I
        I.mnem = 'udf.w'; I.kind = 'undef'; return I
    # ------- 0xFB : multiply / divide
    if (h1 >> 8) == 0xFB:
        rn = h1 & 15; rm = h2 & 15; rd = (h2 >> 8) & 15; ra = (h2 >> 12) & 15
        o1 = (h1 >> 4) & 15; o2 = (h2 >> 4) & 15
        if o1 == 0 and o2 == 0:
            if ra == 15:
                I.mnem = 'mul'; I.ops = '%s, %s, %s' % (RN[rd], RN[rn], RN[rm])
            else:
                I.mnem = 'mla'; I.ops = '%s, %s, %s, %s' % (RN[rd], RN[rn], RN[rm], RN[ra])
            return I
        if o1 == 0 and o2 == 1:
            I.mnem = 'mls'; I.ops = '%s, %s, %s, %s' % (RN[rd], RN[rn], RN[rm], RN[ra]); return I
        if o1 == 9 and o2 == 0xF:
            I.mnem = 'sdiv'; I.ops = '%s, %s, %s' % (RN[rd], RN[rn], RN[rm]); return I
        if o1 == 11 and o2 == 0xF:
            I.mnem = 'udiv'; I.ops = '%s, %s, %s' % (RN[rd], RN[rn], RN[rm]); return I
        if o2 == 0 and o1 in (8, 10, 12, 14):
            I.mnem = {8: 'smull', 10: 'umull', 12: 'smlal', 14: 'umlal'}[o1]
            I.ops = '%s, %s, %s, %s' % (RN[ra], RN[rd], RN[rn], RN[rm]); return I
        I.mnem = 'udf.w'; I.kind = 'undef'; return I
    I.mnem = 'udf.w'; I.kind = 'undef'
    return I


# ---------------------------------------------------------------- driver
def is32(h):
    return (h >> 11) in (0b11101, 0b11110, 0b11111)


def decode_at(data, off, base, it_state=None):
    """Decode one instruction at file offset `off`.
    it_state: list of pending IT conditions (applies to this insn) or None.
    Returns (Insn, new_it_state) or (None, None) at end of data."""
    a = base + off
    if off + 2 > len(data):
        return None, None
    h = data[off] | (data[off + 1] << 8)
    in_it = bool(it_state)
    if is32(h):
        if off + 4 > len(data):
            return None, None
        h2 = data[off + 2] | (data[off + 3] << 8)
        I = d32(h, h2, a)
    else:
        I = d16(h, a, in_it)
    new_it = None
    if in_it:
        c = it_state[0]
        if I.kind != 'it':
            suffix = COND[c]
            m = I.mnem
            m = (m[:-2] + suffix + '.w') if m.endswith('.w') else (m + suffix)
            I.mnem = m; I.cond = c
            if I.kind == 'jump': I.kind = 'cjump'
            elif I.kind == 'ret': I.kind = 'cret'
            elif I.kind == 'call': I.kind = 'ccall'
            elif I.kind == 'icall': I.kind = 'cicall'
        new_it = it_state[1:] or None
    if I.kind == 'it':
        fc, mask = I.cond
        tz = 0
        while not (mask >> tz) & 1:
            tz += 1
        n = 4 - tz
        conds = [fc]; pat = ''
        for i in range(1, n):
            bit = (mask >> (4 - i)) & 1
            if bit == (fc & 1):
                pat += 't'; conds.append(fc)
            else:
                pat += 'e'; conds.append(fc ^ 1)
        I.mnem = 'it' + pat; I.ops = COND[fc]; I.cond = None
        new_it = conds
    return I, new_it


def decode_range(data, start, end, base):
    out = []; off = start; it = None
    while off < end:
        I, it = decode_at(data, off, base, it)
        if I is None:
            break
        out.append(I); off += I.size
    return out


if __name__ == '__main__':
    import sys
    d = open(sys.argv[1], 'rb').read()
    b = int(sys.argv[4], 0) if len(sys.argv) > 4 else 0x08000000
    s = int(sys.argv[2], 0); e = int(sys.argv[3], 0)
    for I in decode_range(d, s - b, e - b, b):
        print('%08X: %-8s %s' % (I.addr, ('%04X' % I.raw) if I.size == 2 else ('%08X' % I.raw), I.text))
