FILENAME = '01-input.txt'

def group_by_elf(iterator):
    accumulator = []
    for line in iterator:
        line = line.strip()
        if line == '':
            yield accumulator
            accumulator = []
        else:
            accumulator.append(int(line))
    yield accumulator

def part_01(elves):
    return max(sum(cals) for cals in elves)

def part_02(elves):
    sorted_sums = sorted((sum(cals) for cals in elves), reverse=True)
    return sum(sorted_sums[:3])

with open(FILENAME) as f:
    values = list(group_by_elf(f))
    print(part_01(values))
    print(part_02(values))
