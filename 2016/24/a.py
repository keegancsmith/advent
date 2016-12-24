#!/usr/bin/env python3

import fileinput
import itertools
from collections import defaultdict, deque, namedtuple
import hashlib
import bisect
import heapq

nodes = {}
vals = {}
for r, line in enumerate(fileinput.input()):
    for c, v in enumerate(line.strip()):
        if v != '#':
            nodes[(r, c)] = v
            if v != '.':
                vals[v] = (r, c)

def bfs(nodes, p):
    dists = {}
    dists[p] = 0
    q = deque([(0, p)])
    while q:
        d, p = q.popleft()
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            p2 = (p[0] + dx, p[1] + dy)
            if p2 not in nodes or p2 in dists:
                continue
            dists[p2] = d + 1
            q.append((d + 1, p2))
    return dists

dists = {}
for v, p in vals.items():
    d = bfs(nodes, p)
    for v2, p2 in vals.items():
        if v2 != v:
            dists[(v, v2)] = d[p2]

partb = True
least = len(nodes) * len(vals)
for vs in itertools.permutations(list(vals.keys())):
    if vs[0] != '0':
        continue
    if partb:
        x = sum(dists[v] for v in zip(vs, vs[1:] + ('0',)))
    else:
        x = sum(dists[v] for v in zip(vs, vs[1:]))
    if x < least:
        print(vs, x)
        least = x
print(least)
