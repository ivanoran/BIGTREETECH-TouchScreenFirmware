#!/usr/bin/env python3
"""Print the ordered call sites of a function with constant-propagated r0-r3 arguments.
Usage: python3 call_sequence.py <dump.bin> 0x0801738A [more addrs]
('sp+N' = pointer into the caller's stack frame, '?' = unknown)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analyze, dataflow
fw = analyze.build(sys.argv[1], verbose=False)
flows = dataflow.analyze_all(fw)
for a in sys.argv[2:]:
    e = int(a, 0) & ~1
    print('##', hex(e))
    for c in flows[e].calls:
        args = ['?' if c['args'].get(i) is None else ('0x%X' % c['args'][i][1] if c['args'][i][0] == 'c' else 'sp+%d' % c['args'][i][1]) for i in range(4)]
        print('  %08X bl %08X (%s)' % (c['addr'], c['target'], ', '.join(args)))
