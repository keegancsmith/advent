#!/usr/bin/env python3

import fileinput
import itertools
from collections import defaultdict, deque
import hashlib
import bisect

lines = list(l.strip().split() for l in fileinput.input())[2:]
nodes = []
for l in lines:
    size, used, avail = [int(x[:-1]) for x in l[1:4]]
    nodes.append((avail, used, size))
nodes.sort()
count = 0
for i, (avail, used, size) in enumerate(nodes):
    if used == 0:
        continue
    j = bisect.bisect_left(nodes, (used, -1, -1))
    count += len(nodes) - j
    if i >= j:
        count -= 1
print(count)
