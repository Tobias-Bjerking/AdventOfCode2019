import GetInput

values = GetInput.get_list("../Input/Day12.txt")
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

print("Part 1:", part_one())