import GetInput
import math

values = GetInput.get_list("../Input/Day10.txt")
asteroids = []
for line in range(len(values)):
    for point in range(len(values[line])):
        if values[line][point] == "#":
            asteroids.append((point, line))


def vector_subtraction(x, y):
    v = []
    for i in range(len(x)):
        v.append(x[i] - y[i])
    return tuple(v)


def euclidean_distance(x, y=(0, 0)):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))


def dot_product(x, y=(0,0)):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def angle_between_vectors(x, y=(0,0)):
    return math.degrees(math.acos(dot_product(x, y)/(euclidean_distance(x) * euclidean_distance(y))))

def angle_from_vector(x, y=(0,0)):
    v = vector_subtraction(x, y)
    return math.degrees(math.atan2(v[0],v[1]))


def part_one():
    best_number_of_asteroids = 0
    best_asteroid = (0,0)
    for current_asteroid in asteroids:
        degrees = {0}
        for comp_asteroid in asteroids:
            angle = angle_from_vector(current_asteroid, comp_asteroid)
            degrees.add(angle)
        if len(degrees) > best_number_of_asteroids:
            best_number_of_asteroids = len(degrees)
            best_asteroid = current_asteroid
    return best_asteroid, best_number_of_asteroids

print(part_one())