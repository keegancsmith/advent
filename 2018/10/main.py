#!/usr/bin/env python3

def slurpNums(s):
    import re
    return list(map(int, re.findall('-?[0-9]+', s)))

def step(points):
    return [(x + dx, y + dy, dx, dy) for x, y, dx, dy in points]

f = '''position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>'''
f = open('input').read()

nums = slurpNums(f)
points = list(zip(nums[0::4], nums[1::4], nums[2::4], nums[3::4]))
area = 100**10
i = -1
while True:
    old = points
    points = step(points)
    i += 1
    bounds = (min(p[0] for p in points),
              max(p[0] for p in points),
              min(p[1] for p in points),
              max(p[1] for p in points))
    a = (bounds[1] - bounds[0] + 1) * (bounds[3] - bounds[2] + 1)
    if a > area:
        points = old
        break
    area = a

bounds = (min(p[0] for p in points),
          max(p[0] for p in points),
          min(p[1] for p in points),
          max(p[1] for p in points))
print("found in %d seconds" % i)
rows = [['.'] * (bounds[1] - bounds[0] + 1) for _ in range(bounds[3] - bounds[2] + 1)]
for x, y, _, _ in points:
    rows[y - bounds[2]][x - bounds[0]] = '#'
print()
print('\n'.join(''.join(r) for r in rows))
