#!/usr/bin/env python3

from collections import defaultdict
import fileinput

R = defaultdict(int)
# Comment for part a
R['c'] = 1

def val(x):
    try:
        return int(x)
    except:
        return R[x]

P = []
for line in fileinput.input():
    P.append(line.split())

ip = 0
while 0 <= ip < len(P):
    p = P[ip]
    #print(ip, p, R)
    act = p[0]
    if act == 'cpy':
        R[p[2]] = val(p[1])
    elif act == 'inc':
        R[p[1]] += 1
    elif act == 'dec':
        R[p[1]] -= 1
    elif act == 'jnz':
        if val(p[1]) != 0:
            ip += val(p[2])
            continue
    ip += 1

print(val('a'))
