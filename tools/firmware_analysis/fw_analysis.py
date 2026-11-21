#!/usr/bin/env python3
"""Анализ дампа стоковой прошивки Anycubic TFT v0.0.2 (STM32F103VCT6).

Использование:
  python3 fw_analysis.py <dump.bin> lits <lo_hex> <hi_hex>   # периферия в регионе
  python3 fw_analysis.py <dump.bin> dis  <off_hex> [n]       # дизассемблинг (offset от 0x08000000)
  python3 fw_analysis.py <dump.bin> find <val_hex>           # поиск 32-бит литералов

Зависимости: pip install capstone
См. docs/hardware_analysis_anycubic_tft_v2.md — карта результатов.
"""
import struct, re, sys
from capstone import *

BASE = 0x08000000

PERIPH = {
    0x40010000: 'AFIO', 0x40010400: 'EXTI', 0x40021000: 'RCC',
    0x40010800: 'GPIOA', 0x40010C00: 'GPIOB', 0x40011000: 'GPIOC',
    0x40011400: 'GPIOD', 0x40011800: 'GPIOE', 0x40011C00: 'GPIOF',
    0x40012000: 'GPIOG',
    0x40013800: 'USART1', 0x40004400: 'USART2', 0x40004800: 'USART3',
    0x40013000: 'SPI1', 0x40003800: 'SPI2', 0x40003C00: 'SPI3',
    0x40000C00: 'TIM5', 0x40000400: 'TIM3',
    0xA0000000: 'FSMC_BCR1', 0xA0000004: 'FSMC_BTR1',
    0xA0000008: 'FSMC_BCR2', 0xA000000C: 'FSMC_BTR2',
    0xA0000010: 'FSMC_BCR3', 0xA0000014: 'FSMC_BTR3',
    0xA0000018: 'FSMC_BCR4', 0xA000001C: 'FSMC_BTR4',
    0xA0000100: 'FSMC_PCR2', 0xA0000140: 'FSMC_PCR3', 0xA0000180: 'FSMC_PCR4',
    0xA000010C: 'FSMC_PMEM2', 0xA000014C: 'FSMC_PMEM3',
    0xA0000110: 'FSMC_PATT2', 0xA0000150: 'FSMC_PATT3',
    0x70000000: 'NAND_Bank2_DATA', 0x70010000: 'NAND_Bank2_CMD',
    0x70020000: 'NAND_Bank2_ADDR',
    0x80000000: 'NAND_Bank3',
    0x60000000: 'FSMC_Bank1_CMD_win', 0x60200000: 'FSMC_Bank1_DATA_win_A20',
    0x60100000: 'FSMC_Bank1_DATA_A19x2', 0x60400000: 'FSMC_Bank1_A21_win',
}

GREG = {0x00: 'CRL', 0x04: 'CRH', 0x08: 'IDR', 0x0C: 'ODR',
        0x10: 'BSRR', 0x14: 'BRR', 0x18: 'LCKR'}
RREG = {0x00: 'CR', 0x04: 'CFGR', 0x08: 'CIR', 0x0C: 'APB2RSTR',
        0x10: 'APB1RSTR', 0x14: 'AHBENR', 0x18: 'APB2ENR', 0x1C: 'APB1ENR'}


def addr_name(a):
    if a in PERIPH: return PERIPH[a]
    for base, name in PERIPH.items():
        off = a - base
        if 0 <= off < 0x400:
            if name.startswith('GPIO') and off in GREG:
                return f'{name}.{GREG[off]}'
            if name == 'RCC' and off in RREG:
                return f'RCC.{RREG[off]}'
            return f'{name}+{off:#x}'
    return None


def find_literals(data, value):
    pat = struct.pack('<I', value)
    out, i = [], data.find(pat)
    while i != -1:
        out.append(i); i = data.find(pat, i + 1)
    return out


def disasm(data, off, n=60):
    md = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
    code, base, out = data[off:off + n * 4 + 32], BASE + off, []
    for ins in md.disasm(code, base):
        ann = addr_name(int(imm, 16)) if (imm := next(iter(re.findall(r'#(0x[0-9a-f]+)', ins.op_str)), None)) else None
        mark = f'  ; <<< {ann}' if ann else ''
        out.append(f'{ins.address:#010x}  {ins.bytes.hex():<10} {ins.mnemonic:<8} {ins.op_str}{mark}')
        if len(out) >= n: break
    return '\n'.join(out)


def region_report(data, lo, hi):
    hits = {}
    for v in PERIPH:
        for off in find_literals(data, v):
            if lo <= off < hi:
                hits.setdefault(PERIPH[v], []).append(hex(off))
    return hits


def main():
    if len(sys.argv) < 3:
        print(__doc__); return 1
    data = open(sys.argv[1], 'rb').read()
    cmd = sys.argv[2]
    if cmd == 'lits':
        for k in sorted(region_report(data, int(sys.argv[3], 16), int(sys.argv[4], 16))):
            print(f'{k}: {region_report(data, int(sys.argv[3], 16), int(sys.argv[4], 16))[k]}')
    elif cmd == 'dis':
        print(disasm(data, int(sys.argv[3], 16), int(sys.argv[4]) if len(sys.argv) > 4 else 60))
    elif cmd == 'find':
        for o in find_literals(data, int(sys.argv[3], 16)): print(hex(o))
    else:
        print(__doc__); return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
