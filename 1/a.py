#!/usr/bin/env python3

import fileinput

dirs = next(fileinput.input()).strip().split(', ')
x, y, z = 0, 0, 0
for d in dirs:
    t, n = d[0], int(d[1:])
    if t == 'R':
        z = (z - 1) % 4
    else:
        z = (z + 1) % 4
    if z % 4 >= 2:
        n *= -1
    if z % 2 == 0:
        x, y = x, y + n
    else:
        x, y = x + n, y
print(abs(x) + abs(y))
