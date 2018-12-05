#!/usr/bin/env python3

x = open('input').read().strip()
def solve(x):
    while True:
        n = len(x)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            x = x.replace(c + c.upper(), '')
            x = x.replace(c.upper() + c, '')
        if len(x) == n:
            break
    return len(x)

print('A:', solve(x))
ans = len(x)
for c in 'abcdefghijklmnopqrstuvwxyz':
    y = x.replace(c, '')
    y = y.replace(c.upper(), '')
    ans = min(ans, solve(y))
print('B:', ans)
