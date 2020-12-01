#!/usr/bin/env python3

def findSum(nums, target):
    front, back = 0, len(nums) - 1
    while front < back:
        a, b = nums[front], nums[back]
        if a + b > target:
            back -= 1
        elif a + b < target:
            front += 1
        else:
            return a * b
    return None

def solveA(nums):
    nums.sort()
    return findSum(nums, 2020)

def solveB(nums):
    nums.sort()
    for i, a in enumerate(nums):
        bc = findSum(nums[i+1:], 2020 - a)
        if bc:
            return a * bc

nums = [int(l.strip()) for l in open('input') if l.strip()]

print('A', solveA(nums))
print('B', solveB(nums))
