#!/usr/bin/env python3

masses = [int(x.strip()) for x in open('input').readlines()]

print('A', sum(m // 3 - 2 for m in masses))

b = 0
for m in masses:
    while True:
        m = m // 3 - 2
        if m <= 0:
            break
        b += m
print('B', b)
