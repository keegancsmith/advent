#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

def solveA(lines):
    for line in lines:
        print(line)

def solveB(lines):
    pass

data = '''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''
data = open('input').read()

foods = []
for line in data.splitlines():
    line = line.strip()
    if not line:
        continue
    ingredients, allergens = line.split('(contains')
    ingredients = set(ingredients.split())
    allergens = set(allergens.strip(')').strip().split(', '))
    foods.append((ingredients, allergens))

A = {}
for ingredients, allergens in foods:
    for a in allergens:
        if a in A:
            A[a] = ingredients & A[a]
        else:
            A[a] = ingredients

all_ingredients = set(itertools.chain(*(ing for ing, _ in foods)))
dangerous = set(itertools.chain(*A.values()))
ansA = 0
for ing in all_ingredients - dangerous:
    ansA += sum(ing in ings for ings, _ in foods)
print("A", ansA)

danger_list = []
while A:
    for allergen, v in A.items():
        if len(v) == 1:
            break
    else:
        assert False
    del(A[allergen])

    ing = v.pop()
    for v in A.values():
        v.discard(ing)

    danger_list.append((allergen, ing))

danger_list.sort()
print(','.join(ing for _, ing in danger_list))
