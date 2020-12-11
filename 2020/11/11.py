#!/usr/bin/env python3

import itertools
from collections import defaultdict

def solveA(state):
    while True:
        next_state = {}
        for (x, y), v in state.items():
            neigh = ((x + dx, y + dy) for dx, dy in itertools.product(range(-1, 2), range(-1, 2)) if not (dx == dy == 0))
            c = [state.get(k, '.') for k in neigh].count('#')
            if v == 'L':
                next_state[(x, y)] = '#' if c == 0 else 'L'
            elif v == '#':
                next_state[(x, y)] = '#' if c < 4 else 'L'

        if next_state == state:
            break
        state = next_state

    return list(state.values()).count('#')

def solveB(state):
    # Create an adjacency list based on visibility
    maxX = max(x for (x, y) in state)
    maxY = max(y for (x, y) in state)
    G = defaultdict(list)
    for (x, y), v in state.items():
        for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
            if dx == dy == 0:
                continue
            x1, y1 = x, y
            while 0 <= x1 <= maxX and 0 <= y1 <= maxY:
                x1, y1 = x1 + dx, y1 + dy
                if (x1, y1) in state:
                    G[(x, y)].append((x1, y1))
                    break

    while True:
        next_state = {}
        for pos, v in state.items():
            c = [state[neigh] for neigh in G[pos]].count('#')
            if v == 'L':
                next_state[pos] = '#' if c == 0 else 'L'
            elif v == '#':
                next_state[pos] = '#' if c < 5 else 'L'

        if next_state == state:
            break
        state = next_state

    return list(state.values()).count('#')

lines = [l.strip() for l in open('input') if l.strip()]
initial = {(x, y): v for x, line in enumerate(lines) for y, v in enumerate(line) if v != '.'}

print('A', solveA(initial.copy()))
print('B', solveB(initial.copy()))
