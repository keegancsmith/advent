#!/usr/bin/env python3

from collections import defaultdict, deque, namedtuple

# Solution is janky, I just ran and submitted an answer once the output looked
# stable. I also was stupid and misread problem two, and could of submitted
# much earlier. https://asciinema.org/a/3YfLTtl5meIMuaOwzgDyM9vAr

lines = [l.strip().split() for l in open('input') if l.strip()]
particles = {}
for i, l in enumerate(lines):
    p = tuple(map(int, l[0][3:-2].split(',')))
    v = tuple(map(int, l[1][3:-2].split(',')))
    a = tuple(map(int, l[2][3:-1].split(',')))
    particles[i] = (p, v, a)

def solve(particles, remove_collisions):
    for j in range(1000):
        closest = None
        closest_d = None
        seen = set()
        seen_twice = set()
        for i, (p, v, a) in particles.items():
            v = tuple(x + y for x, y in zip(v, a))
            p = tuple(x + y for x, y in zip(p, v))
            if remove_collisions:
                if p in seen:
                    seen_twice.add(p)
                else:
                    seen.add(p)
            particles[i] = (p, v, a)
            d = sum(map(abs, p))
            if closest is None or d < closest_d:
                closest_d = d
                closest = i
        if seen_twice:
            particles = dict((i, (p, v, a)) for i, (p, v, a) in particles.items() if p not in seen_twice)

    if remove_collisions:
        return len(particles)
    else:
        return closest
    
print('A', solve(dict(particles), False))
print('B', solve(dict(particles), True))
