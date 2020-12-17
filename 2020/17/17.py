import itertools

data = '''.##..#.#
##.#...#
##.#.##.
..#..###
####.#..
...##..#
#.#####.
#.#.##.#'''
state = set()
for r, line in enumerate(data.splitlines()):
  for c, v in enumerate(line):
    if v == '#':
      # Part A state.add((r, c, 0))
      state.add((r, c, 0, 0))

def neigh(p):
  return (
    # p + dp
    tuple(a + b for a, b in zip(p, dp))
    # (-1, 0, 1) ** len(p)
    for dp in itertools.product(*[range(-1, 2)]*len(p))
    # Exclude (0, ..., 0)
    if any(a != 0 for a in dp))

def next_state(last):
  # Build a set of all active positions and neighbours. This is a superset of
  # the next state.
  consider = last.copy()
  for p in last:
    consider.update(neigh(p))

  state = set()
  for p in consider:
    count = sum(1 if n in last else 0 for n in neigh(p))
    if p in last:
      if 2 <= count <= 3:
        state.add(p)
    elif count == 3:
      state.add(p)
  return state

for i in range(6):
  state = next_state(state)

print(len(state))
