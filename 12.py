from collections import ChainMap

FILENAME = '12-input.txt'


def read_graph(lines):
    graph = {}
    for line in lines:
        a, b = line.strip().split('-')
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    return graph


def is_small_cave(cave_name):
    return cave_name == cave_name.lower()


def remove_position(position, graph):
    # remove all the reciprocal links to this position
    for link in graph[position]:
        graph[link] = [l for l in graph[link] if l != position]

    # now remove this position
    graph[position] = []


def breadth_first_search(graph, position, allow_extra_visit):
    if position == 'end':
        yield [ 'end' ]
        return

    next_steps = graph[position]
    for next_step in next_steps:
        new_graph = graph.new_child()
        if is_small_cave(position):
            remove_position(position, new_graph)

            if allow_extra_visit and position != 'start':
                # make the step without removing it from the graph - we can visit twice
                for sub_path in breadth_first_search(graph, next_step, False):
                    yield [position] + sub_path

        for sub_path in breadth_first_search(new_graph, next_step, allow_extra_visit):
            yield [position] + sub_path

def part_01(graph):
    return sum(1 for _ in breadth_first_search(ChainMap(graph), 'start', False))
    
def part_02(graph):
    return sum(1 for _ in set(','.join(p) for p in breadth_first_search(ChainMap(graph), 'start', True)))

with open(FILENAME) as f: 
    graph = read_graph(f)
    print(part_01(graph))
    print(part_02(graph))
