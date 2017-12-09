#!/usr/bin/env python3

# Asciicast at https://asciinema.org/a/wUtD7YSuRfQjVHHmzdcInrOww

stream = next(open('input')).strip()

stack = [0]
ansa = 0
ansb = 0
in_garbage = False
ignore = False
for c in stream:
    if ignore:
        ignore = False
        continue
    if c == '!':
        ignore = True
        continue
    if in_garbage:
        if c == '>':
            in_garbage = False
        else:
            ansb += 1
        continue
    if c == '{':
        stack.append(stack[-1] + 1)
    if c == '}':
        ansa += stack.pop()
    if c == '<':
        in_garbage = True
print('A', ansa)
print('B', ansb)
