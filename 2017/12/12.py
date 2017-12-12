#!/usr/bin/env python3

# This is a cleaned up version of what I did live. You can see me solve it
# live at https://asciinema.org/a/NGH7dZ7ERLnT6s3QeIwVgV8zj
# Position 40th and 44th. Cast is 6m36s.

G = {}
for line in open('input'):
    line = line.strip().split()
    G[line[0]] = [x.strip(',') for x in line[2:]]

seen = set()
def dfs(n):
    if n in seen:
        return
    seen.add(n)
    for x in G[n]:
        dfs(x)

dfs('0')
print('A', len(seen))

seen = set()
components = 0
while len(seen) < len(G):
    n = (set(G.keys()) - seen).pop()
    dfs(n)
    components += 1
print('B', components)
