#!/usr/bin/env python3

# This is a cleaned up version. Asciicast at
# https://asciinema.org/a/S9RizZCL736qui0ey2Zn9sHZU

def solveA():
    A=16807
    B=48271
    a=873
    b=583
    count = 0
    mask = (1 << 16) - 1
    for i in range(40000000):
        a = (a * A) % 2147483647
        b = (b * B) % 2147483647
        if (a & mask) == (b & mask):
            count += 1
    return(count)
  
def solveB():
    A=16807
    B=48271
    a=873
    b=583
    count = 0
    mask = (1 << 16) - 1
    for i in range(5000000):
        a = (a * A) % 2147483647
        while a % 4 != 0:
            a = (a * A) % 2147483647
        b = (b * B) % 2147483647
        while b % 8 != 0:
            b = (b * B) % 2147483647
        if (a & mask) == (b & mask):
            count += 1
    return(count)
  
print()
print(solveA())
print(solveB())
