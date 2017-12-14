#!/usr/bin/env python3

from collections import deque

# this is a cleaned up version. I had NFC what was going on in this
# problem. The description was not the usual quality. Live version at
# https://asciinema.org/a/6GseuREQNerXwnLfcVge5d3OH

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


def knot_hash(s):
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
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


key = 'jzgqcdpd'
#key = 'flqrgnkx'
grid = []
for i in range(128):
    s = key + '-' + str(i)
    h = knot_hash(s)
    row = ''.join(bin(int(x, 16))[2:].zfill(4) for x in h)
    grid.append(row)


seen = set()
def bfs(r, c):
    if (r, c) in seen:
        return 0
    if grid[r][c] == '0':
        return 0
    seen.add((r, c))
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < 128 and 0 <= nc < 128):
                continue
            if (nr, nc) in seen:
                continue
            if grid[nr][nc] == '0':
                continue
            seen.add((nr, nc))
            q.append((nr, nc))
    return 1

print('A', sum(map(int, ''.join(grid))))
print('B', sum(bfs(r, c) for r in range(128) for c in range(128)))

