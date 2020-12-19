data = open('input').read()
rules_raw, messages_raw = data.split('\n\n')

rules = {}
for line in rules_raw.strip().splitlines():
  k, rest = line.split(':')
  parts = rest.split('|')
  rules[int(k)] = [tuple(map(eval, p.split())) for p in parts]

def gen_regexp(r):
  # Below is part 2. Comment out for part 1
  if r == 8:
    return '(' + gen_regexp(42) + ')+'
  if r == 11:
    r42 = gen_regexp(42)
    r31 = gen_regexp(31)
    parts = []
    # We don't generally make it work, we just make it work for up to
    # 10 recursions of rule 11 which is good enough for our input.
    for i in range(1, 10):
      parts.append('(%s){%d}(%s){%d}' % (r42, i, r31, i))
    return '(' + '|'.join(parts) + ')'
  
  if isinstance(r, str):
    return r
  parts = rules[r]
  if len(parts) == 1:
    return ''.join(gen_regexp(child) for child in parts[0])
  return '(' + '|'.join(''.join(gen_regexp(child) for child in p) for p in parts) + ')'

import re
m = re.compile('^' + gen_regexp(0) + '$')
count = 0
for line in messages_raw.strip().splitlines():
  if m.match(line.strip()):
    count += 1
print(count)
