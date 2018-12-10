#!/usr/bin/env python3

from collections import defaultdict, deque

def simulate(n_players, last_marble):
    marbles = deque([0])
    score = defaultdict(int)
    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            marbles.rotate(7)
            p = i % n_players
            score[p] += i + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)
    return max(score.values())
    
assert simulate(9, 25) == 32
assert simulate(10, 1618) == 8317
assert simulate(13, 7999) == 146373
assert simulate(17, 1104) == 2764
assert simulate(21, 6111) == 54718
assert simulate(30, 5807) == 37305

print("A: ", simulate(425, 70848))
print("B: ", simulate(425, 100*70848))
