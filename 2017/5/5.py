#!/usr/bin/env python3

# Live version at https://asciinema.org/a/LZDpNJkll4YDXNoV2KWXxavEH
# Note: This has been cleaned up from the live version

ins = [int(l.strip()) for l in open('input').readlines() if l.strip()]

def solveA(ins):
    pos = 0
    steps = 0
    while pos >= 0 and pos < len(ins):
        old = pos
        pos += ins[pos]
        ins[old] += 1
        steps += 1
    return steps

def solveB(ins):
    pos = 0
    steps = 0
    while pos >= 0 and pos < len(ins):
        old = pos
        pos += ins[pos]
        if ins[old] >= 3:
            ins[old] -= 1
        else:
            ins[old] += 1
        steps += 1
    return steps

print('A', solveA(ins[:]))
print('B', solveB(ins[:]))
