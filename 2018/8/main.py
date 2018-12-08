#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

def parse_node(nums):
    n_child = nums[0]
    n_metadata = nums[1]
    nums = nums[2:]
    metadata_sum = 0
    for i in range(n_child):
        ms, nums = parse_node(nums)
        metadata_sum += ms
    for i in range(n_metadata):
        metadata_sum += nums[0]
        nums = nums[1:]
    return metadata_sum, nums

def solveA(lines):
    nums = lines
    metadata_sum = 0
    while nums:
        ms, nums = parse_node(nums)
        metadata_sum += ms
    return metadata_sum

def solveB(lines):
    pass

lines = [l.strip().split() for l in open('input') if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass
if all(len(l) == 1 for l in lines):
    lines = [l[0] for l in lines]

#lines = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()))
    
print('A', solveA(lines[0]))
print('B', solveB(lines[0]))
