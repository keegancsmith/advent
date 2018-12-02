#!/usr/bin/env python3

from collections import defaultdict

ids = [l.strip() for l in open('input') if l.strip()]

def solveA(ids):
    t2 = 0
    t3 = 0
    for s in ids:
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        counts = set(d.values())
        if 2 in counts:
            t2 += 1
        if 3 in counts:
            t3 += 1
    return t2 * t3

def solveB(ids):
    seen = set()
    for s in ids:
        for i in range(len(s)):
            k = s[:i] + '_' + s[i+1:]
            if k in seen:
                return s[:i] + s[i+1:]
            seen.add(k)

print('A', solveA(ids))
print('B', solveB(ids))
