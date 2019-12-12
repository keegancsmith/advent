#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

def doNext(pos, vel):
    for i, p in enumerate(pos):
        for j in range(i % 3, len(pos), 3):
            if i == j:
                continue
            if p < pos[j]:
                vel[i] += 1
            elif p > pos[j]:
                vel[i] -= 1
    for i, p in enumerate(pos):
        pos[i] = p + vel[i]

def solveA(pos):
    pos = list(a for p in pos for a in p)
    vel = [0] * len(pos)
    for step in range(1000):
        doNext(pos, vel)
    ans = 0
    for i in range(0, len(pos), 3):
        p, v = 0, 0
        for j in range(i, i + 3):
            p += abs(pos[j])
            v += abs(vel[j])
        ans += p * v
    return ans

def solveB(pos):
    # Is not fast enough yet :( Giving up
    pos = list(a for p in pos for a in p)
    vel = [0] * len(pos)
    seen = set()
    step = 0
    while True:
        if step % 100000 == 0:
            print(step, pos, vel)
        k = (tuple(pos), tuple(vel))
        if k in seen:
            return step
        seen.add(k)
        doNext(pos, vel)
        step += 1

pos = ((19, -10, 7), (1, 2, -3), (14, -4, 1), (8, 7, -6))
#pos = ((-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1))


print("A", solveA(pos))
print("B", solveB(pos))
