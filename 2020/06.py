from functools import reduce
from itertools import takewhile 
from operator import and_

FILENAME = '06-input.txt'

def read_groups(file):
    while (group := list(takewhile(lambda l: len(l) > 0, (line.strip() for line in file)))):
        yield group

def part_01(groups):
    return sum(len(set(''.join(group))) for group in groups)

def common_answers(group):
    # compute size of the intersection of each persons answers
    return len(reduce(and_, (set(person) for person in group)))

def part_02(groups):
    return sum(common_answers(group) for group in groups)

with open(FILENAME) as f:
    print(part_02(read_groups(f)))
    
