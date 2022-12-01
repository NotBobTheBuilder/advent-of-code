from collections import Counter
from itertools import pairwise

FILENAME = '14-input.txt'

def read_rules(file):
    rules = {}
    for line in file:
        pattern, element = line.strip().split(' -> ')
        rules[pattern[0], pattern[1]] = element

    return rules

def run_rules(template, rules, iterations):
    pair_counts = Counter(pairwise(template))

    char_counts = Counter(template)

    for _ in range(iterations):
        new_pair_counts = Counter()
        for pair in pair_counts:
           (a, b) = pair
           # count the new pairs
           new_pair_counts[a, rules[pair]] += pair_counts[pair]
           new_pair_counts[rules[pair], b] += pair_counts[pair]
           # count the new element
           char_counts[rules[pair]] += pair_counts[pair]
        pair_counts = new_pair_counts

    max_char, max_freq = char_counts.most_common()[0]
    min_char, min_freq = char_counts.most_common()[-1]

    return max_freq - min_freq

def part_01(template, rules):
    return run_rules(template, rules, 10)

def part_02(template, rules):
    return run_rules(template, rules, 40)

with open(FILENAME) as f:
    template = next(f).strip()
    next(f)
    rules = read_rules(f)
    print(part_01(template, rules))
    print(part_02(template, rules))
