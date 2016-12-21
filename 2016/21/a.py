#!/usr/bin/env python3

import fileinput
import itertools

def solve(li, lines):
    for line in lines:
        p = line.strip().split()
        if p[0] == 'swap':
            if p[1] == 'position':
                i, j = int(p[2]), int(p[-1])
            else:
                i, j = li.index(p[2]), li.index(p[-1])
            li[i], li[j] = li[j], li[i]
        elif p[0] == 'move':
            i, j = int(p[2]), int(p[-1])
            li.insert(j, li.pop(i))
        elif p[0] == 'reverse':
            i, j = int(p[2]), int(p[-1])
            li = li[:i] + list(reversed(li[i:j+1])) + li[j+1:]
        elif p[0] == 'rotate':
            if p[-2] == 'letter':
                i = li.index(p[-1])
                delta = 1 + i
                if i >= 4:
                    delta += 1
                delta *= -1
            else:
                delta = -int(p[-2]) if p[1] == 'right' else int(p[-2])
            li = [li[(i + delta) % len(li)] for i in range(len(li))]
        else:
            assert False, line
    return ''.join(li)

lines = list(fileinput.input())
print(solve(list('abcdefgh'), lines))
target = 'fbgdceah'
for candidate in itertools.permutations(list(target)):
    if solve(list(candidate), lines) == target:
        print(''.join(candidate))
        exit(0)
