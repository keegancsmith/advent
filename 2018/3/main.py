#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

lines = [l.strip().split() for l in open('input') if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if len(lines[0]) == 1:
    lines = [l[0] for l in lines]
#lines = [x.split() for x in '''#1 @ 1,3: 4x4
##2 @ 3,1: 4x4
##3 @ 5,5: 2x2'''.splitlines()]

def solveA(lines):
    d = defaultdict(int)
    for line in lines:
        x, y = map(int, line[2][:-1].split(','))
        dx, dy = map(int, line[3].split('x'))
        for i in range(x, x + dx):
            for j in range(y, y + dy):
                d[(i, j)] += 1
    ans = sum(1 if x > 1 else 0 for x in d.values())
    return ans

def solveB(lines):
    free = set()
    d = {}
    for line in lines:
        claim = line[0]
        x, y = map(int, line[2][:-1].split(','))
        dx, dy = map(int, line[3].split('x'))
        free.add(claim)
        for i in range(x, x + dx):
            for j in range(y, y + dy):
                k = (i, j)
                if k in d:
                    if d[k] in free:
                        free.remove(d[k])
                    if claim in free:
                        free.remove(claim)
                else:
                    d[k] = claim
    return free

print('A', solveA(lines))
print('B', solveB(lines))
