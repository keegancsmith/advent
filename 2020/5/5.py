#!/usr/bin/env python3


def seat_id(ticket):
    lower, upper = 0, 127
    for x in ticket[:7]:
        mid = (lower + upper) // 2
        if x == "F":
            upper = mid
        elif x == "B":
            lower = mid + 1
    assert lower == upper, "row " + ticket
    row = lower
    lower, upper = 0, 7
    for x in ticket[7:]:
        mid = (lower + upper) // 2
        if x == "L":
            upper = mid
        elif x == "R":
            lower = mid + 1
    assert lower == upper, "col " + ticket
    col = lower
    return row * 8 + col


def solveA(lines):
    return max(seat_id(t) for t in tickets)


def solveB(tickets):
    seats = set(seat_id(t) for t in tickets)
    for i in range(10000):
        if i not in seats and (i + 1) in seats and (i - 1) in seats:
            return i


tickets = [l.strip() for l in open("input") if l.strip()]

print("A", solveA(tickets))
print("B", solveB(tickets))
