#!/usr/bin/env python3

from collections import defaultdict

# List of edges
E = []
for line in open('input'):
    line = line.split()
    a = ' '.join(line[:2])
    line = line[4:]
    while line:
        if line[0] == 'no':
            break
        w, b = int(line[0]), ' '.join(line[1:3])
        E.append((a, b, w))
        line = line[4:]

# Part A you do a DFS on the inverted graph starting at shiny gold.
G = defaultdict(list)
for a, b, w in E:
    G[b].append(a)
seen = set()
def dfsA(b):
    if b in seen:
        return 0
    seen.add(b)
    return 1 + sum(dfsA(a) for a in G[b])
print('A', dfsA('shiny gold') - 1)

# Part b you do a DFS on the graph.
G = defaultdict(list)
for a, b, w in E:
    G[a].append((w, b))
def dfsB(a):
    count = 1
    for w, b in G[a]:
        count += w * dfs(b)
    return count
print('B', dfsB('shiny gold') - 1)
