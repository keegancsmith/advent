#!/usr/bin/env python3

# From https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
# I need to relearn this stuff.
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def solveA(start, buses):
    wait, bus = min((abs(start % (-b)), b) for _, b in buses)
    return wait * bus

def solveB(buses):
    n = []
    a = []
    for i, bus in buses:
        n.append(bus)
        a.append(bus - i)
    return chinese_remainder(n, a)

data = open('input').read()
lines = [l.strip().split(',') for l in data.splitlines() if l.strip()]
start = int(lines[0][0])
buses = [(i, int(b)) for i, b in enumerate(lines[1]) if b != 'x']

print('A', solveA(start, buses))
print('B', solveB(buses))
