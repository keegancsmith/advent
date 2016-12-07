#!/usr/bin/env python3

def abba(s):
    for a, b, c, d in zip(s, s[1:], s[2:], s[3:]):
        if a == d and b == c and a != b:
            return True
    return False

def parts(s):
    for x in s.split('['):
        if not ']' in x:
            yield (True, x)
            continue
        p = x.split(']')
        yield (False, p[0])
        if len(p) > 1 and p[1]:
            yield (True, p[1])

def valid(s):
    s1 = (p for b, p in parts(s) if b)
    s2 = (p for b, p in parts(s) if not b)
    return any(abba(p) for p in s1) and all(not abba(p) for p in s2)

import fileinput
ans = 0
for line in fileinput.input():
    line = line.strip()
    if valid(line):
        ans += 1
print(ans)
