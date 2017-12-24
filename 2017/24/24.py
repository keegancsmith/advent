#!/usr/bin/env python3

from collections import defaultdict

# Started down the wrong path implementing some sort of dijkstra. Then
# realised that the only way to do this is via exhaustive searching of the
# Graph. Quickly got an answer then. Rank 41st for part 2. Live cast at
# https://asciinema.org/a/8QA1ECraopbuOLNGn4zqCsUFz

G = defaultdict(list)
for l in open('input'):
    a, b = map(int, l.split('/'))
    G[a].append(b)
    G[b].append(a)

def dfsA(G, seen, n):
    m = 0
    for c in G[n]:
        x = (c, n) if c < n else (n, c)
        if x in seen:
            continue
        seen.add(x)
        m = max(m, dfsA(G, seen, c) + c + n)
        seen.remove(x)
    return m

def dfsB(G, seen, n):
    m = (0, 0)
    for c in G[n]:
        x = (c, n) if c < n else (n, c)
        if x in seen:
            continue
        seen.add(x)
        l, s = dfsB(G, seen, c)
        m = max(m, (l + 1, s + c + n))
        seen.remove(x)
    return m

print('A', dfsA(G, set(), 0))
print('B', dfsB(G, set(), 0)[1])
