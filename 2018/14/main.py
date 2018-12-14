#!/usr/bin/env python

def solveA(n):
    score = [3, 7]
    i1, i2 = 0, 1
    while len(score) < n + 10:
        for c in str(score[i1] + score[i2]):
            score.append(ord(c) - ord('0'))
        i1 = (i1 + score[i1] + 1) % len(score)
        i2 = (i2 + score[i2] + 1) % len(score)
    return ''.join(map(str, score[n:n+10]))

def solveB(n):
    score = [3, 7]
    i1, i2 = 0, 1
    i = 0
    o = 0
    while True:
        i += 1
        if i % 10000 == 0:
            x = ''.join(map(str, score[o:]))
            idx = x.find(n)
            if idx != -1:
                return idx + o
            o = len(score) - len(n)
        for c in str(score[i1] + score[i2]):
            score.append(ord(c) - ord('0'))
        i1 = (i1 + score[i1] + 1) % len(score)
        i2 = (i2 + score[i2] + 1) % len(score)

print()
assert(solveA(9) == '5158916779')
assert(solveA(5) == '0124515891')
assert(solveA(18) == '9251071085')
assert(solveA(2018) == '5941429882')
print('A:', solveA(793031))

assert(solveB('51589') == 9)
assert(solveB('01245') == 5)
assert(solveB('92510') == 18)
assert(solveB('59414') == 2018)
print('B:', solveB('793031'))
