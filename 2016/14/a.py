#!/usr/bin/env python3

import fileinput
import hashlib
from collections import defaultdict, deque

def solve(stretch):
    salt = 'jlmsuwbz'
    #salt = 'abc'
    old = defaultdict(deque)
    A = []
    maxA = 0
    for i in range(10**11):
        if len(A) >= 64 and i > maxA + 1000:
            break
        h = salt + str(i)
        for j in range(stretch+1):
            m = hashlib.md5()
            m.update(h.encode('utf-8'))
            h = m.hexdigest()
        last, count = None, 0
        seen3 = False
        seen5 = False
        for c in h:
            if c != last:
                last = c
                count = 0
            count += 1
            if count == 3 and not seen3:
                seen3 = True
                old[last * 3].append(i)
            elif count == 5 and not seen5:
                seen5 = True
                d = old[last * 3]
                while len(d):
                    x = d.popleft()
                    if x == i:
                        d.append(x)
                        break
                    if not (i - 1000 <= x):
                        continue
                    if len(A) < 64 and x > maxA:
                        maxA = x
                    A.append(x)
    A.sort()
    return A[63]
print(solve(0))
print(solve(2016))
