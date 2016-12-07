#!/usr/bin/env python3

def aba(s):
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == c and a != b:
            yield a + b

def bab(s, abas):
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == c and a != b and (b + a) in abas:
            return True
            
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
    abas = set()
    for b, p in parts(s):
        if not b:
            continue
        abas.update(set(aba(p)))
    return any(bab(p, abas) for b, p in parts(s) if not b)

import fileinput
ans = 0
for line in fileinput.input():
    line = line.strip()
    if valid(line):
        ans += 1
print(ans)
