#!/usr/bin/env python3

import math
from collections import defaultdict

data = open('input').read()

size = 0
tiles = {}
for lines in data.split('\n\n'):
    lines = lines.split()
    num = int(lines[1].strip(':'))
    size = len(lines[2:])
    tile = set()
    for r, row in enumerate(lines[2:]):
        for c, v in enumerate(row):
            if v == '#':
                tile.add((r,c))
    tiles[num] = tuple(tile)

def flip_x(tile):
    return tuple((size - x - 1, y) for x, y in tile)

def flip_y(tile):
    return tuple((x, size - y - 1) for x, y in tile)

def rot(tile):
    return tuple((y, size - x - 1) for x, y in tile)

def orientations(tile):
    tiles = set()
    ops = [flip_x, flip_y, flip_y, flip_x, flip_y, flip_x, flip_x, flip_y]
    for i in range(4):
        for op in ops:
            tile = op(tile)
            if tile not in tiles:
                yield tile
                tiles.add(tile)
        tile = rot(tile)

def print_tile(*tiles):
    for y in range(size):
        rows = []
        for tile in tiles:
            rows.append(''.join('#' if (x, y) in tile else '.' for x in range(size)))
        print(' '.join(rows))

next_x = defaultdict(set)
next_y = defaultdict(set)
for k, tile in tiles.items():
    for tile in orientations(tile):
        next_x[tuple(sorted(p for p in tile if p[0] == 0))].add((k, tile))
        next_y[tuple(sorted(p for p in tile if p[1] == 0))].add((k, tile))

total_size = int(math.sqrt(len(tiles)))
assert max(len(s) for s in next_x.values()) == 2
assert max(len(s) for s in next_y.values()) == 2
        
def adjacent(k, tile, dimension):
    if dimension == 0:
        next_k = tuple(sorted((0, y) for x, y in tile if x == size - 1))
        next_d = next_x
    else:
        next_k = tuple(sorted((x, 0) for x, y in tile if y == size - 1))
        next_d = next_y
    if next_k not in next_d:
        return None, None
    for k2, tile in next_d[next_k]:
        if k != k2:
            return k2, tile
    return None, None       

def valid_orientation(k, tile):
    corners = []
    image = []
    for i in range(total_size):
        if image:
            k, tile = image[-1][0]
            k, tile = adjacent(k, tile, 1)
            if k is None:
                #print("no down adj")
                return None
        cur = [(k, tile)]
        for j in range(1, total_size):
            k, tile = adjacent(k, tile, 0)
            if k is None:
                #print("no left adj")
                return None
            cur.append((k, tile))
            if image:
                k2, tile2 = image[-1][j]
                k2, _ = adjacent(k2, tile2, 1)
                if k2 != k:
                    #print("mismatch down adj")
                    return None
        image.append(cur)
        #print()
        #print_tile(*(t for k, t in cur))
        if i in (0, total_size - 1):
            corners.append(cur[0][0])
            corners.append(cur[-1][0])
    ans = 1
    for c in corners:
        ans *= c
    return ans, [[t for _, t in row] for row in image]

def valid(k):
    for tile in orientations(tiles[k]):
        ans = valid_orientation(k, tile)
        if ans is not None:
            return ans

for k in tiles:
    ans = valid(k)
    if ans is not None:
        print('A', ans[0])
        image = ans[1]
        break

image_rows = []
for tiles in image:
    for y in range(size-2):
        rows = []
        for tile in tiles:
            rows.append(''.join('#' if (x+1, y+1) in tile else '.' for x in range(size-2)))
        row = ''.join(rows)
        image_rows.append(row)
size = len(row)
assert len(row) == len(image_rows)


active = set()
for y, row in enumerate(image_rows):
    for x, v in enumerate(row):
        if v == '#':
            active.add((x, y))


monster = (
    (0, 0),
    (1, 1),
    (4, 1),
    (5, 0),
    (6, 0),
    (7, 1),
    (10, 1),
    (11, 0),
    (12, 0),
    (13, 1),
    (16, 1),
    (17, 0),
    (18, -1),
    (18, 0),
    (19, 0),
)

for tile in orientations(active):
    active = set(tile)
    rough = set(tile)
    for x, y in active:
        m = set((x + dx, y + dy) for dx, dy in monster)
        if m < active:
            for p in m:
                rough.discard(p)
    if len(rough) != len(active):
        print("B", len(rough))
