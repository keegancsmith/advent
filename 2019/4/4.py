def valida(i):
    s = str(i)
    if not any(a == b for a, b in zip(s, s[1:])):
        return False
    return all(a <= b for a, b in zip(s, s[1:]))

def validb(i):
    s = str(i)
    s2 = ' ' + s + ' '
    if not any(b == c and a != b and c != d for a, b, c, d in zip(s2, s2[1:], s2[2:], s2[3:])):
        return False
    return all(a <= b for a, b in zip(s, s[1:]))

print('A', sum(1 if valida(i) else 0 for i in range(134792, 675810 + 1)))
print('B', sum(1 if validb(i) else 0 for i in range(134792, 675810 + 1)))
