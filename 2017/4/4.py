a = 0
b = 0
for line in open('input').readlines():
    p = line.split()
    if len(set(p)) == len(p):
        a += 1
    if len(set(''.join(sorted(x)) for x in p)) == len(p):
        b += 1
print(a)
print(b)
