#!/usr/bin/env python3

f = open('input').read()
world = {}
carts = []
for x, line in enumerate(f.splitlines()):
    for y, v in enumerate(line):
        c = v
        if v == '^':
            c = '|'
            carts.append(((x, y), (-1, 0), 0))
        elif v in 'v':
            c = '|'
            carts.append(((x, y), (1, 0), 0))
        elif v == '<':
            c = '-'
            carts.append(((x, y), (0, -1), 0))
        elif v == '>':
            c = '-'
            carts.append(((x, y), (0, 1), 0))
        world[(x, y)] = c

next_state_left = {
    (-1, 0): ( 0, -1),
    (1, 0) :  ( 0, 1),
    (0, 1) :  (-1, 0),
    (0, -1): ( 1, 0,)
}
next_state_right = {v: k for k, v in next_state_left.items()}
        
def step(world, carts):
    carts.sort()
    pos = {c[0]: i for i, c in enumerate(carts)}
    for i, cart in enumerate(carts):
        if cart is None:
            continue
        
        (x, y), (dx, dy), intersection_state = cart
        del pos[(x, y)]
        x, y = x + dx, y + dy
        v = world.get((x, y))
        if v == '+':
            if intersection_state == 0:
                dx, dy = next_state_left[(dx, dy)]
            elif intersection_state == 2:
                dx, dy = next_state_right[(dx, dy)]
            intersection_state = (intersection_state + 1) % 3
        elif v == '/':
            dx, dy = -dy, -dx
        elif v == '\\':
            dx, dy = dy, dx

        if (x, y) in pos:
            carts[i] = None
            carts[pos[(x, y)]] = None
            del pos[(x, y)]
            print("%d,%d" % (y, x))
        else:
            pos[(x, y)] = i
            carts[i] = ((x, y), (dx, dy), intersection_state)
    return [c for c in carts if c is not None]

print()
for j in range(100000):
    carts = step(world, carts)
    if len(carts) <= 1:
        break
if carts:
    x, y = carts[0][0]
    print("%d,%d" % (y, x))
