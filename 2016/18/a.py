#!/usr/bin/env python3

from collections import defaultdict, deque
import fileinput
import hashlib

row = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
print(row)
n = 400000
count = row.count('.')
for i in range(n - 1):
    g = lambda j : row[j] if 0 <= j < len(row) else '.'
    row = ['^' if (g(j-1) + g(j) + g(j + 1)) in ('^^.', '.^^', '^..', '..^') else '.' for j in range(len(row))]
    count += row.count('.')
    #print(''.join(row))

print(count)
