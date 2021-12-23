from dataclasses import dataclass, field
from itertools import pairwise, permutations
from functools import reduce
from math import ceil
from operator import add

FILENAME = '18-input.txt'

@dataclass
class El:
    magnitude: int
    left: 'El' = None
    right: 'El' = None
    up: 'El' = None

    def leftmost_pair_by_depth(self, depth):
        return None

    def __str__(self):
        return str(self.magnitude)

    def set_left(self, left):
        self.left = left
        left.right = self

    def set_right(self, right):
        self.right = right
        right.left = self

    def in_order(self):
        yield self

    def split(self):
        if self.magnitude >= 10:
            left = El(magnitude=self.magnitude//2)
            right = El(magnitude=ceil(self.magnitude/2))
            left.set_right(right)
            if self.left:
                left.set_left(self.left)
            if self.right:
                right.set_right(self.right)
            new_pair = Pair(left=left, right=right, up=self.up)
            left.up = right.up = new_pair
            if self.up:
                if self == self.up.left:
                    self.up.left = new_pair
                else:
                    self.up.right = new_pair
            return True
        return False


@dataclass
class Pair:
    left: El
    right: El
    up: 'El' = None

    @property
    def magnitude(self):
        return self.left.magnitude * 3 + self.right.magnitude * 2

    def leftmost_pair_by_depth(self, depth):
        if depth == 0:
            return self
        if (left_pair := self.left.leftmost_pair_by_depth(depth-1)):
            return left_pair
        return self.right.leftmost_pair_by_depth(depth - 1)

    def _explode(self):
        assert type(self.left) == El
        assert type(self.right) == El
        zero = El(magnitude=0, up=self.up)
        if self.left.left:
            self.left.left.magnitude += self.left.magnitude
            self.left.left.set_right(zero)
        if self.right.right:
            self.right.right.magnitude += self.right.magnitude
            self.right.right.set_left(zero)

        if self.up.left == self:
            self.up.left = zero
        else:
            self.up.right = zero

    def in_order(self):
        yield from self.left.in_order()
        yield from self.right.in_order()

    def leftmost(self):
        left = self.left
        while left.left:
            left = left.left
        return left

    def rightmost(self):
        right = self.right
        while right.right:
            right = right.right
        return right

    def explode(self):
        while (pair := self.leftmost_pair_by_depth(4)):
            pair._explode()

    def split(self):
        return any(el.split() for el in self.in_order())

    def __str__(self):
        return f'[{str(self.left)},{str(self.right)}]'

    def __add__(self, other):
        new_pair = Pair(left=self, right=other)
        self.rightmost().set_right(other.leftmost())
        self.up = other.up = new_pair
        new_pair.explode()
        while new_pair.split():
            new_pair.explode()
        return new_pair

def read(num_str):
    if num_str[0] == '[':
        left, num_str = read(num_str[1:])
        right, num_str = read(num_str[1:])
        pair = Pair(left=left, right=right)
        left.up = right.up = pair
        return pair, num_str[1:]
    else:
        return El(magnitude=int(num_str[0])), num_str[1:]

def process(pair):
    for a, b in pairwise(pair.in_order()):
        a.set_right(b)

def read_line(line):
    p, _ = read(line)
    process(p)
    return p

def part_01(numbers):
    return reduce(add, map(read_line, numbers)).magnitude

def sums(numbers):
    for a, b in permutations(numbers, 2):
        yield (read_line(a) + read_line(b)).magnitude
    
def part_02(numbers):
    return max(sums(numbers))

with open(FILENAME) as f:
    numbers = list(f)
    print(part_01(numbers))
    print(part_02(numbers))
