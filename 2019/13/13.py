import itertools, collections

def run(prog, inputs):
    prog = collections.defaultdict(int, enumerate(prog))
    pc = 0
    rbase = 0
    outputs = []
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
            outputs.append(get(1))
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
    return outputs

def solve(prog, white):
    seen = set()
    p = (0, 0)
    dx, dy = 0, 1
    vm = run(prog, [1 if p in white else 0])
    while True:
        if seen:
            try:
                color = vm.send(1 if p in white else 0)
            except StopIteration:
                break
        else:
            color = next(vm)

        seen.add(p)
        if color == 1:
            white.add(p)
        elif p in white:
            white.remove(p)

        turn = next(vm)
        if turn == 1:
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        p = (p[0] + dx, p[1] + dy)
    return seen, white

def solveA(prog):
    vm = run(prog, [])
    count = 0
    while True:
        try:
            x = next(vm)
        except StopIteration:
            return count
        y = next(vm)
        tile_id = next(vm)
        if tile_id == 2:
            count+=1

def solve(prog, inputs):
    score = -1
    try:
        outputs = run(prog, inputs[:])
        for i in range(0, len(outputs), 3):
            if outputs[i] == -1 and outputs[i+1] == 0:
                score = outputs[i+2]
        if score > 0:
            print(score, inputs)
        return score
    except IndexError:
        # This means we need to add on to the inputs
        pass

    return max(solve(prog, inputs + [move]) for move in (-1, 0, 1))
            
def solveB(prog):
    prog = prog[:]
    prog[0] = 2
    return solve(prog, [])

prog = [int(x) for x in open('input').read().split(',')]
#print('A', solveA(prog))
print('B', solveB(prog))
