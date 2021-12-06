from itertools import takewhile
from string import digits, hexdigits

FILENAME = '04-input.txt'

def is_four_digit_year_between(low, high):
    return lambda val: is_digits(4, digits)(val) and low <= int(val) <= high

def is_digits(num, digitstr):
    return lambda val: len(val) == num and all(d in digitstr for d in val)

def is_height(val):
    if 'cm' in val:
        return 150 <= int(val.replace('cm', '')) <= 193
    if 'in' in val:
        return 59 <= int(val.replace('in', '')) <= 76
    return False

def is_hair_colour(val):
    return val.startswith('#') and is_digits(6, hexdigits)(val[1:])

REQUIRED_FIELDS = {
    'byr': is_four_digit_year_between(1920, 2002),
    'iyr': is_four_digit_year_between(2010, 2020),
    'eyr': is_four_digit_year_between(2020, 2030),
    'hgt': is_height,
    'hcl': is_hair_colour,
    'ecl': 'amb blu brn gry grn hzl oth'.split(' ').__contains__,
    'pid': is_digits(9, digits),
}

def is_valid_01(line):
    parsed_line = dict(kv.split(':') for kv in line.strip().split(' '))
    return all(field in parsed_line for field in REQUIRED_FIELDS)

def is_valid_02(line):
    parsed_line = dict(kv.split(':') for kv in line.strip().split(' '))
    return all(field in parsed_line and validator(parsed_line[field]) \
                for field, validator in REQUIRED_FIELDS.items())


def read_entries(batch):
    while (lines := list(takewhile(lambda line: len(line.strip()) > 0, batch))):
        yield ' '.join(line.strip() for line in lines)

with open(FILENAME) as batch:
    print(sum(is_valid_02(line) for line in read_entries(batch)))
