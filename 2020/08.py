FILENAME = '08-input.txt'

def tokenise(program):
    for line in program:
        cmd, arg = line.strip().split(' ')
        yield (cmd, int(arg))

def run_until_cycle(program):
    seen_ops = set()
    op_idx = 0
    acc = 0

    while op_idx < len(program) and op_idx not in seen_ops:
        seen_ops.add(op_idx)
        op, arg = program[op_idx]
        if op == 'nop':
            op_idx += 1
        if op == 'jmp':
            op_idx += arg
        if op == 'acc':
            op_idx += 1
            acc += arg

    return acc, seen_ops, op_idx == len(program)

def op_swapped(program, op):
    for i in range(len(program)):
        cmd, arg = program[i]
        if i == op:
            yield ('nop' if cmd == 'jmp' else 'jmp'), arg
        else:
            yield cmd, arg

def run_01(program):
    return run_until_cycle(list(program))[0]

def run_02(program):
    program = list(program)
    _, ops, _ = run_until_cycle(program)

    for op in ops:
        if program[op][0] == 'acc':
            continue

        acc, _, finished = run_until_cycle(list(op_swapped(program, op)))
        if finished:
            return acc

with open(FILENAME) as program:
    print(run_02(list(tokenise(program))))
