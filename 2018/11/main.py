#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

serial_num = 4842
def power(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_num
    power_level *= rack_id
    return (power_level % 1000) // 100 - 5
powers = [[power(x, y) for y in range(301)] for x in range(301)]

def solveA(powers):
    best = (0, 0, 0)
    size = 3
    for x, y in itertools.product(range(len(powers) - size), range(len(powers) - size)):
        a = sum(powers[x][y] for x,y in itertools.product(range(x, x + size), range(y, y + size)))
        if a > best[0]:
            best = (a, x, y)
    return "%d,%d" % best[1:]

def solveB(powers):
    N = len(powers)
    sum_x = [[0] * len(row) for row in powers]
    sum_y = [[0] * len(row) for row in powers]
    for x in range(N):
        sum_x[x][0] = powers[x][0]
        for y in range(1, N):
            sum_x[x][y] = sum_x[x][y-1] + powers[x][y]
    for y in range(N):
        sum_y[y][0] = powers[0][y]
        for x in range(1, N):
            sum_y[y][x] = sum_y[y][x-1] + powers[x][y]

    def row_sum(x, y1, y2):
        row = sum_x[x]
        y1 = 0 if y1 == 0 else row[y1-1]
        y2 = row[y2]
        return y2 - y1

    def col_sum(y, x1, x2):
        col = sum_y[y]
        x1 = 0 if x1 == 0 else col[x1-1]
        x2 = col[x2]
        return x2 - x1

    for (x, y) in itertools.product(range(N), range(N)):
        a = 0
        for size in range(1, N):
            x2 = x + size - 1
            y2 = y + size - 1
            if x2 == N or y2 == N:
                break
            a += row_sum(x2, y, y2) + col_sum(y2, x, x2) - powers[x2][y2]
            yield (a, x, y, size)

print(solveA(powers))
print(max(solveB(powers)))
