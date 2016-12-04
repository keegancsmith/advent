#!/usr/bin/env python3

from collections import defaultdict

def validate(x):
    y = defaultdict(int)
    parts = x.split('-')[:-1]
    for p in parts:
        for c in p:
            y[c] += 1
    checksum = ''.join(b for _, b in sorted(((-count, c) for c, count in y.items())))[:5]
    last = x[:-1].split('-')[-1]
    sector, got = last.split('[')
    if got == checksum:
        return int(sector)
    return 0
    
import fileinput
ans = 0
for line in fileinput.input():
    ans += validate(line.strip())
print(ans)
