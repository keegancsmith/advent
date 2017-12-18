#!/usr/bin/env python3

from collections import defaultdict, deque

# This is a cleaned up version. Live cast at
# https://asciinema.org/a/PlDz6Y0UsdkVZ99pQWKR1eYjI

def program(code, p, rcv):
    registers = defaultdict(int)
    registers['p'] = p
    def val(r):
        try:
            return int(r)
        except:
            return registers[r]
    i = 0
    while 0 <= i < len(code):
        x = code[i]
        if x[0] == 'snd':
            yield ('snd', val(x[1]))
        elif x[0] == 'set':
            registers[x[1]] = val(x[2])
        elif x[0] == 'add':
            registers[x[1]] += val(x[2])
        elif x[0] == 'mul':
            registers[x[1]] *= val(x[2])
        elif x[0] == 'mod':
            registers[x[1]] = val(x[1]) % val(x[2])
        elif x[0] == 'rcv':
            yield ('rcv', val(x[1]))
            registers[x[1]] = rcv()
        elif x[0] == 'jgz':
            if val(x[1]) > 0:
                i += val(x[2])
                continue
        i += 1

def solveA(code):
    sound = None
    p = program(code, 0, lambda: 0)
    while True:
        ins, v = next(p)
        if ins == 'snd':
            sound = v
        elif ins == 'rcv':
            if v != 0:
                return sound

def solveB(code):
    q = [deque([]), deque([])]
    p = [program(code, 0, lambda: q[0].popleft()),
         program(code, 1, lambda: q[1].popleft())]
    s = [None, None]
    n = 0
    ans = 0
    while True:
        ins, v = next(p[n])
        if ins == 'snd':
            q[(n + 1) % 2].append(v)
            if n == 1:
                ans += 1
        elif ins == 'rcv':
            if len(q[n]) > 0:
                continue
            s[n] = 'WAIT'
            if all(x == 'WAIT' for x in s) and sum(len(x) for x in q) == 0:
                return ans
            n = (n + 1) % 2

code = [l.strip().split() for l in open('input') if l.strip()]
print('A', solveA(code))
print('B', solveB(code))
