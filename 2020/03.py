from itertools import cycle, count, islice, starmap, tee
from math import prod as product

FILENAME = '03-input.txt'

def is_tree(drop, line):
    return next(islice(cycle(line.strip()), drop, None)) == '#'

def down_2(lines):
    while True:
        # yield 1, drop 1
        yield next(lines)
        if next(lines, None) is None:
            return

with open(FILENAME) as report:
    a, b, c, d, e  = tee(report, 5)
    a = sum(starmap(is_tree, zip(count(0, 1), a)))
    b = sum(starmap(is_tree, zip(count(0, 3), b)))
    c = sum(starmap(is_tree, zip(count(0, 5), c)))
    d = sum(starmap(is_tree, zip(count(0, 7), d)))
    e = sum(starmap(is_tree, zip(count(0, 1), down_2(e))))
    
    print(b)
    print(product([a,b,c,d,e]))
