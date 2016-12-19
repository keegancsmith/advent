#!/usr/bin/env python3

from collections import defaultdict, deque
import fileinput
import hashlib

N = 3004953
left = list(range(1, N)) + [0]
right = [N - 1] + list(range(N - 1))
i = 0
while left[i] != i:
    left[i] = left[left[i]]
    right[left[i]] = i
    i = left[i]
print(i + 1)    
    
