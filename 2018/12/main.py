#!/usr/bin/env python3

f = open('input').read()

parts = f.split()
state = list(parts[2])
rules = dict(zip(map(tuple, parts[3::3]), parts[5::3]))

def solve(state, rules, gen):
    assert state[0] == '#'
    offset = 0
    seen = {}
    for i in range(gen):
        d = state.index('#')
        offset += d
        state = state[d:]
        while state[-1] == '.':
            state.pop()
        state = ['.'] * 3 + state + ['.'] * 3
        offset -= 1
        state = [rules.get(p, '.') for p in zip(state[0:], state[1:], state[2:], state[3:], state[4:])]
        k = ''.join(state)
        if k in seen:
            break
        seen[k] = (i, offset)

    if i == gen - 1:
        return sum(i if p == '#' else 0 for i, p in zip(range(offset, offset + len(state)*2), state))
    
    # We luckily seem to have a simple repeating pattern for large gens
    loop_size = i - seen[k][0]
    loop_offset = offset - seen[k][1]
    assert loop_size == 1
    assert loop_offset == 1
    return sum(i if p == '#' else 0 for i, p in zip(range(offset + gen - i - 1, offset + gen - i - 1 + len(state)*2), state))

print(solve(state, rules, 20))
print(solve(state, rules, 50000000000))
