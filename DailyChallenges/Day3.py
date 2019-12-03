import GetInput
import sys


def manhattan_distance(point_a, point_b):
    return abs(point_a[0] - (point_b[0])) + abs(point_a[1] - (point_b[1]))


def draw_wire(wires):
    paths = []
    dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    for wire in wires:
        x = y = 0
        path = set()
        for direction in wire:
            direct, dist = direction[0], int(direction[1:])
            dist_x, dist_y = dirs[direct]
            for i in range(dist):
                x += dist_x
                y += dist_y
                path.update([(x, y)])
        paths.append(path)
    return paths


def find_closest_intersection_manhattan(intersections):
    min_dist = sys.maxsize
    for x in intersections:
        min_dist = min(min_dist, manhattan_distance((0,0), x))
    return min_dist


def find_closest_intersection_length(wires, intersections):
    dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    length = {0:{},1:{}}
    iter = 0
    for wire in wires:
        x = y = steps = 0
        for direction in wire:
            direct, dist = direction[0], int(direction[1:])
            dist_x, dist_y = dirs[direct]
            for i in range(dist):
                steps += 1
                x += dist_x
                y += dist_y
                length[iter][(x,y)] = steps
        iter+=1

    min_dist = sys.maxsize
    for cross in intersections:
        min_dist = min(min_dist, length[0][cross] + length[1][cross])
    return min_dist


values = GetInput.get_line("../Input/Day3.txt")
paths = draw_wire(values)
intersections = paths[0] & paths[1]
print("Closest intersection manhattan:", find_closest_intersection_manhattan(intersections))
print("Closest intersection length:",find_closest_intersection_length(values, intersections))
