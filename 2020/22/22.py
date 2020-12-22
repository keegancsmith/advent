#!/usr/bin/env python3

p1 = [
    10,
    39,
    16,
    32,
    5,
    46,
    47,
    45,
    48,
    26,
    36,
    27,
    24,
    37,
    49,
    25,
    30,
    13,
    23,
    1,
    9,
    3,
    31,
    14,
    4,
]


p2 = [
    2,
    15,
    29,
    41,
    11,
    21,
    8,
    44,
    38,
    19,
    12,
    20,
    40,
    17,
    22,
    35,
    34,
    42,
    50,
    6,
    33,
    7,
    18,
    28,
    43,
]

def deck_value(deck):
    return sum((i + 1) * v for i, v in enumerate(reversed(deck)))

def combat(p1, p2, recursive = False):
    seen = set()

    while p1 and p2:
        if recursive:
            tp1 = tuple(p1)
            tp2 = tuple(p2)
            if tp1 in seen or tp2 in seen:
                return 1, p1
            seen.add(tp1)
            seen.add(tp2)

        t1, t2 = p1.pop(0), p2.pop(0)

        if recursive and t1 <= len(p1) and t2 <= len(p2):
            winner, _ = combat(p1[:t1].copy(), p2[:t2].copy(), recursive)
        elif t1 > t2:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            p1.append(t1)
            p1.append(t2)
        else:
            p2.append(t2)
            p2.append(t1)

    if p1:
        return 1, p1
    else:
        return 2, p2

_, deckA = combat(p1.copy(), p2.copy(), False)
_, deckB = combat(p1.copy(), p2.copy(), True)
print("A", deck_value(deckA))
print("B", deck_value(deckB))
