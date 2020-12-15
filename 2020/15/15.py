#!/usr/bin/env python3

from collections import defaultdict


def solveA(nums, turns=2020):
    spoken_turns = defaultdict(list)
    last_spoken = None
    for turn, n in enumerate(nums):
        spoken_turns[n].append(turn + 1)
        last_spoken = n

    for turn in range(len(nums) + 1, turns + 1):
        if len(spoken_turns[last_spoken]) == 1:
            speak = 0
        else:
            speak = spoken_turns[last_spoken][-1] - spoken_turns[last_spoken][-2]
        spoken_turns[speak].append(turn)
        last_spoken = speak
    return speak


def solveB(nums):
    return solveA(nums, 30000000)


assert solveA([1, 3, 2]) == 1
assert solveA([1, 3, 2]) == 1
assert solveA([2, 1, 3]) == 10
assert solveA([1, 2, 3]) == 27
assert solveA([2, 3, 1]) == 78
assert solveA([0, 3, 6]) == 436
assert solveA([3, 2, 1]) == 438
assert solveA([3, 1, 2]) == 1836

data = open("input").read()
nums = [int(x.strip()) for x in data.split(",")]

print("A", solveA(nums))
print("B", solveB(nums))
