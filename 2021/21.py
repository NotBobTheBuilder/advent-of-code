from collections import Counter
from itertools import count, cycle, islice, product

FILENAME = '21-input.txt'

class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0

    def add_score(self, score):
        self.position += score
        self.position = self.position % 10 if self.position % 10 else 10
        self.score += self.position


def read_position(pos_str):
    return int(pos_str.strip().split(' ')[-1])


def part_01(p1, p2):
    dice = enumerate(cycle(iter(range(1, 101))), 1)
    
    for p in cycle([p1, p2]):
        _, r1 = next(dice)
        _, r2 = next(dice)
        roll_num, r3 = next(dice)
        p.add_score(r1 + r2 + r3)
        if p.score >= 1000:
            return roll_num * (p2 if p1 == p else p1).score

ROLLS = Counter(map(sum, product((1, 2, 3), repeat=3)))

def scores(start):
    scores = Counter([start])

    while True:
        next_scores = Counter()
        wins = 0
        for score, freq1 in scores.items():
            for roll, freq2 in ROLLS.items():
                round_score = (score + roll) % 10
                if round_score == 0:
                    round_score = 10
                next_scores[score + round_score] = freq1 * freq2
        yield next_scores
        scores = Counter({k, v for k, v in next_scores if v < 21})

def part_02(p1, p2):
    win_universes = Counter()

    print(sum(islice(scores(4), 20)))
    print(sum(islice(scores(8), 20)))

with open(FILENAME) as f:
    p1 = Player(read_position(next(f)))
    p2 = Player(read_position(next(f)))
    print(part_01(p1, p2))
    print(part_02(p1, p2))
