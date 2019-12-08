import itertools

initial_prog = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]

def run(inputs):
    prog = initial_prog[:]
    pc = 0
    while prog[pc] != 99:
        inst = prog[pc]
        if prog[pc] > 99:
            modes = [inst // 100 % 10, inst // 1000 % 10]
            inst = inst % 100
        else:
            modes = [0, 0]

        def get(i):
            if modes[i-1] == 0:
                return prog[prog[pc + i]]
            else:
                return prog[pc + i]

        if inst == 1:
            prog[prog[pc+3]] = get(1) + get(2)
            pc += 4

        elif inst == 2:
            prog[prog[pc+3]] = get(1) * get(2)
            pc += 4

        elif inst == 3:
            prog[prog[pc+1]] = inputs.pop(0)
            pc += 2

        elif inst == 4:
            got = yield get(1)
            assert got is not None
            inputs.append(got)
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
            prog[prog[pc+3]] = 1 if get(1) < get(2) else 0
            pc += 4

        elif inst == 8:
            prog[prog[pc+3]] = 1 if get(1) == get(2) else 0
            pc += 4

        else:
            assert False, prog[pc]

def a():
    for settings in itertools.permutations(range(0, 5)):
        output = 0
        for i in settings:
            g = run([i, output])
            output = next(g)
        yield output
    
def b():
    for settings in itertools.permutations(range(5, 10)):
        output = 0
        gens = []
        for i in settings:
            g = run([i, output])
            output = next(g)
            gens.append(g)

        for g in itertools.cycle(gens):
            try:
                output = g.send(output)
            except StopIteration:
                break

        yield output

print('A', max(a()))
print('B', max(b()))
