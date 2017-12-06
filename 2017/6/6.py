#!/usr/bin/env python3

# asciicast of me solving this at https://asciinema.org/a/JYydMvHuat7gDxaMKI9UUsAR0

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

lines = [l.strip().split() for l in open('input').readlines() if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass

def solveA(banks):
    seen = set()
    count = 0
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        count += 1
        m = max(banks)
        idx = banks.index(m)
        banks[idx] = 0
        for i in range(idx + 1, idx + m + 1):
            banks[i % len(banks)] += 1
    return count

def solveB(banks):
    seen = {}
    count = 0
    while tuple(banks) not in seen:
        seen[tuple(banks)] = count
        count += 1
        m = max(banks)
        idx = banks.index(m)
        banks[idx] = 0
        for i in range(idx + 1, idx + m + 1):
            banks[i % len(banks)] += 1
    return count - seen[tuple(banks)]

print(solveA(lines[0]))
print(solveB(lines[0]))
