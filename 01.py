from itertools import pairwise, tee

FILENAME = '01-input.txt'

def threewise(iterator):
    """
    Produce a rolling 3-wide window over iterator
    """
    a, b, c = tee(iterator, 3)

    # use next to skip the first element in b and first 2 elements in c
    # the result is that the zipped iterators will be offset by 0-1-2
    next(b, None)

    next(c, None)
    next(c, None)

    return zip(a, b, c)

def report_lines(file_name):
    """
    Read the input lines into a number sequence
    """
    with open(file_name) as report:
        yield from (int(num) for num in report)

def part_1():
    """
    Count 1 for every increasing pair
    """
    return sum(1 for (a, b) in pairwise(report_lines(FILENAME)) if a < b)

def part_2():
    """
    First produce pairs of rolling-sums-of-threes
    Then Count 1 for every increasing pair of sums
    """
    threes_sums = (sum(three) for three in threewise(report_lines(FILENAME)))
    return sum(1 for (a, b) in pairwise(threes_sums) if a < b)

print(part_2())
