from operator import xor

FILENAME = '02-input.txt'

def is_valid_01(entry):
    limit, char_colon, password = entry.strip().split(' ')
    min_freq, max_freq = (int(freq) for freq in limit.split('-'))
    char = char_colon[0]

    return min_freq <= password.count(char) <= max_freq

def is_valid_02(entry):
    limit, char_colon, password = entry.strip().split(' ')
    a, b = (password[int(freq)-1] for freq in limit.split('-'))
    char = char_colon[0]

    return xor(a == char, b == char)

with open(FILENAME) as database:
    print(sum(1 for entry in database if is_valid_02(entry)))
