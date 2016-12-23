#!/usr/bin/env python3

from collections import defaultdict
import fileinput

R = defaultdict(int)
R['a'] = 7

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
    print(ip, P[ip])
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
    elif act == 'tgl':
        i = ip + val(p[1])
        if not (0 <= i < len(P)):
            ip += 1
            continue
        p = P[i]
        act = p[0]
        if act == 'inc':
            act = 'dec'
        elif len(p) == 2:
            act = 'inc'
        elif act == 'jnz':
            act = 'cpy'
        elif len(p) == 3:
            act = 'jnz'
        else:
            assert False
        P[i][0] = act
    else:
        assert False
    ip += 1

print(val('a'))
