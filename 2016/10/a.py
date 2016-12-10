#!/usr/bin/env python3

from collections import defaultdict
import fileinput

V = defaultdict(list)
E = []
O = {}
X = [17, 61]
#X = [5, 2]

for line in fileinput.input():
    p = line.strip().split()
    if p[0] == 'value':
        x, i = int(p[1]), int(p[-1])
        V[i].append(x)
    else:
        E.append((int(p[1]), p[5], int(p[6]), p[-2], int(p[-1])))
for v in V.values():
    assert len(v) <= 2
    v.sort()
changed = True
while changed:
    changed = False
    for i, lt, l, ht, h in E:
        if len(V[i]) < 2:
            continue
        if X[0] in V[i] and X[1] in V[i]:
            print('Part A', i)
        changed = True
        lv, hv = V[i][0], V[i][-1]
        V[i] = V[i][1:-1]
        if lt == 'bot':
            V[l].append(lv)
            V[l].sort()
        else:
            O[l] = lv
        if ht == 'bot':
            V[h].append(hv)
            V[h].sort()
        else:
            O[l] = hv


print('Part B', O[0]*O[1]*O[2])
