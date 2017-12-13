#!/usr/bin/env python3

# This is a cleaned up version. Unranked for part 1, 62nd for part 2. Live
# cast at https://asciinema.org/a/5S1VkWZ4DKzzpZCKvu0ImfChY

firewall = dict(map(int, line.split(': ')) for line in open('input'))
print('A', sum(d * r for d, r in firewall.items() if d % (r * 2 - 2) == 0))
delay = 0
while True:
    if all((d + delay) % (r * 2 - 2) != 0 for d, r in firewall.items()):
        print('B', delay)
        break
    delay += 1
