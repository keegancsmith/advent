#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

def solveA(lines):
    for line in lines:
        print(line)

def solveB(lines):
    pass

lines = [l.strip().split() for l in open('input') if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if all(len(l) == 1 for l in lines):
    lines = [l[0] for l in lines]

print('A', solveA(lines))
print('B', solveB(lines))

val = '80871224585914546619083218645595'
val = open('input').read().strip()
x = [ord(x) - ord('0') for x in val*10000]
phases = []
for i in range(1, len(x)+1):
    phase = []
    while len(phase) < len(x) + 1:
        for j in (0,1,0,-1):
            phase.extend([j] * i)
    phases.append(phase[1:len(x)+1])
for i in range(100):
    y = []
    for phase in phases:
        y.append(abs(sum(xi * p for xi, p in zip(x, phase))) % 10)
        #print(' + '.join('%s*%s' % (xi, p) for xi, p in zip(x, phase)) + ' = ' + str(y[-1]))
    x = y
    #print(x)
    
print(''.join(map(str, x[:8])))
