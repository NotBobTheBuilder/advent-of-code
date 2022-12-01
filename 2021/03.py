from collections import Counter

FILENAME = '03-input.txt'

def count(lines):
    """
    Produce a list of counters, where at each index, the counter summarises the frequency 
    of characters in the elements of the input list at that index within the element

    counter(['ab'], ['cd']) == [Counter({'a': 1, 'c': 1}), Counter({'b': 1, 'd': 1})]
    """
    sums = []
    for line in lines:
        for index, value in enumerate(line):
            if len(sums) <= index:
                sums.append(Counter())
            sums[index][value] += 1
    return sums


with open(FILENAME) as report:
    report_lines = [line.strip() for line in report]
    sums = count(report_lines)

    gamma = ''
    epsilon = ''
    oxygen_searches = report_lines
    co2_searches = report_lines

    for position_idx, position in enumerate(sums):
        (most, most_num), (least, least_num) = position.most_common(2)
        gamma += most
        epsilon += least

        if len(oxygen_searches) > 1:
            (most, most_num), (least, least_num) = count(oxygen_searches)[position_idx].most_common(2)
            sought = most if most_num > least_num else '1' 
            oxygen_searches = [ num for num in oxygen_searches if num[position_idx] == sought ]

        if len(co2_searches) > 1:
            (most, most_num), (least, least_num) = count(co2_searches)[position_idx].most_common(2)
            sought = least if most_num > least_num else '0'
            co2_searches = [ num for num in co2_searches if num[position_idx] == sought ]

    print(int(gamma, 2) * int(epsilon, 2))
    print(int(oxygen_searches[0], 2) * int(co2_searches[0], 2))
