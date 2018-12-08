#!/usr/bin/env python3

def parse_node(nums):
    n_child = nums[0]
    n_metadata = nums[1]
    nums = nums[2:]
    children = []
    for i in range(n_child):
        child, nums = parse_node(nums)
        children.append(child)
    metadata = nums[:n_metadata]
    nums = nums[n_metadata:]
    return (children, metadata), nums

def solveA(node):
    children, metadata = node
    return sum(metadata) + sum(solveA(n) for n in children)

def solveB(node):
    children, metadata = node
    if len(children) == 0:
        return sum(metadata)
    sums = [0] + [solveB(n) for n in children]
    ans = 0
    for i in metadata:
        if i < len(sums):
           ans += sums[i]
    return ans

nums = [int(x) for x in open('input').read().split()]
#nums = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()))

root, nums = parse_node(nums)
assert len(nums) == 0

print('A', solveA(root))
print('B', solveB(root))
