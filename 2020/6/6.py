#!/usr/bin/env python3

from functools import reduce

groups = [[]]
for line in open('input'):
    line = line.strip()
    if line:
        groups[-1].append(set(line))
    else:
        groups.append([])

print("A", sum(len(reduce(set.union,        group)) for group in groups))
print("B", sum(len(reduce(set.intersection, group)) for group in groups))
