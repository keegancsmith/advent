#!/usr/bin/env python3

import fileinput

dirs = next(fileinput.input()).strip().split(', ')
seen = set((0, 0))
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y, z = 0, 0, 0
for d in dirs:
    t, n = d[0], int(d[1:])
    if t == 'R':
        z = (z - 1) % 4
    else:
        z = (z + 1) % 4
    dx, dy = delta[z]
    for i in range(n):
        x, y = x + dx, y + dy
        if (x, y) in seen:
            print(abs(x) + abs(y))
            exit(0)
        seen.add((x, y))
print(abs(x) + abs(y))
