#!/usr/bin/env python3

from collections import defaultdict, deque
import fileinput
import hashlib

m = '''
#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |V#  
#########
'''.strip().splitlines()

code = 'qzthpkfp'
q = deque([(code, (1, 1))])
maxlen = 0
while q:
    path, (x, y) = q.popleft()
    h = hashlib.md5(path.encode('utf-8')).hexdigest()[:4]
    for hc, d, (dx, dy) in zip(h, 'UDLR', ((-1, 0), (1, 0), (0, -1), (0, 1))):
        if hc not in 'bcdef':
            continue
        if m[x + dx][y + dy] == '#':
            continue
        nx, ny = x + dx * 2, y + dy * 2
        if m[nx][ny] == 'V':
            if maxlen == 0:
                print((path + d)[len(code):])
            maxlen = len(path + d) - len(code)
            continue
        q.append((path + d, (nx, ny)))

print(maxlen)
