#!/usr/bin/env python3

deltas = (
    ('e',   2, 0),
    ('w',  -2, 0),
    ('se',  1, -2),
    ('sw', -1, -2),
    ('nw', -1,  2),
    ('ne',  1,  2),
)

def dest(dirs):
    x, y = 0, 0
    while dirs:
        for d, dx, dy in deltas:
            if dirs.startswith(d):
                #print('{} ({}, {}) -> ({}, {})'.format(d.rjust(2), x, y, x + dx, y + dy))
                x, y = x + dx, y + dy
                dirs = dirs[len(d):]
                break
        else:
            assert False, dirs
    return (x, y)

def neigh(p):
    return ((p[0] + dx, p[1] + dy) for _, dx, dy in deltas)

assert dest('esew') == (1, -2)
assert dest('nwwswee') == (0, 0)

black = set()
for line in open('input'):
    p = dest(line.strip())
    if p in black:
        black.discard(p)
    else:
        black.add(p)
print('A', len(black))

for i in range(100):
    candidates = black.copy()
    candidates.update(*[neigh(p) for p in black])

    black_next = set()
    for p in candidates:
        count = sum(p2 in black for p2 in neigh(p))
        if 1 <= count <= 2 and p in black:
            black_next.add(p)
        elif count == 2 and p not in black:
            black_next.add(p)
    black = black_next

print('B', len(black))
