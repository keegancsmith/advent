#!/usr/bin/env python3

from collections import defaultdict

def solveA(claims):
    d = defaultdict(int)
    for _, x, y, dx, dy in claims:
        for i in range(x, x + dx):
            for j in range(y, y + dy):
                d[(i, j)] += 1
    return sum(1 if x > 1 else 0 for x in d.values())

def solveB(lines):
    free = set()
    d = {}
    for claim, x, y, dx, dy in claims:
        free.add(claim)
        for i in range(x, x + dx):
            for j in range(y, y + dy):
                k = (i, j)
                if k in d:
                    free.discard(d[k])
                    free.discard(claim)
                else:
                    d[k] = claim
    assert(len(free) == 1)
    return free.pop()

claims = []
for line in open('input'):
    parts = line.split()
    claim = int(parts[0][1:])
    x, y = map(int, parts[2][:-1].split(','))
    dx, dy = map(int, parts[3].split('x'))
    claims.append((claim, x, y, dx, dy))

print('A', solveA(claims))
print('B', solveB(claims))
