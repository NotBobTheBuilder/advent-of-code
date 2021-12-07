from itertools import tee, permutations, islice

FILENAME = '09-input.txt'
PREAMBLE_SIZE = 25

def _n_wise(iterable, num):
    """
    Helper for n_wise
    return num iterators, each skipping the first element of the previous iterator
    _n_wise([1,2,3,4,5], 3) => [1,2,3,4,5], [2,3,4,5], [3,4,5]
    """
    iterators = tee(iterable, num)
    for i in range(num):
        yield iterators[0]
        iterators = iterators[1:]
        for iterator in iterators:
            next(iterator, None)

def n_wise(iterable, num):
    """
    Return num copies of iterable, each skipping the first element of the previous iterator.
    n_wise([1,2,3,4,5], 3) => [1,2,3], [2,3,4], [3,4,5]
    """
    return zip(*_n_wise(iterable, num))

def part_01(numbers):
    previous_25s = n_wise(numbers, PREAMBLE_SIZE)
    sums = numbers[PREAMBLE_SIZE:]
    
    for num, preamble in zip(sums, previous_25s):
        if num not in map(sum, permutations(preamble, 2)):
            return num

def part_02(target, numbers):
    for i in range(len(numbers)):
        acc_sum = numbers[i] 

        acc_min = numbers[i]
        acc_max = numbers[i]

        for j in range(i+1, len(numbers)):
            acc_sum += numbers[j]

            acc_min = min([acc_min, numbers[j]])
            acc_max = max([acc_max, numbers[j]])

            if acc_sum > target:
                break

            if acc_sum == target:
                return acc_min + acc_max


with open(FILENAME) as numbers:
    numbers = list(int(n) for n in numbers)
    print(part_02(part_01(numbers), numbers))
