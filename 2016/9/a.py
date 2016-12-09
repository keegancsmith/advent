#!/usr/bin/env python3

import fileinput
import re

def solve(line):
    r = re.compile(r'\((\d+)x(\d+)\)')
    ans = 0
    while True:
        m = r.search(line)
        if not m:
            break
        a, b = m.span()
        x, y = map(int, m.groups())
        assert(x != 0)
        x = min(x, len(line) - b)
        if x == 0:
            line = line[:a]
            continue
        ans += a + x * y
        line = line[b+x:]
    print(ans + len(line))
    print()

for line in fileinput.input():
    solve(line.strip())
