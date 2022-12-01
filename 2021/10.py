FILENAME = '10-input.txt'

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

AUTOCOMPLETE_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

class Illegal(Exception):
    def __init__(self, char):
        self.char = char

def _read(chars, closing):
    while (c := next(chars, None)):
        if c == closing:
            return
        elif c in PAIRS:
            yield from _read(chars, PAIRS[c])
        else:
            raise Illegal(c)
    yield closing

def part_01(file):
    score = 0
    for line in file:
        line = line.strip()
        char, line = line[0], line[1:]
        try:
            ''.join(_read(iter(line), PAIRS[char]))
        except Illegal as e:
            score += SCORES[e.char]
    return score

def part_02(file):
    for line in file:
        score = 0
        line = line.strip()
        hd, tail = line[0], line[1:]
        try:
            autocomplete = ''.join(_read(iter(tail), PAIRS[hd]))
        except Illegal:
            continue
        for char in autocomplete:
            score *= 5
            score += AUTOCOMPLETE_SCORE[char]
        yield score 

with open(FILENAME) as f:
    f = list(f)
    print(part_01(f))
    sorted_scores = sorted(part_02(f))
    print(sorted_scores[len(sorted_scores)//2])

