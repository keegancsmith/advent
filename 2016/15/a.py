#!/usr/bin/env python3

from collections import defaultdict
import fileinput

def solve():
    A = (
        (17, 1),
        (7 , 0),
        (19, 2),
        (5 , 0),
        (3 , 0),
        (13, 5),
        # Part B
        (11, 0),
    )
    
    #A = ((5,4), (2, 1))
    for x in range(1, 10**10):
        if all((s + i + x) % m == 0 for i, (m, s) in enumerate(A)):
            return x - 1
        
print(solve())
