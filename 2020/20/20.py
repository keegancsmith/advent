#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

data = '''
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
'''
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
    last = None
    for i in range(total_size):
        if last is not None:
            k, tile = last[0]
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
            if last is not None:
                k2, _ = adjacent(last[j][0], last[j][1], 1)
                if k2 != k:
                    #print("mismatch down adj")
                    return None
        last = cur
        #print()
        #print_tile(*(t for k, t in cur))
        if i in (0, total_size - 1):
            corners.append(cur[0][0])
            corners.append(cur[-1][0])
    ans = 1
    for c in corners:
        ans *= c
    return ans

def valid(k):
    for tile in orientations(tiles[k]):
        ans = valid_orientation(k, tile)
        if ans is not None:
            return ans

for k in tiles:
    ans = valid(k)
    if ans is not None:
        print(ans)
        break

