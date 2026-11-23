#!/usr/bin/env python3
"""Standalone string scanner.  python3 extract_strings.py <dump.bin> [--min 4] [--base 0x08000000]
Reports ASCII (NUL-terminated or not), UTF-16LE and GBK-like (0xA1-0xF7 pair) runs. No analysis dependencies."""
import re, sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument('dump'); ap.add_argument('--min', type=int, default=4); ap.add_argument('--base', default='0x08000000')
a = ap.parse_args(); d = open(a.dump, 'rb').read(); base = int(a.base, 0)
print('# ASCII')
for m in re.finditer(rb'[\x20-\x7e\n\r\t]{%d,}' % a.min, d):
    t = d[m.end():m.end() + 1] == b'\x00'
    print('0x%08X len=%d nul=%s %r' % (base + m.start(), len(m.group()), t, m.group().decode()))
print('# UTF-16LE (>=%d chars)' % a.min)
n16 = 0
for m in re.finditer(rb'(?:[\x20-\x7e]\x00){%d,}' % a.min, d):
    n16 += 1; print('0x%08X %r' % (base + m.start(), m.group().decode('utf-16le')))
print('# UTF-16 hits:', n16)
print('# GBK-like double-byte runs (>=3 chars)')
n = 0
for m in re.finditer(rb'(?:[\xb0-\xf7][\xa1-\xfe]){3,}', d):
    n += 1; print('0x%08X %s' % (base + m.start(), m.group().hex()))
print('# GBK-like hits:', n)
