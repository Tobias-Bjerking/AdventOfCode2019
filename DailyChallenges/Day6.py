import GetInput


orbits = GetInput.get_map("../Input/Day6.txt", ")")


def get_number_of_orbits():
    return __traverse_tree("COM", -1)


def __traverse_tree(node, depth):
    if node not in orbits.keys():
        return depth + 1
    else:
        satelites_total = 0
        for satelite in orbits[node]:
            satelites_total += __traverse_tree(satelite, depth + 1)
        return satelites_total + depth + 1


print(get_number_of_orbits())
