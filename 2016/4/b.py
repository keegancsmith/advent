#!/usr/bin/env python3

def getname(x):
    last = x[:-1].split('-')[-1]
    sector, got = last.split('[')
    sector = int(sector)
    parts = x.split('-')[:-1]
    name = []
    for p in parts:
        name.append(''.join(chr(((ord(c) - ord('a')) + sector) % 26 + ord('a')) for c in p))
    return ' '.join(name)
    
import fileinput
ans = 0
for line in fileinput.input():
    print(line.strip(), getname(line.strip()))
print(ans)
