#!/usr/bin/env python3

from collections import defaultdict
import fileinput

def dragon(x):
    return x + ['0'] + ['1' if a == '0' else '0' for a in reversed(x)]

def checksum(x):
    x = ['1' if a == b else '0' for a, b in zip(x[::2], x[1::2])]
    if len(x) % 2 == 0:
        x = checksum(x)
    return x

def solve(init, want):
    A = list(init)
    while len(A) < want:
        A = dragon(A)
    A = A[:want]
    return ''.join(checksum(A))
    
A = '00111101111101000'
print(solve('00111101111101000', 35651584))
