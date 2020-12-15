#!/usr/bin/env python3

def solveA(nums, turns=2020):
    last_turn = {}
    last_spoken = None
    for turn, n in enumerate(nums):
        last_turn[n] = turn + 1
        last_spoken = n
    del(last_turn[nums[-1]])

    for turn in range(len(nums) + 1, turns + 1):
        if last_spoken in last_turn:
            speak = turn - 1 - last_turn[last_spoken]
        else:
            speak = 0
        last_turn[last_spoken] = turn - 1
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
