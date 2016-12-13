#!/usr/bin/env python3

from collections import deque
import fileinput


def open(x, y):
    F = 1364
    #F = 10
    n = x*x + 3*x + 2*x*y + y + y*y + F
    return bin(n).count('1') % 2 == 0

S = (1, 1)
G = (31, 39)
#G = (7, 4)
seen = set([S])
Q = deque([(0, S)])
while Q:
    d, p = Q.popleft()
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        x, y = p[0] + dx, p[1] + dy
        p2 = (x, y)
        if x < 0 or y < 0 or p2 in seen or not open(x, y) or d + 1 > 50:
            continue
        seen.add(p2)
        Q.append((d + 1, p2))

print(len(seen))
