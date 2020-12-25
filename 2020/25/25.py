#!/usr/bin/env python3

a = 16915772
b = 18447943
mod = 20201227
base = 7

def find_exp(target):
  for exp in range(base * mod):
    if pow(base, exp, mod) == target:
      return exp

card = pow(a, find_exp(b), mod))
print(card)
door = pow(b, find_exp(a), mod))
assert door == card
