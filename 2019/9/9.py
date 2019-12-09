import itertools, collections

def run(prog, inputs):
    prog = collections.defaultdict(int, enumerate(prog))
    pc = 0
    rbase = 0
    while prog[pc] != 99:
        inst = prog[pc]
        if prog[pc] > 99:
            modes = [inst // 100 % 10, inst // 1000 % 10, inst // 10000 % 10]
            inst = inst % 100
        else:
            modes = [0, 0, 0]

        def get(i):
            if modes[i-1] == 0:
                return prog[prog[pc + i]]
            elif modes[i-1] == 1:
                return prog[pc + i]
            else:
                return prog[rbase + prog[pc+i]]

        def set(i, v):
            if modes[i-1] == 0:
                prog[prog[pc + i]] = v
            elif modes[i-1] == 1:
                prog[pc + i] = v
            else:
                prog[rbase + prog[pc+i]] = v

        if inst == 1:
            set(3, get(1) + get(2))
            pc += 4

        elif inst == 2:
            set(3, get(1) * get(2))
            pc += 4

        elif inst == 3:
            set(1, inputs.pop(0))
            pc += 2

        elif inst == 4:
            yield get(1)
            pc += 2

        elif inst == 5:
            if get(1) != 0:
                pc = get(2)
            else:
                pc += 3

        elif inst == 6:
            if get(1) == 0:
                pc = get(2)
            else:
                pc += 3

        elif inst == 7:
            set(3, 1 if get(1) < get(2) else 0)
            pc += 4

        elif inst == 8:
            set(3, 1 if get(1) == get(2) else 0)
            pc += 4

        elif inst == 9:
            rbase += get(1)
            pc += 2

        else:
            assert False, prog[pc]

prog = [int(x) for x in open('input').read().split(',')]
for i in run(prog, [1]):
    print('A', i)
for i in run(prog, [2]):
    print('B', i)
