#!/usr/bin/env python3

from collections import defaultdict, deque

def solve(cups, partA):
    cups = deque(cups)
    minCup = min(cups)
    maxCup = max(cups)

    if partA:
        moves = 100
    else:
        cups.extend(range(maxCup + 1, maxCup + 1 + (1000000 - len(cups))))
        assert len(cups) == 1000000, len(cups)
        maxCup = max(cups)
        moves = 10000000

    # From
    # https://old.reddit.com/r/adventofcode/comments/kimluc/2020_day_23_solutions/ggrulhj/
    # Rather than doing the insert, lazily store it for when you next read it
    lazy_insert = defaultdict(list)
    def popleft():
        front = cups.popleft()
        if front in lazy_insert:
            cups.extendleft(reversed(lazy_insert[front]))
            del lazy_insert[front]
        return front

    for move in range(moves):
        front = [popleft(), popleft(), popleft(), popleft()]

        dest = front[0]
        while dest in front:
            dest -= 1
            if dest < minCup:
                dest = maxCup

        lazy_insert[dest] += front[1:]
        cups.append(front[0])

    while (v := popleft()) != 1:
        cups.append(v)

    if partA:
        digits = []
        while cups:
            digits.append(popleft())
        return ''.join(map(str, digits))
    else:
        a, b = popleft(), popleft()
        return a*b


#cups = list(map(int, '389125467'))
cups = list(map(int, '487912365'))

print('A', solve(cups, True))
print('B', solve(cups, False))
