#!/usr/bin/env python3

def num_trees(slopes, dx, dy):
    x, y = dx, dy
    ans = 0
    while x < len(slopes):
        if slopes[x][y] == '#':
            ans += 1
        x, y = x + dx, (y + dy) % len(slopes[x])
    return ans

def solveA(lines):
    return num_trees(lines, 1, 3)

def solveB(lines):
    return (num_trees(lines, 1, 1) *
            num_trees(lines, 1, 3) *
            num_trees(lines, 1, 5) *
            num_trees(lines, 1, 7) *
            num_trees(lines, 2, 1))

lines = [l.strip() for l in open('input')]
print('A', solveA(lines))
print('B', solveB(lines))
