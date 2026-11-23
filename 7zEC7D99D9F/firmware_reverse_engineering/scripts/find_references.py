#!/usr/bin/env python3
"""Query results of run_all.py.   python3 find_references.py <addr> [--dir ..]
Prints: function containing/at addr, callers, callees, literal loads of the value, peripheral accesses near it."""
import sys, os, json, csv, argparse
ap = argparse.ArgumentParser(); ap.add_argument('addr'); ap.add_argument('--dir', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
a = ap.parse_args(); x = int(a.addr, 0); D = a.dir
F = json.load(open(os.path.join(D, 'disassembly', 'functions.json')))['functions']
for f in F:
    s, e = int(f['address'], 0), int(f['end_address'], 0)
    if s <= x < e:
        print('FUNCTION', f['address'], f['name'], f['confidence'], '-', f['description'])
        print(' calls      :', f['calls']); print(' called_by  :', f['called_by']); print(' peripherals:', f['peripherals']); break
else:
    print('address not inside a known function')
print('XREFS to/from 0x%08X:' % x)
for r in csv.DictReader(open(os.path.join(D, 'disassembly', 'cross_references.csv'))):
    if int(r['from_addr'], 0) == x or int(r['to_addr'], 0) == x: print(' ', r['from_addr'], '->', r['to_addr'], r['type'])
R = json.load(open(os.path.join(D, 'disassembly', 'references.json')))
for p in R['peripheral_accesses']:
    if int(p['insn'], 0) == x or int(p['address'], 0) == x: print(' PERIPH', p)
