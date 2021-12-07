from collections import Counter

FILENAME = '08-input.txt'

def fuel_to_walk(crabs, position, fuel_func):
    return sum(fuel_func(abs(position - crab)) * num_crabs for (crab, num_crabs) in crabs.items())

def linear_fuel_for_steps(s):
    # We can use triangle numbers here. area of a triangle is w * h / 2
    # https://en.wikipedia.org/wiki/Triangular_number#Formula
    return (s * (s + 1)) // 2

def smallest_fuel(crabs, fuel_func):
    # use a range to search for spots as there might not already be a crab in the ideal spot
    possible_alignment_spots = range(min(crabs), max(crabs) + 1)
    return min(fuel_to_walk(crabs, spot, fuel_func) for spot in possible_alignment_spots)

def part_01(crabs):
    return smallest_fuel(crabs, lambda fuel: fuel)

def part_02(crabs):
    return smallest_fuel(crabs, linear_fuel_for_steps)

with open(FILENAME) as f:
    crabs = Counter(int(c) for c in f.readline().split(','))
    
    print(part_02(crabs))
