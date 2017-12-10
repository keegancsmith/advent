#!/usr/bin/env python3

# This is a cleaned up version. The live version can be seen as an asciicast
# at https://asciinema.org/a/u8xdq1LjQHrITY1U2MvMqIlke


def reverse_range(li, a, size):
    for i in range(size // 2):
        x = (a + i) % len(li)
        y = (a + size - 1 - i) % len(li)
        li[x], li[y] = li[y], li[x]


def solveA(lengths):
    elements = list(range(256))
    idx = 0
    skip = 0
    for l in lengths:
        reverse_range(elements, idx, l)
        idx += l + skip
        skip += 1
    return elements[0] * elements[1]


def solveB(lengths):
    elements = list(range(256))
    idx = 0
    skip = 0
    for _ in range(64):
        for l in lengths:
            reverse_range(elements, idx, l)
            idx += l + skip
            skip += 1
    dense = []
    for i in range(0, 256, 16):
        c = 0
        for j in range(i, i + 16):
            c ^= elements[j]
        c = hex(c).split('x')[1]
        if len(c) == 1:
            c = '0' + c
        dense.append(c)
    return ''.join(dense)


lengths = [int(x) for x in next(open('input')).strip().split(',')]
print('A', solveA(lengths))

lengths = [ord(c) for c in next(open('input')).strip()] + [17, 31, 73, 47, 23]
print('B', solveB(lengths))
