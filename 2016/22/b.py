#!/usr/bin/env python3

import fileinput
import itertools
from collections import defaultdict, deque, namedtuple
import hashlib
import bisect
import heapq

lines = list(l.strip().split() for l in fileinput.input())[2:]
nodes = {}
Disk = namedtuple('Disk', ['size', 'used', 'avail'])
for l in lines:
    d = Disk(*list(int(x[:-1]) for x in l[1:4]))
    x, y = [int(x[1:]) for x in l[0].split('-')[1:]]
    nodes[(x, y)] = d

def with_a(item):
    d, p, nodes = item
    return (d + p[0] + p[1], d, p, nodes)

maxx, maxy = max(x for x, y in nodes), max(y for x, y in nodes)
for y in range(maxy + 1):
    line = []
    for x in range(maxx + 1):
        n = nodes[(x, y)]
        #line.append('%d/%d' % (n.avail, n.used))
        #line.append(str(n.used).ljust(3))
        line.append(str(n.avail).ljust(3))
    print(' '.join(line))
