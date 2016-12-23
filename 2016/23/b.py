#!/usr/bin/env python3

from collections import defaultdict
import fileinput

R = defaultdict(int)
# Part A
R['a'] = 7
# Part B
R['a'] = 12

def val(x):
    try:
        return int(x)
    except:
        return R[x]

P = []
for line in fileinput.input():
    P.append(line.split())

ip = 0
n = 0
b = 0
while 0 <= ip < len(P):
    #print(ip, P[ip], ' '.join('%s=%d' % x for x in sorted(R.items()) if x[0] in 'abcd'))
    if b != R['b']:
        b = R['b']
        print(b)
        #print(n)
        print(' '.join('%s=%d' % x for x in sorted(R.items()) if x[0] in 'abcd'))
        print('\n'.join(' '.join(x) for x in P))
        print()
        if b == 7 and False:
            exit(0)
    n += 1
    p = P[ip]
    act = p[0]
    if act == 'cpy':
        R[p[2]] = val(p[1])
    elif act == 'inc':
        R[p[1]] += 1
    elif act == 'dec':
        R[p[1]] -= 1
    elif act == 'jnz':
        if p[2] == '-2' and P[ip-2][0] == 'inc' and P[ip-1][0] == 'dec' and P[ip-1][1] == p[1]:
            R[P[ip-2][1]] = R[P[ip-2][1]] + R[p[1]]
            R[p[1]] = 0
        if p[2] == '-5' and P[ip-5][0] == 'cpy' and P[ip-4][0] == 'inc' and P[ip-3][0] == 'dec' and P[ip-2][0] == 'jnz' and P[ip-1][0] == 'dec' and p[1] == 'd':
            # We assume registers make sense for our input
            #print(' '.join('%s=%d' % x for x in sorted(R.items()) if x[0] in 'abcd'))
            R['a'] = (R['d'] + 1) * R['b']
            R['c'] = 0
            R['d'] = 0
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
