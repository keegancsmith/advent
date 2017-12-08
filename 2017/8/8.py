#!/usr/bin/env python3

from collections import defaultdict

# asciicast at https://asciinema.org/a/2HcC8SyK6W3j07YmuXWey2qYA

lines = [l.strip() for l in open('input').readlines() if l.strip()]

ansb = -1000
reg = defaultdict(int)
for line in lines:
    r, op, n, _, cond = line.split(' ', 4)
    n = int(n)
    if eval(cond, None, reg):
        if op == 'dec':
            n *= -1
        reg[r] += n
        ansb = max(ansb, max(reg.values()))

print('A', max(reg.values()))
print('B', ansb)
