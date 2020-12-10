#!/usr/bin/env python3

def solveA(adapters):
    diffs = [y - x for x, y in zip(adapters, adapters[1:])]
    return diffs.count(1) * diffs.count(3)

def solveB(adapters):
   dp = [1]
   for i in range(1, len(adapters)):
       a = 0
       x = adapters[i]
       for j in range(max(0, i-3), i):
           if x - adapters[j] <= 3:
               a += dp[j]
       dp.append(a)
   return dp[-1]

adapters = sorted(int(l) for l in open('input'))
adapters = [0] + adapters + [adapters[-1] + 3]

print('A', solveA(adapters))
print('B', solveB(adapters))
