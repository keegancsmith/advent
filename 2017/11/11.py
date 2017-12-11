#!/usr/bin/env python3

from collections import deque

# Asciicast at https://asciinema.org/a/ZmFNlAge1zHATpejUAuw4uUlf Was slow. I
# need to carry a pen and paper, I am sure there is a nice way to represent
# the coordinates so that you can just calculate the distance to origin with a
# formula. Instead I implemented a BFS.
#
# Also I restarted my emacs and my elisp was all broken for interacting with
# aoc :'(

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

delta = {
    'n':  (0, 2),
    'ne':  (1, 1),
    'nw':  (-1, 1),
    'sw':  (-1, -1),
    's':  (0, -2),
    'se':  (1, -1),
}

def neighbours(x, y):
    for dx, dy in delta.values():
        yield (x + dx, y + dy)

q = deque([((0, 0), 0)])
seen = {}
def dist(target):
    if target in seen:
        return seen[target]
    while q:
        p, d = q.popleft()
        for np in neighbours(p[0], p[1]):
            if np in seen:
                continue
            seen[np] = d + 1
            q.append((np, d + 1))
        if p == target:
            return d
        
path = next(open('input')).strip().split(',')
p = (0, 0)
maxd = 0
for s in path:
    dx, dy = delta[s]
    p = (p[0] + dx, p[1] + dy)
    maxd = max(maxd, dist(p))
print('A', dist(p))
print('B', maxd)
