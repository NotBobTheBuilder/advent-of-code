from itertools import count, takewhile, pairwise
from collections import Counter
from dataclasses import dataclass

FILENAME = '17-input.txt'

@dataclass
class Area:
    x_range: range
    y_range: range
    
    def __contains__(self, point):
        x, y = point
        return x in self.x_range and y in self.y_range

    def collides_line(self, points):
        return any(p in self for p in points)

def y_points(y_v):
    y = 0
    while True:
        y += y_v
        y_v -= 1
        yield y

def x_points(x_v):
    x = 0
    while True:
        x += x_v
        if x_v > 0:
            x_v -= 1
        elif x_v < 0:
            x_v += 1
        yield x

def count_with_negative(n=0):
    pos = count(n)
    neg = count(n-1, -1)
    while True:
        yield next(pos)
        yield next(neg)

def find_y_velocities_hitting_target(target):
    for counter in count_with_negative():
        for pt1, pt2 in pairwise(y_points(counter)):
            if pt1 in target.y_range or pt2 in target.y_range:
                yield counter
                break
            if pt2 < target.y_range.start:
                if abs(pt1 - pt2) > len(target.y_range)**2:
                    return
                break

def find_x_velocities_hitting_target(target):
    for counter in count(1):
        if counter > target.x_range.stop:
            return
        for pt1, pt2 in pairwise(x_points(counter)):
            if pt1 in target.x_range or pt2 in target.x_range:
                yield counter
                break
            if pt1 == pt2: 
                break

def path(x_v, y_v, target):
    xps = takewhile(lambda x: x <= target.x_range.stop, x_points(x_v))
    yps = takewhile(lambda y: y >= target.y_range.start, y_points(y_v))
    return list(zip(xps, yps))

def part_01(target):
    y_v = max(find_y_velocities_hitting_target(target))
    return max(takewhile(lambda n: n >= target.y_range.start, y_points(y_v)))

def part_02(target):
    return sum(1 for x in find_x_velocities_hitting_target(target)
                 for y in find_y_velocities_hitting_target(target)
                 if target.collides_line(path(x, y, target)))

with open(FILENAME) as f:
    line = f.read().strip()
    x, y = line.replace('target area: ', '').split(', ')
    x_start, x_end = x.replace('x=', '').split('..')
    y_start, y_end = y.replace('y=', '').split('..')
    area = Area(x_range=range(int(x_start), int(x_end)+1),
                y_range=range(int(y_start), int(y_end)+1))
    print(part_01(area))
    print(part_02(area))
