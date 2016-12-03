#!/usr/bin/env python3

import fileinput

part2 = True
if not part2:
    buttons = [
        '123',
        '456',
        '789',
    ]
    x, y = 1, 1
else:
    buttons = [
        '  1  ',
        ' 234 ',
        '56789',
        ' ABC ',
        '  D  ',
    ]
    x, y = 0, 2

delta = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}
code = []
for line in fileinput.input():
    for c in line.strip():
        dx, dy = delta[c]
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(buttons) and 0 <= nx < len(buttons[ny]) and buttons[ny][nx] != ' ':
            x, y = nx, ny
    code.append(buttons[y][x])
print(''.join(code))
