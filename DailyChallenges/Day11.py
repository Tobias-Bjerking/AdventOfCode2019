import IntcodeComputer
import GetInput
import sys

program = GetInput.get_numbered_line("../Input/Day11.txt")
comp = IntcodeComputer.IntcodeComputer(program)
DIRECTIONS = {0: "UP", 1: "LEFT", 2: "DOWN", 3: "RIGHT"}
dir = "UP"
location = (0, 0)
matrix = {}


# function to return key for any value
def get_key(val):
    for key, value in DIRECTIONS.items():
        if val == value:
            return key
    return "key doesn't exist"


def paint(color):
    matrix[location] = color


def new_dir(turn):
    global dir
    dir = DIRECTIONS[(get_key(dir) + (turn * 2) + 1) % 4]


def move(turn):
    global location, dir
    new_dir(turn)
    if dir == "UP":
        location = (location[0], location[1] - 1)
    elif dir == "LEFT":
        location = (location[0] - 1, location[1])
    elif dir == "DOWN":
        location = (location[0], location[1] + 1)
    elif dir == "RIGHT":
        location = (location[0] + 1, location[1])
    else:
        print("MOVE ERROR")


def part_one():
    out = comp.run([1])
    while out is not None:
        paint(out)
        out = comp.run()
        move(out)
        if location in matrix:
            out = comp.run([matrix[location]])
        else:
            out = comp.run([0])
    return len(matrix)


def get_width():
    high_x = 0
    low_x = sys.maxsize
    for key in matrix:
        high_x = max(high_x, key[0])
        low_x = min(low_x, key[0])
    return high_x + abs(low_x), abs(low_x)


def get_height():
    high_y = 0
    low_y = sys.maxsize
    for key in matrix:
        high_y = max(high_y, key[1])
        low_y = min(low_y, key[1])
    return high_y + abs(low_y), abs(low_y)


def part_two():
    color = {0: "█", 1: "░"}
    width, x_offset = get_width()
    height, y_offset = get_height()
    new_matrix = {}
    for key in matrix:
        new_matrix[(key[0]+x_offset, key[1]+y_offset)] = matrix[key]
    for h in range(height+1):
        for w in range(width+1):
            if (w, h) in new_matrix:
                print(color[new_matrix[(w, h)]], end="")
            else:
                print(color[0], end="")
        print("")


print("Part 1:", part_one())
print("Part 2:")
part_two()
