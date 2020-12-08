#!/usr/bin/env python3


def run(prog):
    acc = 0
    off = 0
    seen = set()
    while off not in seen and off < len(prog):
        seen.add(off)
        ins, arg = prog[off]
        if ins == 'acc':
            acc += arg
            off += 1
        elif ins == 'jmp':
            off += arg
        elif ins == 'nop':
            off += 1
        else:
            assert False
    return acc, off


def solveA(prog):
    acc, off = run(prog)
    return acc


def solveB(prog):
    for i, (ins, arg) in enumerate(prog):
        if ins == 'jmp':
            ins = 'nop'
        elif ins == 'nop':
            ins = 'jmp'
        else:
            continue
        fixed = prog[:i] + [(ins, arg)] + prog[i + 1 :]
        acc, off = run(fixed)
        if off == len(prog):
            return acc


lines = [l.strip().split() for l in open('input') if l.strip()]
prog = [(l[0], int(l[1])) for l in lines]

print('A', solveA(prog))
print('B', solveB(prog))
