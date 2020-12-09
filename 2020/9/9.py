#!/usr/bin/env python3


def has2sum(nums, target):
    for j, v1 in enumerate(nums):
        if target in (v1 + v2 for v2 in nums[j + 1 :]):
            return True
    return False


def solveA(nums, preamble_len):
    for i, v in enumerate(nums[preamble_len:]):
        if not has2sum(nums[i : i + preamble_len], v):
            return v


def solveB(nums, target):
    low, high = 0, 1
    current = nums[0]
    while current != target:
        if current > target:
            current -= nums[low]
            low += 1
        else:
            current += nums[high]
            high += 1
    return min(nums[low:high]) + max(nums[low:high])


nums = [int(l) for l in open("input")]

a = solveA(nums, 25)
print("A", a)
print("B", solveB(nums, a))
