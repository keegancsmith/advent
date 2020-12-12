#!/usr/bin/env python3

def solveA(lines):
    x, y = 0, 0
    dx, dy = 1, 0
    for line in lines:
        ins = line[0]
        val = int(line[1:])
        if ins == 'F':
            x += dx * val
            y += dy * val
        elif ins == 'N':
            y += val
        elif ins == 'S':
            y -= val
        elif ins == 'E':
            x += val
        elif ins == 'W':
            x -= val
        elif ins == 'R':
            while val > 0:
                val -= 90
                dx, dy = dy, -dx
        elif ins == 'L':
            while val > 0:
                val -= 90
                dx, dy = -dy, dx
        else:
            assert False, line
    return abs(x) + abs(y)

def solveB(lines):
    x, y = 0, 0
    dx, dy = 10, 1
    for line in lines:
        ins = line[0]
        val = int(line[1:])
        if ins == 'F':
            x += dx * val
            y += dy * val
        elif ins == 'N':
            dy += val
        elif ins == 'S':
            dy -= val
        elif ins == 'E':
            dx += val
        elif ins == 'W':
            dx -= val
        elif ins == 'R':
            while val > 0:
                val -= 90
                dx, dy = dy, -dx
        elif ins == 'L':
            while val > 0:
                val -= 90
                dx, dy  = -dy, dx
        else:
            assert False, line
    return abs(x) + abs(y)

data = open('input').read()
lines = [l.strip().split() for l in data.splitlines() if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if all(len(l) == 1 for l in lines):
    lines = [l[0] for l in lines]

print('A', solveA(lines))
print('B', solveB(lines))
