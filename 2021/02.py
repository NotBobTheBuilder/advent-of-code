FILENAME = '02-input.txt'

def move_01(current, cmd):
    current_horizontal, current_depth = current
    direction, magnitude_str = cmd.split(' ')
    magnitude = int(magnitude_str)

    if direction == 'forward':
        return (current_horizontal + magnitude, current_depth)
    if direction == 'down':
        return (current_horizontal, current_depth + magnitude) 
    if direction == 'up':
        return (current_horizontal, current_depth - magnitude)

    raise Exception()

def part_01():
    with open(FILENAME) as commands:
        position = (0, 0)
        for command in commands:
            position = move_01(position, command)
    
        return position[0] * position[1]

def move_02(current, cmd):
    horizontal, aim, depth = current
    direction, magnitude_str = cmd.split(' ')
    magnitude = int(magnitude_str)

    if direction == 'forward':
        return (horizontal + magnitude, aim, depth + aim * magnitude)
    if direction == 'down':
        return (horizontal, aim + magnitude, depth)
    if direction == 'up':
        return (horizontal, aim - magnitude, depth)

def part_02():
    with open(FILENAME) as commands:
        position = (0,0,0)
        for command in commands:
            position = move_02(position, command)

        return position[0] * position[2]

print(part_02())
