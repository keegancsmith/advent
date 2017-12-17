#!/usr/bin/env python3

# Rank 25 for part 2. This is essentially the original version as I did the
# contest. Asciicast at https://asciinema.org/a/YGlRfXospB0lDJqMW0InuziVo

step = 312

l = [0]
i = 0
for j in range(1, 2018):
    i = (i + step) % len(l) + 1
    l.insert(i, j)
i = (i + 1) % len(l)
print(l[i])

zero_idx = 0
after_zero = None
l = 1
i = 0
for j in range(1, 50000000 + 1):
    i = (i + step) % l + 1
    if i <= zero_idx:
        zero_idx += 1
    if i == zero_idx + 1:
        after_zero = j
    l += 1
print(after_zero)
