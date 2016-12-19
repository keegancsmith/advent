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
    lc = 0 if n.left  is None else n.left.count
    rc = 0 if n.right is None else n.right.count
    v = n.n
    if i < lc:
        v = remove(n.left, i)
    elif i >= n.count - rc:
        v = remove(n.right, i - (n.count - rc))
    n.count -= 1
    return v

def print_(n, li):
    lc = 0 if n.left is None else n.left.count
    rc = 0 if n.right is None else n.right.count
    if lc > 0:
        print_(n.left, li)
    if n.count > lc + rc:
        li.append(n.n)
    if rc > 0:
        print_(n.right, li)

N = 3004953
import sys
if len(sys.argv) > 1:
    N = int(sys.argv[1])
root = construct(1, N)
i = 0
while root.count > 1:
    j = (i + root.count // 2) % root.count
    li = []
    print_(root, li)
    assert root.count == len(li)
    v = remove(root, j)
    assert v == li[j]
    li = [('<' + x + '>') if idx == i else (('>' + x + '<') if idx == j else x) for idx, x in enumerate(map(str, li))]
    print(' '.join(s.center(4) for s in li))
    print(v)
    if j > i:
        i += 1
    i = i % root.count
print(remove(root, 0))
