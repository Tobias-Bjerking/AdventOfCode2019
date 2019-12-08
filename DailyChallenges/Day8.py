import GetInput
import sys

values = GetInput.get_list("../Input/Day8.txt")[0]
width, height = 25, 6
size = width*height

layers = []

for i in range(len(values)//size):
    layers.append(values[i*size:(i+1)*size])

lowest_number_of_zeros = sys.maxsize
total = -1
for layer in layers:
    if layer.count("0") < lowest_number_of_zeros:
        lowest_number_of_zeros = layer.count("0")
        total = layer.count("1") * layer.count("2")
print(total)
