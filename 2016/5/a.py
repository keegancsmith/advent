#!/usr/bin/env python3

import fileinput
import md5

x = 'wtnhxymk'
m = md5.new(x)
ans = []
i = 0
while len(ans) < 8:
    hs = m.copy()
    hs.update(str(i))
    h = hs.hexdigest()
    i += 1
    if h[:5] == '00000':
        ans.append(h[5])
        print(h)
print(''.join(ans))
