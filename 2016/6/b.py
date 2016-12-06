#!/usr/bin/env python3

from collections import defaultdict
import fileinput
counts = [defaultdict(int) for _ in range(8)]
for line in fileinput.input():
    for i, c in enumerate(line.strip()):
        counts[i][c] += 1
print(''.join(min((y,x) for x, y in c.items())[1] for c in counts))
