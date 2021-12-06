from itertools import combinations
from math import prod as product

FILENAME = '01-input.txt'

def sums_to_2020(nums):
    return sum(nums) == 2020

def first_combination_matching(predicate, iterable, combination_size):
    return next(filter(predicate, combinations(iterable, combination_size)))

def part_01(report):
    return product(first_combination_matching(sums_to_2020, report, 2))

def part_02(report):
    return product(first_combination_matching(sums_to_2020, report, 3))

with open(FILENAME) as report:
    print(part_02(int(line) for line in report))
