#!/usr/bin/env python3

from collections import defaultdict

guards = defaultdict(lambda: [0] * 60)
for l in sorted(open('input')):
    if '#' in l:
        g = int(l.split('#')[1].split()[0])
    elif 'asleep' in l:
        start = int(l[15:17])
    else:
        end = int(l[15:17])
        for x in range(start, end):
            guards[g][x % 60] += 1

def solve(f):
    _, g, m = max((f(v), g, v.index(max(v))) for g, v in guards.items())
    return g * m

print("A:", solve(sum))
print("B:", solve(max))
