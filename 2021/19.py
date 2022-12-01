from collections import defaultdict
from itertools import takewhile
from math import sqrt

FILENAME = '19-input.txt'

class Matrix:
    def __init__(self, mtx):
        self.mtx = { (row_i, col_i): val for row_i, row in enumerate(mtx)
                                         for col_i, val in enumerate(row) }
        self.num_rows = len(mtx)
        self.num_cols = len(mtx[0])

    def __iter__(self):
        for row in range(self.num_rows):
            yield [ self.mtx[row, col] for col in range(self.num_cols) ]

    def row(self, i):
        return [ self.mtx[i, col] for col in range(self.num_cols) ]

    def col(self, i):
        return [ self.mtx[row, i] for row in range(self.num_rows) ]  

    def __matmul__(self, other):
        return Matrix([
            [   sum(a * b for a, b in zip(self.row(row), other.col(col)))
                for col in range(other.num_cols)
            ] for row in range(self.num_rows)
        ])

    def __add__(self, other):
        assert self.num_rows == other.num_rows
        assert self.num_cols == other.num_cols
        return Matrix([ [ sval + oval for sval, oval in zip(srow, orow) ] 
                        for srow, orow in zip(self, other) ])

    def __sub__(self, other):
        assert self.num_rows == other.num_rows
        assert self.num_cols == other.num_cols
        return Matrix([ [ sval - oval for sval, oval in zip(srow, orow) ] 
                        for srow, orow in zip(self, other) ])

    def __transpose__(self, other):
        pass

    @staticmethod
    def identity(size):
        [[ 1 if row == col else 0 for col in range(size) ] for row in range(size)]


    def rotate_onto(self, other):
        numerator = (self + other) @ (self + other).transpose()
        denominator = (self + other).transpose() @ (self + other)

        return 2 * (numerator / denominator) - Matrix.identity(3)

class Beacon:
    def __init__(self, bcn):
        self.bcn = bcn
        self.x, self.y, self.z = self.bcn.col(0)
        
    def distance(self, other):
        dx = (max(self.x, other.x) - min(self.x,  other.x)) ** 2
        dy = (max(self.y, other.y) - min(self.y,  other.y)) ** 2
        dz = (max(self.z, other.z) - min(self.z,  other.z)) ** 2
        return sqrt(dx + dy + dz)

    def vector(self, other):
        return other.bcn - self.bcn

    def translate(self, vector):
        return Beacon(self.bcn + self.vector)

class Scanner:
    def __init__(self, num):
        self.num = num
        self.beacons = []
        self.distances = defaultdict(list)

    def add_beacon(self, beacon):
        for other in self.beacons:
            self.distances[beacon.distance(other)].append((beacon, other))

    def merge(self, other):
        overlaps = set(self.distances) & set(other.distances)
        if len() >= 12:
            pass

def read_scanners(file):
    file = (line.strip() for line in file)
    while (scanner_line := list(takewhile(len, file))):
        scanner_num, *beacons = scanner_line
        num = int(scanner_num.replace('--- scanner ', '').replace(' ---', ''))
        scanner = Scanner(num)
        for beacon in beacons:
            scanner.add_beacon(Beacon(Matrix([ [int(n)] for n in beacon.split(',')] )))
        yield scanner

def merge_all(scanners):
    pass

def part_01(scanners):
    return len(merge_all(scanners).beacons)

with open(FILENAME) as f:
    scanners = list(read_scanners(file))
    
