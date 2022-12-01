from itertools import product

FILENAME = '20-input.txt'

def neighbours(pos):
    x, y = pos
    return [ (nx, ny) for ny in range(y-1, y+2) for nx in range(x-1, x+2) ]

class Image:
    def __init__(self, image, default):
        self.image = image
        self.default = default

    def __getitem__(self, key):
        return self.image.get(key, self.default)

    def values(self):
        return self.image.values()

    def boundaries(self):
        min_x = min(self.image)[0]
        max_x = max(self.image)[0]
        min_y = min(self.image, key=lambda p: p[1])[1]
        max_y = max(self.image, key=lambda p: p[1])[1]
    
        return range(min_x-1, max_x+2), range(min_y-1, max_y+2)

    def next_val(self, pos, enhancement):
        idx = ''.join(self[n] for n in neighbours(pos))
        return enhancement[int(idx, 2)]

    def next_default(self):
        return '1' if self.default == '0' else '0'

    def __str__(self):
        xs, ys = self.boundaries()
        return '\n'.join(''.join('#' if self[x,y] == '1' else '.' for y in ys) for x in xs)

    def enhance(self, enhancement):
        xs, ys = self.boundaries()
        i = Image({ pos: self.next_val(pos, enhancement) for pos in product(ys, xs)}, '0')
        print(str(i))
        return i


def read_image(f):
    return Image({ (row_i, col_i): '1' if val == '#' else '0'
                   for row_i, row in enumerate(f) 
                   for col_i, val in enumerate(row.strip()) }, '0')

def part_01(image, enhancement):
    return sum(map(int, image.enhance(enhancement).enhance(enhancement).values()))

with open(FILENAME) as f:
    enhancement = [ '1' if val == '#' else '0' for val in next(f).strip() ]
    next(f)
    f = list(f)
    image = read_image(f)
    print(str(image))

    print(part_01(image, enhancement))
