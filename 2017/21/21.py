#!/usr/bin/env python3

# Asciicast at https://asciinema.org/a/aW6iEsT4litBiMsGTBU21Sbq8

from collections import defaultdict

def rotate(p):
    x = p.split('/')
    d = len(x)
    rotations = [
        # Rotations clockwise
        lambda r, c : (r, c),
        lambda r, c : (c, d - r - 1),
        lambda r, c : (d - r - 1, d - c - 1),
        lambda r, c : (d - c - 1, r),
    ]

    flipC = [
        lambda r, c : (r, c),
        lambda r, c : (r, d - c - 1),
    ]

    flipR = [
        lambda r, c : (r, c),
        lambda r, c : (d - r - 1, c),
    ]
    for rot in rotations:
        for fc in flipC:
            for fr in flipR:
                t = lambda r, c : rot(*fc(*fr(r, c)))
                y = []
                for r in range(len(x)):
                    for c in range(len(x[r])):
                        r2, c2 = t(r, c)
                        y.append(x[r2][c2])
                    y.append('/')
                yield ''.join(y[:-1])

def divide(p):
    x = p.split('/')
    if len(x) % 2 == 0:
        d = 2
    elif len(x) % 3 == 0:
        d = 3
    else:
        assert False
    n = defaultdict(list)
    for r, row in enumerate(x):
        r = r // d
        for c, v in enumerate(row):
            n[(r, c // d)].append(v)
        for c in range(len(row) // d):
            n[(r, c)].append('/')
    for _, v in sorted(n.items()):
        yield ''.join(v[:-1])

def join(x):
    x = list(x)
    d = round(len(x) ** 0.5)
    rows = []
    for i, p in enumerate(x):
        x2 = p.split('/')
        if i % d == 0:
            for _ in x2:
                rows.append([])
        for j, y in enumerate(x2):
            rows[-len(x2)+j].append(y)
    return '/'.join(''.join(y) for y in rows)

lines = [l.strip().split() for l in open('input') if l.strip()]
d = {}
for p1, _, p2 in lines:
    for p in rotate(p1):
        d[p] = p2

print()
cur = '.#./..#/###'
for i in range(18):
    divide(cur)
    cur = join(d[p] for p in divide(cur))
    if i == 4:
        print('A', cur.count('#'))
print('B', cur.count('#'))
