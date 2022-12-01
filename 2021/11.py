FILENAME = '11-input.txt'

def neighbours(cell):
    x, y = cell
    return [(x - xd, y - yd) for yd in range(-1, 2) for xd in range(-1, 2) if (x - xd, y - yd) != cell]

def run_step(grid):
    new_grid = dict(grid.items())
    flashed_octos = set()
    seen_neighbours = set()
    for cell, val in new_grid.items():
        new_grid[cell] += 1

    while any(val > 9 for val in new_grid.values()):
        for cell, val in new_grid.items():
            if new_grid[cell] > 9:
                new_grid[cell] = 0
                if cell in flashed_octos:
                    continue
                flashed_octos.add(cell)
                for neighbour in neighbours(cell):
                    if neighbour in new_grid and neighbour not in flashed_octos:
                            new_grid[neighbour] += 1
    return len(flashed_octos), new_grid


def part_01(grid):
    total_flashes = 0
    for step in range(100):
        flashes, grid = run_step(grid)
        total_flashes += flashes
    return total_flashes

def part_02(grid):
    step = 1
    while True:
        flashes, grid = run_step(grid)
        if flashes == len(grid):
            break
        step += 1
    return step

with open(FILENAME) as f:
    grid = {(x, y): int(val)    for y, row in enumerate(f) 
                                for x, val in enumerate(row.strip())}

    print(part_01(grid))
    print(part_02(grid))
