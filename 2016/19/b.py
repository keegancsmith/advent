#!/usr/bin/env python3

from collections import defaultdict, deque
import fileinput
import hashlib

class node(object):
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None
        self.count = 1

def construct(l, r):
    m = (l + r) // 2
    n = node(m)
    if l < m:
        n.left = construct(l, m - 1)
        n.count += n.left.count
    if m < r:
        n.right = construct(m + 1, r)
        n.count += n.right.count
    return n

def remove(n, i):
    assert 0 <= i < n.count
    lc = 0
    rc = 0
    if n.left != None:
        lc = n.left.count
    if n.right != None:
        rc = n.right.count
    v = n.n
    if i < lc:
        v = remove(n.left, i)
    elif i >= n.count - rc:
        v = remove(n.right, i - (n.count - rc))
    n.count -= 1
    return v

N = 3004953
#N = 5
root = construct(1, N)
i = 0
while root.count > 1:
    j = (i + root.count // 2) % root.count
    v = remove(root, j)
    #print(v)
    if j > i:
        i = (i + 1) % root.count
print(remove(root, 0))
