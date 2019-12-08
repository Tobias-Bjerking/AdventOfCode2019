import GetInput
import sys

values = GetInput.get_list("../Input/Day8.txt")[0]
width, height = 25, 6
size = width * height

layers = []
color = {0: "█", 1: "░", 2: " "}

for i in range(len(values) // size):
    layers.append(values[i * size:(i + 1) * size])


def part_two():
    image = ''
    for pixel in range(size):
        c = 2
        for layer in layers:
            if int(layer[pixel]) in [0, 1]:
                c = int(layer[pixel])
                break
        image += color[c]
    for h in range(height):
        print(image[h*width:(h+1)*width])


def part_one():
    lowest_number_of_zeros = sys.maxsize
    total = -1
    for layer in layers:
        if layer.count("0") < lowest_number_of_zeros:
            lowest_number_of_zeros = layer.count("0")
            total = layer.count("1") * layer.count("2")
    return total


print("Part 1:", part_one())
print("Part 2:")
part_two()
