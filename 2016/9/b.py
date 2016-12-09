#!/usr/bin/env python3

import fileinput
import re

r = re.compile(r'\((\d+)x(\d+)\)')
def size(line):
    if not line:
        return 0
    m = r.search(line)
    if not m:
        return len(line)
    a, b = m.span()
    x, y = map(int, m.groups())
    assert(x != 0)
    x = min(x, len(line) - b)
    if x == 0:
        return a
    ## This has a weird boundary condition, hope for the best
    return a + size(line[b:b+x]) * y + size(line[b+x:])
    
        
def solve(line):
    print(line)
    print(size(line))
    print()

for line in fileinput.input():
    solve(line.strip())
