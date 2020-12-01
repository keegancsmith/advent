import collections
G = {}

for line in open('input'):
    tokens = [t.strip(',') for t in line.split()]
    inputs = tuple(zip(map(int, tokens[:-3:2]), tokens[1:-3:2]))
    G[tokens[-1]] = (int(tokens[-2]), inputs)

extra = collections.defaultdict(int)
amount_ore = 0
Q = [(1, 'FUEL')]
while Q:
    amount, chemical = Q.pop(0)
    if chemical not in G:
        assert chemical == 'ORE'
        amount_ore += amount
        continue
    if extra[chemical] >= amount:
        extra[chemical] -= amount
        continue
    else:
        amount -= extra[chemical]
        extra[chemical] = 0
    num, inputs = G[chemical]
    multiplier = num // amount
    if num % amount != 0:
        multiplier += 1
        extra[chemical] += (num % amount)
    for n, child in inputs:
        Q.append((n * multiplier, child))
print(amount_ore)
