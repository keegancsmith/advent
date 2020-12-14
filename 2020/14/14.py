#!/usr/bin/env python3

from collections import defaultdict

def solveA(prog):
    andmask, ormask = None, None
    mem = defaultdict(int)
    for op, arg in prog:
        if op == 'mask':
            andmask = int(arg.replace('X', '1'), 2)
            ormask = int(arg.replace('X', '0'), 2)
        else:
            addr = int(op[4:-1])
            mem[addr] = (int(arg) & andmask) | ormask
    return sum(mem.values())


def allvals(v, mask):
    vals = [v]
    for i, b in enumerate(reversed(mask)):
        if b == '0':
            continue
        elif b == '1':
            vals = [v | (1 << i) for v in vals]
        else:
            vals = (
                [v |  (1 << i) for v in vals] +
                [v & ~(1 << i) for v in vals]
            )
    return vals


def solveB(prog):
    mask = None
    mem = defaultdict(int)
    for op, arg in prog:
        if op == 'mask':
            mask = arg
        else:
            addr = int(op[4:-1])
            arg = int(arg)
            for v in allvals(addr, mask):
                mem[v] = arg
    return sum(mem.values())

prog = [l.strip().split(' = ') for l in open('input') if l.strip()]

print('A', solveA(prog))
print('B', solveB(prog))
