from collections import Counter
from itertools import chain, repeat

FILENAME = '05-input.txt'

def axis_points(p1, p2):
    """
    Return the points on this axis. 
    If there is only one point, repeat it infinitely so it can be zipped
    with a finite axis
    """
    step = 1 if p2 > p1 else -1
    return range(p1, p2+step, step) if p1 != p2 else repeat(p1)

def points(line, skip_diagonals):
    """
    Return all the points on the line described by the line text.
    If the line is diagonal and skip_diagonal is true, the generator
    will be empty.
    """
    start, end = line.strip().split(' -> ')

    x1, y1 = int(pos) for pos in start.split(',')
    x2, y2 = int(pos) for pos in end.split(',')

    if skip_diagonals and x1 != x2 and y1 != y2:
        return
    
    yield from zip(axis_points(x1, x2), axis_points(y1, y2))

def part_01(f):
    """
    Count all the points on all the lines and find those with overlap (excluding diagonals)
    """
    counter = Counter(chain.from_iterable(points(line, skip_diagonals=True) for line in f))
    return sum(1 for (crossing, count) in counter.items() if count > 1)

def part_02(f):
    """
    Count all the points on all the lines and find those with overlap (including diagonals)
    """
    counter = Counter(chain.from_iterable(points(line, skip_diagonals=False) for line in f))
    return sum(1 for (crossing, count) in counter.items() if count > 1)

with open(FILENAME) as f:
    print(part_02(f))
