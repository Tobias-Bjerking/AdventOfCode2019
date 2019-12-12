import GetInput
import time
import winsound
from math import gcd

values = GetInput.get_list("../Input/Day12.txt")
moons = []
velocity = []


def initialize():
    global moons, velocity
    moons = []
    velocity = []
    for moon in values:
        split = moon.split(">")[0]
        split = split.split(",")
        coords = []
        for coord in split:
            coords.append(int(coord.split("=")[1]))
        moons.append(coords)
        velocity.append([0,0,0])


def step():
    for moon in range(len(moons)):
        for other_moon in moons:
            if moons[moon] != other_moon:
                for i in range(3):
                    if moons[moon][i] < other_moon[i]:
                        velocity[moon][i] = velocity[moon][i] + 1
                    elif moons[moon][i] > other_moon[i]:
                        velocity[moon][i] = velocity[moon][i] - 1
    for moon in range(len(moons)):
        for coord in range(len(moons[moon])):
            moons[moon][coord] = moons[moon][coord] + velocity[moon][coord]


def part_one():
    initialize()
    for i in range(1000):
        step()
    total_energy = 0
    for moon in range(len(moons)):
        pot_energy = kin_energy = 0
        for coord in range(len(moons[moon])):
            pot_energy += abs(moons[moon][coord])
            kin_energy += abs(velocity[moon][coord])
        total_energy += pot_energy * kin_energy
    return total_energy


def lcm(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def part_two():
    initialize()
    initial_state_x = []
    initial_state_y = []
    initial_state_z = []
    for moon in range(len(moons)):
        initial_state_x.append((moons[moon][0], velocity[moon][0]))
        initial_state_y.append((moons[moon][1], velocity[moon][1]))
        initial_state_z.append((moons[moon][2], velocity[moon][2]))
    steps = x_steps = y_steps = z_steps = 0
    while x_steps == 0 or y_steps == 0 or z_steps == 0:
        step()
        steps += 1
        new_state_x = []
        new_state_y = []
        new_state_z = []
        for moon in range(len(moons)):
            new_state_x.append((moons[moon][0], velocity[moon][0]))
            new_state_y.append((moons[moon][1], velocity[moon][1]))
            new_state_z.append((moons[moon][2], velocity[moon][2]))
            if initial_state_x == new_state_x and x_steps == 0:
                x_steps = steps
            if initial_state_y == new_state_y and y_steps == 0:
                y_steps = steps
            if initial_state_z == new_state_z and z_steps == 0:
                z_steps = steps
    return lcm([x_steps, y_steps, z_steps])


print("Part 1:", part_one())
start_time = time.time()
print("Part 2:", part_two())
print(time.time() - start_time)
