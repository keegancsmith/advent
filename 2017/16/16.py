#!/usr/bin/env python3

# Came 42nd today. This is a cleaned up version. Asciicast at
# https://asciinema.org/a/VLfUUMOe93Ok4wuPwX4tJBXlF

def dance(p, moves):
    for m in moves:
        if m[0] == 's':
            n = int(m[1:])
            p = p[-n:] + p[:-n]
        elif m[0] == 'x':
            n, m = map(int, m[1:].split('/'))
            p[n], p[m] = p[m], p[n]
        elif m[0] == 'p':
            n, m = p.index(m[1]), p.index(m[-1])
            p[n], p[m] = p[m], p[n]
    return p

def solveB(p, moves):
    seen = {}
    target = 1000000000
    for i in range(target):
        x = ''.join(p)
        if x in seen:
            cycle_size = i - seen[x]
            break
        seen[x] = i
        p = dance(p, moves)

    target = (target - i) % cycle_size
    for i in range(target):
        p = dance(p, moves)
    return ''.join(p)

moves = next(open('input')).strip().split(',')
p = list('abcdefghijklmnop')
print('A', ''.join(dance(p, moves)))
print('B', solveB(p, moves))
