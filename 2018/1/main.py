#!/usr/bin/env python3

lines = [l.strip() for l in open('input') if l.strip()]
nums = [int(x[1:]) * (-1 if x[0] == '-' else 1) for x in lines]

def solveA(nums):
    return sum(nums)

def solveB(nums):
    seen = set([0])
    f = 0
    while True:
        for d in nums:
            f += d
            if f in seen:
                return f
            seen.add(f)
            
print('A', solveA(nums))
print('B', solveB(nums))
