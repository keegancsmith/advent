#!/usr/bin/env python3

from collections import defaultdict
import fileinput
import itertools

def freeze(e, state):
    return (e, tuple(tuple(sorted(row)) for row in state))

# Part b
initial_state = freeze(0, [
    ['PG', 'PM', 'EG', 'EM', 'DG', 'DM'],
    ['CG', 'cG', 'RG', 'pG'],
    ['CM', 'cM', 'RM', 'pM'],
    [],
])
# Part a
#initial_state = freeze(0, [
#    ['PG', 'PM'],
#    ['CG', 'cG', 'RG', 'pG'],
#    ['CM', 'cM', 'RM', 'pM'],
#    [],
#])
# Sample
#initial_state = freeze(0, [
#    ['HM', 'LM'],
#    ['HG'],
#    ['LG'],
#    [],
#])

def is_fried(row):
    if len(row) == 1:
        return False
    g = set(x[0] for x in row if x[1] == 'G')
    m = set(x[0] for x in row if x[1] == 'M')
    return len(g) > 0 and len(m - g) != 0

def next(state):
    e, rows = state
    for x in itertools.chain(itertools.combinations(rows[e], 1), itertools.combinations(rows[e], 2)):
        if is_fried(x):
            continue
        new_row = tuple(r for r in rows[e] if r not in x)
        if is_fried(new_row):
            continue
        for e2 in (e - 1, e + 1):
            if e2 < 0 or e2 > 3:
                continue
            if is_fried(x + rows[e2]):
                continue
            new_row2 = tuple(sorted(rows[e2] + x))
            yield (e2, tuple(new_row if i == e else (new_row2 if i == e2 else r)
                             for i, r in enumerate(rows)))

def goal(state):
    r = state[1]
    return (3, ((), (), (), tuple(sorted(r[0] + r[1] + r[2] + r[3]))))
    
from collections import deque
seen = [{initial_state: 0}, {goal(initial_state): 0}]
q = deque([(0, 0, initial_state), (0, 1, goal(initial_state))])
while q:
    steps, si, state = q.popleft()
    steps += 1
    for n in next(state):
        if n in seen[si]:
            continue
        if n in seen[(si + 1) % 2]:
            print(steps + seen[(si + 1 % 2)][n])
            exit(0)
        seen[si][n] = steps
        q.append((steps, si, n))
