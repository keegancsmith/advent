#!/usr/bin/env python3

from collections import defaultdict
import math

# I took so long so didn't bother uploading a livecast. The trick to this
# problem is to actually convert the assembly into python and simplify. I
# spent a lot of time micro-optimizing certain bits. However, if I just tried
# to understand the whole program it would of been much faster to solve.

def is_prime(b):
    if b % 2 == 0 and b > 2:
        return False
    for d in range(3, int(math.sqrt(b)) + 1, 2):
        if b % d == 0:
            return False
    return True

def program(code, a):
    count = defaultdict(int)
    registers = defaultdict(int)
    registers['a'] = a
    def val(r):
        try:
            return int(r)
        except:
            return registers[r]
    i = 0
    while 0 <= i < len(code):
        if i == 8 and a == 1:
            # Part B is a primality checker
            registers['f'] = 1 if is_prime(val('b')) else 0
            i = 24
        x = code[i]
        count[x[0]] += 1
        if x[0] == 'set':
            registers[x[1]] = val(x[2])
        elif x[0] == 'mul':
            registers[x[1]] *= val(x[2])
        elif x[0] == 'jnz':
            if val(x[1]) != 0:
                i += val(x[2])
                continue
        elif x[0] == 'sub':
            registers[x[1]] -= val(x[2])            
        else:
            assert False, x
        i += 1
    return count, registers


def solveA(code):
    count, registers = program(code, a=0)
    return count['mul']

def solveB(code):
    count, registers = program(code, a=1)
    return registers['h']

code = [l.strip().split() for l in open('input') if l.strip()]
print('A', solveA(code))
print('B', solveB(code))
