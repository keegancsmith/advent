#!/usr/bin/env python3

import fileinput

blacklist = [tuple(map(int, x.strip().split('-'))) for x in fileinput.input()]
blacklist.sort()
blacklist.append((4294967295 + 1, 4294967295 + 1))
frontier = 0
parta = None
partb = 0
for a, b in blacklist:
    if frontier < a:
        if parta is None:
            parta = frontier
        partb += (a - frontier)
    frontier = max(frontier, b + 1)
print(parta)
print(partb)
