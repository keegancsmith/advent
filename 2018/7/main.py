#!/usr/bin/env python3

from collections import defaultdict

lines = [l.strip().split() for l in open('input') if l.strip()]

V = set()
G = defaultdict(list)
for l in lines:
    a, b = l[1], l[-3]
    G[a].append(b)
    V.add(a)
    V.add(b)

for vs in G.values():
    vs.sort()

def compute_valence():
    valence = defaultdict(int)
    for v, vs in G.items():
        valence[v] += 0
        for c in vs:
            valence[c] += 1
    return valence

valence = compute_valence()
V = sorted(list(V))
ans = []
while V:
    for v in V:
        if valence[v] == 0:
            ans.append(v)
            for c in G[v]:
                valence[c] -= 1
            V.remove(v)
            break
print('A:', ''.join(ans))

valence = compute_valence()
q = [v for v, n in valence.items() if n == 0]
w = []
t = 0
while q or w:
    assert len(w) <= 5
    if len(w) < 5 and q:
        v = min(q)
        q.remove(v)
        w.append((t + 60 + 1 + ord(v) - ord('A'), v))
    else:
        assert w
        t, v = min(w)
        w.remove((t, v))
        for c in G[v]:
            valence[c] -= 1
            if valence[c] == 0:
                q.append(c)
                
print('B:', t)
