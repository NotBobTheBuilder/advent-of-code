from functools import reduce
from itertools import dropwhile, pairwise, product

FILENAME = '05-input.txt'

ALL_ROWS = list(range(0, 128))
ALL_COLS = list(range(0, 8))
ALL_SEATS = list(product(ALL_ROWS, ALL_COLS))

def seat_id(seat):
    row, col = seat
    return row * 8 + col


def half_range(range_to_shrink, direction):
    halfway_point = len(range_to_shrink) // 2

    if direction in 'FL':
        return range_to_shrink[:halfway_point]

    if direction in 'BR':
        return range_to_shrink[halfway_point:]


def card_to_seat(card):
    rows, cols = card[:7], card[7:]

    row, = reduce(half_range, rows, ALL_ROWS)
    col, = reduce(half_range, cols, ALL_COLS)

    return (row, col)
    
def part_01(cards):
    return max(seat_id(card_to_seat(card.strip())) for card in cards)

def part_02(cards):
    all_seats = set(ALL_SEATS) - set(card_to_seat(card.strip()) for card in cards)

    return seat_id(next(dropwhile(lambda a: a[0][0] == a[1][0], zip(sorted(all_seats), ALL_SEATS)))[0])


with open(FILENAME) as cards:
    print(part_02(cards))
