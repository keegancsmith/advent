#!/usr/bin/env python3

def evalA(expr):
    while ')' in expr:
        r = expr.index(')')
        l = expr.rindex('(', 0, r)
        expr = expr[:l] + evalA(expr[l+1:r]) + expr[r+1:]
    tokens = expr.split()
    while len(tokens) > 1:
        x, op, y = tokens[:3]
        if op == '*':
            v = int(x) * int(y)
        else:
            assert op == '+'
            v = int(x) + int(y)
        tokens = [str(v)] + tokens[3:]
    return tokens[0]

def evalB(expr):
    # Note to future self. cpbotha pointed out there is a nice hack to insert
    # parens to force precedence
    # https://en.wikipedia.org/wiki/Operator-precedence_parser#Alternative_methods
    cpbotha = False
    if cpbotha:
        return str(eval(
            '((('
            + expr.replace('(', '(((')
            .replace(')', ')))')
            .replace('+', ')+(')
            .replace('*', '))*((')
            + ')))'
        ))

    while ')' in expr:
        r = expr.index(')')
        l = expr.rindex('(', 0, r)
        expr = expr[:l] + evalB(expr[l+1:r]) + expr[r+1:]
    tokens = expr.split()
    while '+' in tokens:
        i = tokens.index('+')
        x, y = tokens[i-1], tokens[i+1]
        v = int(x) + int(y)
        tokens = tokens[:i-1] + [str(v)] + tokens[i+2:]
    while len(tokens) > 1:
        x, op, y = tokens[:3]
        assert op == '*'
        v = int(x) * int(y)
        tokens = [str(v)] + tokens[3:]
    return tokens[0]

assert evalA('2 * 3 + (4 * 5)') == '26'
assert evalA('5 + (8 * 3 + 9 + 3 * 4 * 3)') == '437'
assert evalA('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == '12240'
assert evalA('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == '13632'

assert evalB('1 + (2 * 3) + (4 * (5 + 6))') == '51'
assert evalB('2 * 3 + (4 * 5)') == '46'
assert evalB('5 + (8 * 3 + 9 + 3 * 4 * 3)') == '1445'
assert evalB('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == '669060'
assert evalB('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == '23340'

lines = open('input').readlines()

print('A', sum(int(evalA(l)) for l in lines))
print('B', sum(int(evalB(l)) for l in lines))
