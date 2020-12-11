#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

def count_adjacent(state, x, y):
    c = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < len(state) and 0 <= y1 < len(state[x1]) and state[x1][y1] == '#':
                c += 1
    return c

# * If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# * If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# * Otherwise, the seat's state does not change.
def next_cell(state, x, y):
    v = state[x][y]
    if v == 'L':
        return '#' if count_adjacent(state, x, y) == 0 else 'L'
    elif v == '#':
        return '#' if count_adjacent(state, x, y) < 4 else 'L'
    else:
        return v

def solveA(lines):
    last = tuple()
    state = tuple(tuple(l) for l in lines)
    while True:
        next_state = tuple(tuple(next_cell(state, x, y) for y in range(len(state[0]))) for x in range(len(state)))
        if state == next_state:
            break
        state = next_state
    return sum(row.count('#') for row in state)

def solveB(lines):
    G = defaultdict(list)
    state = {}
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            if v == '.':
                continue
            state[(x, y)] = v
            
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == 0:
                        continue
                    x1, y1 = x + dx, y + dy
                    while 0 <= x1 < len(lines) and 0 <= y1 < len(lines[x1]):
                        if lines[x1][y1] != '.':
                            G[(x, y)].append((x1, y1))
                            break
                        x1, y1 = x1 + dx, y1 + dy

    while True:
        next_state = {}
        for pos, v in state.items():
            c = [state[neigh] for neigh in G[pos]].count('#')
            if v == 'L':
                next_state[pos] = '#' if c == 0 else 'L'
            elif v == '#':
                next_state[pos] = '#' if c < 5 else 'L'
            else:
                assert False
        if next_state == state:
            break
        state = next_state
            
    return list(state.values()).count('#')

data = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
data = open('input').read()
lines = [l.strip().split() for l in data.splitlines() if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if all(len(l) == 1 for l in lines):
    lines = [l[0] for l in lines]

print('A', solveA(lines))
print('B', solveB(lines))
