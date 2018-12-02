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

def solveA(lines):
    t2 = 0
    t3 = 0
    for line in lines:
        d = defaultdict(int)
        for c in line[0]:
            d[c]+=1
        twice = False
        thrice = False
        for v in d.values():
            if v == 2:
                twice = True
            if v == 3:
                thrice = True
        if twice:
            t2 += 1
        if thrice:
            t3 += 1
    return t2 * t3

def solveB(lines):
    d = {}
    for line in lines:
        s = line[0]
        for i in range(len(s) - 1):
            k = s[:i] + '_' + s[i+1:]
            if k in d:
                return s[:i] + s[i+1:]
            d[k] = s

print('A', solveA(lines))
print('B', solveB(lines))
