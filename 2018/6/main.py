#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

def solveA(points):
    minx = min(p[0] for p in points)
    maxx = max(p[0] for p in points)
    miny = min(p[1] for p in points)
    maxy = max(p[1] for p in points)
    sizes = defaultdict(int)
    inf = set()
    x1 = minx - 1 - (maxx - minx)
    x2 = maxx + 1 + (maxx - minx)
    y1 = miny - 1 - (maxy - miny)
    y2 = maxy + 1 + (maxy - miny)
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            wp, wd = None, 2*(maxx - minx + maxy - miny)
            smallest = True
            for p, (px, py) in enumerate(points):
                d = abs(px - x) + abs(py - y)
                if d < wd:
                    wp, wd = p, d
                    smallest = True
                elif d == wd:
                    smallest = False
            if smallest:
                sizes[wp] += 1
                if x == x1 or x == x2 or y == y1 or y == y2:
                    inf.add(wp)
    for p in inf:
        del sizes[p]
    return max(sizes.values())

def distbounds(xs, dx):
    x1 = max(x - dx + 1 for x in xs)
    x2 = min(x + dx - 1 for x in xs)
    for x1 in range(x1, x2 + 1):
        d = sum(abs(x1 - x) for x in xs)
        if d < dx:
            break
    for x2 in range(x2, x1 - 1, -1):
        d = sum(abs(x1 - x) for x in xs)
        if d < dx:
            break
    return (x1-1, x2+1)
    

def solveB(points):
    x1, x2 = distbounds([p[0] for p in points], 10000)
    y1, y2 = distbounds([p[1] for p in points], 10000)
    print(x1, x2, y1, y2)
    ans = 0
    per = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            d = 0
            for px, py in points:
                d += abs(px - x) + abs(py - y)
                if d >= 10000:
                    break
            if d < 10000:
                ans += 1
        per2 = int(1.0 * (x - x1) / (x2 - x1 + 1) * 100)
        if per2 != per:
            per = per2
            print("%d%%" % per)
    return ans

lines = [l.strip().split(', ') for l in open('input') if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if all(len(l) == 1 for l in lines):
    lines = [l[0] for l in lines]
print()
#print('A', solveA(lines))
#print('B', solveB(lines))
