from itertools import tee, pairwise, starmap
from operator import sub
from collections import Counter

FILENAME = '10-input.txt'

def part_01(adapters):
    adapters = [0] + list(sorted(int(joltage) for joltage in adapters))
    adapters += [ adapters[-1] + 3 ]
    one_jolt_jumps = 0
    three_jolt_jumps = 0
    for (low, high) in pairwise(adapters):
        if low + 1 == high:
            one_jolt_jumps += 1

        if low + 3 == high:
            three_jolt_jumps += 1

    return one_jolt_jumps * three_jolt_jumps


joltage_overlap = range(1, 4)

def part_02(adapters):
    output_joltage = adapters[-1] + 3
    adapters = [ 0 ] + adapters + [ output_joltage ]

    # We'll count the ways to "reach" each adapter
    pathways_to_joltage = Counter()
    # hardcode that there is only 1 way to reach the start point
    pathways_to_joltage[0] = 1

    for adapter in adapters:
        # The only way to reach an adapter is from the adapters before it
        # where the difference is within the overlap range
        
        # Therefore, the number of pathways to get to this adapter, 
        # is the sum of the number of pathways to get to all the connectable previous adapters
        for delta in joltage_overlap:
            pathways_to_joltage[adapter] += pathways_to_joltage[adapter-delta]

    return pathways_to_joltage[output_joltage]

with open(FILENAME) as adapters:
    print(part_02(list(sorted(int(a) for a in adapters))))
