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

data = '''
'''
# data = open('input').read()
lines = [l.strip().split() for l in data.readlines() if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if all(len(l) == 1 for l in lines):
    lines = [l[0] for l in lines]

print('A', solveA(lines))
print('B', solveB(lines))
