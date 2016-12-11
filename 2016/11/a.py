#!/usr/bin/env python3

from collections import defaultdict
import fileinput
import itertools

def freeze(e, state):
    return (e, tuple(tuple(sorted(row)) for row in state))

initial_state = freeze(0, [
    ['PG', 'PM'],
    ['CG', 'cG', 'RG', 'pG'],
    ['CM', 'cM', 'RM', 'pM'],
    [],
])
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

def is_goal(state):
    e, rows = state
    return e == 3 and all(len(r) == 0 for r in rows[:-1])
    
from collections import deque
seen = set([initial_state])
#parent = {initial_state: None}
q = deque([(0, initial_state)])
while q:
    steps, state = q.popleft()
    steps += 1
    for n in next(state):
        if n in seen:
            continue
        #parent[n] = state
        seen.add(n)
        q.append((steps, n))
        if is_goal(n):
            print(steps)
            #while n is not None:
            #    print(n)
            #    n = parent[n]
            exit(0)
