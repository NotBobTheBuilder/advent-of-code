from itertools import takewhile
from collections import Counter

FILENAME = '13-input.txt'

def points(file):
    for line in takewhile(lambda x: len(x) > 0, file):
        x, y = line.split(',')
        yield int(x), int(y)

def fold(paper, instruction):
    axis, value = instruction.replace('fold along ', '').split('=')
    value = int(value)
    new_paper = Counter()
    for (x,y) in paper:
        if axis == 'x' and x > value:
            new_paper[value+(value-x),y] += paper[x,y]
        
        elif axis == 'y' and y > value:
            new_paper[x, value+(value-y)] += paper[x,y]
        elif paper[x,y] > 0:
            new_paper[x,y] = paper[x,y]
    return new_paper



def part_01(points, instructions):
    paper = Counter(points)
    instruction = instructions[0]

    new_paper = fold(paper, instruction)
    return sum(1 for v in new_paper.values() if v > 0)

def part_02(points, instructions):
    paper = Counter(points)
    for instruction in instructions:
        paper = fold(paper, instruction)

    
    max_x = max(x for x,y in paper)
    max_y = max(y for x,y in paper)
    
    return '\n'.join(''.join('#' if paper[x,y] else ' ' for x in range(max_x+1)) for y in range(max_y+1))

with open(FILENAME) as f:
    contents = (l.strip() for l in f)
    initial_points = list(points(contents))
    instructions = list(contents)
    print(part_01(initial_points, instructions))
    print(part_02(initial_points, instructions))
