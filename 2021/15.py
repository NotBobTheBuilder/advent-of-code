from dataclasses import dataclass, field
from math import sqrt

FILENAME = '15-input.txt'

@dataclass
class Cell:
    score: int = field()
    heuristic: int = field()
    cell: tuple = field()

    def neighbours(self):
        x, y = self.cell
        return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

class SortedList:
    def __init__(self, /, *, init=None, key=None):
        self.key = (lambda x: x) if key is None else key
        if init is None:
            init = []
        self.list = sorted(init, key=self.key)

    def pop_first(self):
        first, self.list = self.list[0], self.list[1:]
        return first

    def peep_where(self, predicate):
        for i in range(len(self.list)):
            if predicate(self.list[i]):
                return self.list[i]

    def pop_where(self, predicate):
        for i in range(len(self.list)):
            if predicate(self.list[i]):
                return self.list.pop(i)

    def add(self, el):
        order_val = self.key(el)
        for i in range(len(self.list)):
            if order_val < self.key(self.list[i]):
                self.list.insert(i, el)
                return
        self.list.append(el)
        

def path_from(sources, target):
    path = []
    cell = target
    while cell in sources:
        path.insert(0, cell)
        cell = sources[cell].cell
    return path


def astar(graph, target):
    open_list = SortedList(key=lambda c: c.heuristic)
    closed_cells = set()
    sources = {}
    max_x, max_y = target

    open_list.add(Cell(score=0, heuristic=0, cell=(0,0)))

    while open_list:
        current = open_list.pop_first()
        closed_cells.add(current.cell)
        if current.cell == target:
            return sources
        for neighbour in current.neighbours():
            if neighbour not in graph:
                continue
            if neighbour in closed_cells:
                continue
            nx, ny = neighbour
            neighbour_score = current.score + graph[neighbour]
            neighbour_cell = open_list.peep_where(lambda c: c.cell == neighbour)
            heuristic = neighbour_score + (max_x - nx) + (max_y - ny) 
            if neighbour_cell is None or neighbour_cell.score > neighbour_score:
                open_list.pop_where(lambda c: c.cell == neighbour)
                open_list.add(Cell(score=neighbour_score, heuristic=heuristic, cell=neighbour))
                sources[neighbour] = current


def part_01(graph):
    return sum(graph[p] for p in path_from(astar(graph, max(graph)), max(graph)))


def expand_graph(graph):
    max_x, max_y = max(graph)
    new_graph = {}
    for (x, y) in graph:
        for x_grid_pos, x_offset in enumerate(range(0, 5*max_x+1, max_x+1)):
            for y_grid_pos, y_offset in enumerate(range(0, 5*max_y+1, max_y+1)):
                val = graph[x,y] + x_grid_pos + y_grid_pos
                while val > 9:
                    val -= 9
                new_graph[x_offset + x, y_offset + y] = val

    return new_graph


def part_02(graph):
    graph = expand_graph(graph)        
    path = path_from(astar(graph, max(graph)), max(graph))
    return sum(graph[p] for p in path)

def read_graph(file):
    return {(x,y): int(n) for y, line in enumerate(f) for x,n in enumerate(line.strip())}

with open(FILENAME) as f:
    graph = read_graph(f)
    print(part_01(graph))
    print(part_02(graph))
