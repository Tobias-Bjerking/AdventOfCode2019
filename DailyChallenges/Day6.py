import GetInput


orbits = GetInput.get_map("../Input/Day6.txt", ")")


def get_number_of_orbits():
    return __traverse_tree("COM", -1)


def __traverse_tree(node, depth):
    if node not in orbits.keys():
        return depth + 1
    else:
        satellites_total = 0
        for satellite in orbits[node]:
            satellites_total += __traverse_tree(satellite, depth + 1)
        return satellites_total + depth + 1


def get_orbit(val):
    for key, value in orbits.items():
        if val in value:
            return key


def get_all_satellites(node):
    orbiting_satellites = []
    if node in orbits.keys():
        for satellite in orbits[node]:
            orbiting_satellites.append(satellite)
            orbitals = get_all_satellites(satellite)
            for x in orbitals:
                orbiting_satellites.append(x)
    return orbiting_satellites


def __shared_orbit(node):
    orbiting = get_orbit(node)
    satellites = get_all_satellites(orbiting)
    if "YOU" in satellites and "SAN" in satellites:
        return orbiting
    else:
        return __shared_orbit(orbiting)

def shared_orbit():
    return __shared_orbit("YOU")


def __calculate_distance(node, search):
    for satellite in orbits[node]:
        all_satellites = get_all_satellites(satellite)
        if search in all_satellites:
            return __calculate_distance(satellite, search) + 1
    return 0


def calculate_distance():
    shared = shared_orbit()
    total = __calculate_distance(shared, "YOU")
    return total + __calculate_distance(shared, "SAN")


print("Part 1:", get_number_of_orbits())
print("Part 2:", calculate_distance())
