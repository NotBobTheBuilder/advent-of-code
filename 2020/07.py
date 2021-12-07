from collections import defaultdict
from itertools import repeat

FILENAME = '07-input.txt'

class Bag:
    def __init__(self, colour):
        self.colour = colour
        self.contents = []
        self.containedby = set()

    def contains(self, num, bag):
        self.contents.append((num, bag))
        bag.containedby.add(self)

class DefaultDictKeyed(defaultdict):
    def __missing__(self, key):
        self[key] = self.default_factory(key)
        return self[key]

def containers(frontier):
    all_containers = set()
    while (frontier := set([el for el in frontier if el not in all_containers])):
        all_containers.update(frontier)
        frontier = [gp for parent in frontier for gp in parent.containedby]

    return all_containers

def contents(frontier):
    all_bags = list()
    while frontier:
        (hd_num, hd_val), frontier = frontier[0], frontier[1:]
        all_bags.extend(repeat(hd_val, hd_num))
        if hd_val.contents:
            frontier = hd_val.contents * hd_num + frontier

    return all_bags

def prepare(f):
    bags = DefaultDictKeyed(Bag)

    for line in f:
        outer, inners = line.strip('\n.').split(' contain ')
        outer = outer.replace(' bags', '').replace(' bag', '')
        if not inners == 'no other bags':
            for inner in inners.split(', '):
                num, innerbagname = inner.split(' ', 1)
                num = int(num)
                innerbagname = innerbagname.replace(' bags', '').replace(' bag', '')
                bags[outer].contains(num, bags[innerbagname])

    return bags

def part_01(bags):
    return len(containers(bags['shiny gold'].containedby))

def part_02(bags):
    return len(contents(bags['shiny gold'].contents))

with open(FILENAME) as f:
    print(part_02(prepare(f)))
