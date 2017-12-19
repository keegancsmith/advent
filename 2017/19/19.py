#!/usr/bin/env python3

# Slow day for me :'( Cast at
# https://asciinema.org/a/OswdxPXo2ufnt1kmwAUGRyDvj

lines = list(open('input'))

def at(r, c):
    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
        return lines[r][c] if lines[r][c] != ' ' else ''
    return ''

r, c = 0, lines[0].index('|')
dr, dc = 1, 0
path = []
steps = 0
while True:
    steps += 1
    if at(r, c) not in '|+-':
        path.append(at(r, c))
    if at(r + dr, c + dc):
        r, c = r + dr, c + dc
        continue

    # Change direction
    if dr == 0:
        n = ((r + 1, c), (r - 1, c))
    else:
        n = ((r, c + 1), (r, c - 1))
    n = [p for p in n if at(*p)]
    assert len(n) <= 1
    if not n:
        break
    dr, dc = n[0][0] - r, n[0][1] - c
    r, c = n[0]    

print(''.join(path))
print(steps)
