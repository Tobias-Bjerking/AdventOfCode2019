import GetInput
import IntcodeComputer
import sys

color = {0: " ", 1: "█", 2: "░", 3: "_", 4: "O"}
program = GetInput.get_numbered_line("../Input/Day13.txt")
screen = {}
ball_dir = 0
ball_pos = (0, 0)


def get_width():
    high_x = 0
    for key in screen:
        high_x = max(high_x, key[0])
    return high_x


def get_height():
    high_y = 0
    for key in screen:
        high_y = max(high_y, key[1])
    return high_y


def print_screen():
    width= get_width()
    height = get_height()
    if (-1,0) in screen.keys():
        print("Points:",screen[(-1,0)])
    for h in range(height+1):
        for w in range(width+1):
            if (w, h) in screen:
                print(color[screen[(w, h)]], end="")
        print("")


def calculate_input():
    ball = paddle = None
    for key in screen.keys():
        if screen[key] == 4:
            ball = key
        elif screen[key] == 3:
            paddle = key
    if ball is not None and paddle is not None:
        if ball[0] > paddle[0]:
            return 1
        elif ball[0] < paddle[0]:
            return -1
        else:
            return 0

comp = IntcodeComputer.IntcodeComputer(program, calculate_input)
x_coord = comp.run()
y_coord = comp.run()
block_type = comp.run()
while x_coord is not None and y_coord is not None and block_type is not None:
    screen[(x_coord, y_coord)] = block_type
    x_coord, y_coord, block_type = [comp.run() for _ in range(3)]
    print_screen()
    i = calculate_input()
    if i is not None:
        inp = i
