#!/usr/bin/env python3

import fileinput
ans = 0
la, lb, lc = [], [], []
for line in fileinput.input():
    a, b, c = map(int, line.strip().split())
    la.append(a)
    lb.append(b)
    lc.append(c)
x = la + lb + lc
for a, b, c in zip(x[::3], x[1::3], x[2::3]):
    if not ((a + b <= c) or (a + c <= b) or (b + c <= a)):
        ans += 1
print(ans)
