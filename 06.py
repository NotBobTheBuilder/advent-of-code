from collections import Counter
from itertools import repeat

FILENAME = '06-input.txt'

NEW_FISH = 8
MATERNAL_FISH = 6

def day(sea):
    """
    Take a counter of the number of fish of each age
    Return a counter of the number of fish of each age at the end of the day
    """
    next_sea = Counter()
    for i in range(1, NEW_FISH+1):
        next_sea[i-1] = sea[i]
    next_sea[NEW_FISH] += sea[0]
    next_sea[MATERNAL_FISH] += sea[0]

    return next_sea

with open(FILENAME) as statefile:
    sea = Counter(int(f) for f in statefile.readline().strip().split(','))
    for i in range(256):
        sea = day(sea)
    print(sum(sea.values()))
