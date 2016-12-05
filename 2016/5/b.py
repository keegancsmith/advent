#!/usr/bin/env python3

import fileinput
import md5

x = 'wtnhxymk'
m = md5.new(x)
ans = {}
i = 0
while len(ans) < 8:
    hs = m.copy()
    hs.update(str(i))
    h = hs.hexdigest()
    i += 1
    if h[:5] == '00000':
        try:
            p = int(h[5])
            if p not in ans and p < 8:
                ans[p] = h[6]
                print(ans)
        except:
            pass
        print(h)
print(''.join(str(ans[i]) for i in range(8)))
