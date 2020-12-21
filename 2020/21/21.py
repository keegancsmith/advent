#!/usr/bin/env python3

import itertools
from collections import defaultdict

foods = []
for line in open('input').read().strip().splitlines():
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

all_ingredients = set(itertools.chain.from_iterable(ing for ing, _ in foods))
dangerous = set(itertools.chain.from_iterable(A.values()))
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
