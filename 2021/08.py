from itertools import groupby

FILENAME = '08-input.txt'

NUMBERS = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

LENGTHS = {k: list(vs) for k, vs in groupby(sorted(NUMBERS), len)}

NUMBERS_WITH_SEGMENT = {segment: [NUMBERS[n] for n in NUMBERS if segment in n] for segment in 'abcdefg'}


def part_01(report):
    ones_fours_sevens_eights = 0
    for line in report:
        _, displays = line.split(' | ')
        displays = [''.join(sorted(display)) for display in displays.strip().split(' ')]

        for display in displays:
            if len(LENGTHS[len(display)]) == 1:
                ones_fours_sevens_eights += 1
    return ones_fours_sevens_eights


def get_conversions(signals):
    # start assuming any number can map to any other number
    possibilities = { char: set('abcdefg') for char in 'abcdefg' }

    # if a display signal has a unique length, its segments can only be the 
    # segments for whatever that unique number may be
    for signal in signals:
        if len(LENGTHS[len(signal)]) == 1:
            for char in signal:
                possibilities[char] &= set(LENGTHS[len(signal)][0])
                if len(possibilities[char]) == 1:
                    for k in possibilities:
                        if k == char:
                            break
                        possibilities[k] -= set([char])

    # if a segment is not used in the NUMBERS map as often as it is used here, 
    # it cannot be a posibility
    for s in possibilities:
        for possibility in set(possibilities[s]):
            signals_with_possibility = [sig for sig in signals if s in sig]
            nsp = NUMBERS_WITH_SEGMENT[possibility]
            if len(signals_with_possibility) != len(nsp):
                possibilities[s] -= set(possibility)

    # if a segment only has 1 possible correct value, that value cannot be the value
    # of any other segments
    for s in possibilities: 
        if len(possibilities[s]) == 1:
            for k in possibilities:
                if k == s:
                    continue
                possibilities[k] -= possibilities[s]

    # create 2 strings of "our" segments and the true segments and make a 
    # translation table
    thisline = ''
    diagram = ''
    for s in possibilities:
        thisline += s
        diagram += next(iter(possibilities[s]))
    return str.maketrans(thisline,diagram)

def part_02(report):
    total = 0

    for line in report:
        signals, displays = line.split(' | ')
        # create a translation table from the signal part of the message
        signals = [''.join(sorted(signal)) for signal in signals.strip().split(' ')]
        conversions = get_conversions(signals)

        # use the translation table to determine the number being displayed
        displays = [display for display in displays.strip().split(' ')]
        displays = [''.join(sorted(display.translate(conversions))) for display in displays]

        total += int(''.join(str(NUMBERS[display]) for display in displays))

    return total

with open(FILENAME) as report:
    print(part_02(report))
