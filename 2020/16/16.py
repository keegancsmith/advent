#!/usr/bin/env python3

import itertools

data = open('input').read()
sections = data.split('\n\n')

rules = {}
for line in sections[0].splitlines():
    k, v = line.split(':')
    v = v.split()
    a, b = map(int, v[0].split('-'))
    c, d = map(int, v[-1].split('-'))
    rules[k] = ((a, b), (c, d))

your = tuple(map(int, sections[1].splitlines()[-1].split(',')))

tickets = []
for line in sections[2].splitlines()[1:]:
    tickets.append(tuple(map(int, line.split(','))))

def valid_ticket_field(v):
    return any(a <= v <= b or c <= v <= d for ((a, b), (c, d)) in rules.values())

print("A", sum(v for v in itertools.chain(*tickets) if not valid_ticket_field(v)))

def valid_ticket(ticket):
    return all(valid_ticket_field(v) for v in ticket)

# discard bad tickets
tickets = [ticket for ticket in tickets if all(valid_ticket_field(v) for v in ticket)]
tickets.append(your)

# Collect all possible positions for a rule to occupy
rule_pos = {}
for rule, ((a, b), (c, d)) in rules.items():
    valid = set()
    for i in range(len(tickets[0])):
        if all(a <= t[i] <= b or c <= t[i] <= d for t in tickets):
            valid.add(i)
    rule_pos[rule] = valid

# If a rule can only occupy one position, that must be its position. Remove
# that pos from the valid positions from everyone else. Continue this until
# nothing is left.
final = {}
while rule_pos:
    for rule, valid in rule_pos.items():
        if len(valid) == 1:
            break
    else:
        assert False
    i = valid.pop()
    final[rule] = i
    del(rule_pos[rule])
    for valid in rule_pos.values():
        valid.remove(i)

ansB = 1
for rule, i in final.items():
    if rule.startswith("departure"):
        ansB *= your[i]
print("B", ansB)
