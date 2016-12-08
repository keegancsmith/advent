#!/usr/bin/env python3

import fileinput

R = 6
C = 50
screen = [[False] * C for _ in range(R)]

def print_():
    print('\n'.join(''.join('#' if b else '.' for b in r) for r in screen))
    print()

def rect(A, B):
    for x in range(A):
        for y in range(B):
            screen[y][x] = True

def rotate_row(A, B):
    l = len(screen[A])
    row = [screen[A][(i - B) % l] for i in range(l)]
    screen[A] = row

def rotate_col(A, B):
    l = len(screen)
    col = [screen[(i - B) % l][A] for i in range(l)]
    for i, b in enumerate(col):
        screen[i][A] = b

for line in fileinput.input():
    parts = line.strip().split()
    if parts[0] == 'rect':
        A, B = map(int, parts[1].split('x'))
        rect(A, B)
    elif parts[1] == 'row':
        A = int(parts[2][2:])
        B = int(parts[-1])
        rotate_row(A, B)
    else:
        A = int(parts[2][2:])
        B = int(parts[-1])
        rotate_col(A, B)
    print(line.strip())
    print_()

print(sum(sum(1 if b else 0 for b in r) for r in screen))
