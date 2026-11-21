#!/usr/bin/env python3
"""Полный линейный дизассемблинг регионов дампа -> текстовые файлы (для grep/поиска).

Использование:
  python3 full_disasm.py <dump.bin> <out_dir> [lo_hex hi_hex ...]

По умолчанию разбирает загрузчик (0x08000000-0x08010000) и приложение
(0x08010000-0x08024000) прошивки Anycubic TFT v0.0.2.
Зависимости: pip install capstone
"""
import sys
import re
from capstone import *

BASE = 0x08000000

PERIPH = {
    0x40010000: 'AFIO', 0x40021000: 'RCC',
    0x40010800: 'GPIOA', 0x40010C00: 'GPIOB', 0x40011000: 'GPIOC',
    0x40011400: 'GPIOD', 0x40011800: 'GPIOE', 0x40012000: 'GPIOG',
    0x40013800: 'USART1', 0x40013000: 'SPI1', 0x40003800: 'SPI2',
    0x40003C00: 'SPI3', 0x40000C00: 'TIM5', 0x40000000: 'TIM2',
    0xA0000000: 'FSMC', 0x70000000: 'NAND_B2', 0x80000000: 'NAND_B3',
    0x60000000: 'LCD_CMD_win', 0x60200000: 'LCD_DATA_win',
}
GREG = {0x00: 'CRL', 0x04: 'CRH', 0x08: 'IDR', 0x0C: 'ODR',
        0x10: 'BSRR', 0x14: 'BRR', 0x18: 'LCKR'}
RREG = {0x00: 'CR', 0x04: 'CFGR', 0x14: 'AHBENR', 0x18: 'APB2ENR', 0x1C: 'APB1ENR'}
FREG = {0x00: 'BCR1', 0x04: 'BTR1', 0x08: 'BCR2', 0x0C: 'BTR2', 0x10: 'BCR3',
        0x14: 'BTR3', 0x18: 'BCR4', 0x1C: 'BTR4', 0x100: 'PCR2', 0x104: 'SR2',
        0x10C: 'PMEM2', 0x110: 'PATT2', 0x140: 'PCR3', 0x144: 'SR3',
        0x14C: 'PMEM3', 0x150: 'PATT3', 0x180: 'PCR4', 0x194: 'ECCR2', 0x19C: 'ECCR3'}


def annotate(op_str):
    out = op_str
    for h in re.findall(r'#(0x[0-9a-f]{8,10})', op_str):
        v = int(h, 16)
        if v in PERIPH:
            out = out.replace(h, PERIPH[v]); continue
        for base, name in PERIPH.items():
            off = v - base
            if 0 < off < 0x400:
                if name.startswith('GPIO') and off in GREG:
                    out = out.replace(h, f'{name}.{GREG[off]}')
                elif name == 'RCC' and off in RREG:
                    out = out.replace(h, f'RCC.{RREG[off]}')
                elif name == 'FSMC' and off in FREG:
                    out = out.replace(h, f'FSMC.{FREG[off]}')
                break
    return out


def disasm_region(data, lo, hi, out_path):
    md = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
    lines, addr = [], lo
    while addr < hi:
        code = data[addr - BASE:addr - BASE + 4]
        try:
            ins = next(md.disasm(code, addr))
        except StopIteration:
            addr += 2; continue
        if ins.address >= hi: break
        ann = annotate(ins.op_str)
        mark = f'  ; <<< {ann}' if ann != ins.op_str else ''
        lines.append(f'{ins.address:#010x}  {ins.bytes.hex():<10} {ins.mnemonic:<8} {ann}{mark}')
        addr += ins.size
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f'{out_path}: {len(lines)} instructions')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    data = open(sys.argv[1], 'rb').read()
    out_dir = sys.argv[2].rstrip('/') + '/'
    regions = [(0x08000000, 0x08010000, 'boot'), (0x08010000, 0x08024000, 'app')]
    if len(sys.argv) >= 5:
        regions = [(int(sys.argv[3], 16), int(sys.argv[4], 16), 'custom')]
    for lo, hi, tag in regions:
        disasm_region(data, lo, hi, f'{out_dir}{tag}_disasm.txt')
