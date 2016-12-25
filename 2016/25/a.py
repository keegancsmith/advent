#!/usr/bin/env python3

from collections import defaultdict
import fileinput

P = []
for line in fileinput.input():
    P.append(line.split())

def solve(initial):
    R = defaultdict(int)
    R['a'] = initial
    
    def val(x):
        try:
            return int(x)
        except:
            return R[x]

    numtimes = 0
    expect = 0
    ip = 0
    while 0 <= ip < len(P):
        #print(ip, P[ip])
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
        elif act == 'out':
            if val(p[1]) != expect:
                return False
            expect = (expect + 1) % 2
            numtimes += 1
            if numtimes == 1000:
                return True
        else:
            assert False
        ip += 1

for i in range(10000):
    x = solve(i)
    print(i, x)
    if x:
        break
