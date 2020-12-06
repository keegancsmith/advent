#!/usr/bin/env python3

from functools import reduce

data = open('input').read()
groups = [[set(line) for line in group.split()] for group in data.split('\n\n')]

print("A", sum(len(reduce(set.union,        group)) for group in groups))
print("B", sum(len(reduce(set.intersection, group)) for group in groups))
