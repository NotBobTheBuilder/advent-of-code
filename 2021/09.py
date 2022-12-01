FILENAME = '09-input.txt'

def neighbours(cell):
    x, y = cell
    # clockwise neighbours
    return [ (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

def part_01(grid):
    for cell, value in grid.items():
        neighbour_heights = [grid[n] for n in neighbours(cell) if n in grid]
        if all(value < h for h in neighbour_heights):
            yield cell, 1 + value

def part_02(grid):
    basins = []
    # start at the low points, keep expanding around 
    for cell, _ in part_01(grid):
        new_basin = set()
        frontier = [ cell ]
        while frontier:
            el = frontier.pop()
            if el in new_basin:
                continue
            new_basin.add(el)
            frontier.extend(n for n in neighbours(el) if n in grid and grid[n] < 9)

        basins.append(new_basin)

    basins = sorted(basins, key=len, reverse=True)
    return len(basins[0]) * len(basins[1]) * len(basins[2])


with open(FILENAME) as f:
    grid = {(x, y): int(n) for y, line in enumerate(f) for x, n in enumerate(line.strip()) }
    print(sum(v for _, v in part_01(grid)))
    print(part_02(grid))
