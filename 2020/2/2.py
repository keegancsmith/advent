#!/usr/bin/env python3

def solveA(lines):
    return sum(1 if a <= word.count(c) <= b else 0 for (a, b), c, word in lines)

def solveB(lines):
    ans = 0
    for (a, b), c, word in lines:
        a -= 1
        b -= 1
        if (word[a] == c and word[b] != c) or (word[a] != c and word[b] == c):
            ans += 1
    return ans

lines = [l.strip().split() for l in open('input') if l.strip()]
lines = [(tuple(map(int, l[0].split('-'))), l[1][0], l[2]) for l in lines]

print('A', solveA(lines))
print('B', solveB(lines))
