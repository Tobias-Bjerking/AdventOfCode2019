import GetInput
import sys
from itertools import permutations

program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
program = GetInput.get_numbered_line("../Input/Day7.txt")
memory = program.copy()
pointer = 0


def addition():
    global pointer
    memory[get_value(3)] = memory[get_value(1)] + memory[get_value(2)]
    pointer += 4


def multiplication():
    global pointer
    memory[get_value(3)] = memory[get_value(1)] * memory[get_value(2)]
    pointer += 4


def save(user_input="NaN"):
    global pointer
    if user_input == "NaN":
        memory[memory[pointer + 1]] = int(input(">"))
    else:
        memory[memory[pointer + 1]] = user_input
    pointer += 2


def output():
    global pointer
    pointer += 2
    return memory[get_value(1, pointer-2)]


def jump_if_true():
    global pointer
    if memory[get_value(1)] != 0:
        pointer = memory[get_value(2)]
    else:
        pointer += 3


def jump_if_false():
    global pointer
    if memory[get_value(1)] == 0:
        pointer = memory[get_value(2)]
    else:
        pointer += 3


def less_than():
    global pointer
    if memory[get_value(1)] < memory[get_value(2)]:
        memory[get_value(3)] = 1
    else:
        memory[get_value(3)] = 0
    pointer += 4


def equals():
    global pointer
    if memory[get_value(1)] == memory[get_value(2)]:
        memory[get_value(3)] = 1
    else:
        memory[get_value(3)] = 0
    pointer += 4


def get_operations(operation):
    operation = reverse_integer(operation)
    while len(operation) < 5:
        operation += "0"
    return operation


def reverse_integer(number):
    return str(number)[::-1]


def get_value(step, point="NaN"):
    if point =="NaN":
        point = pointer
    instruction = get_operations(memory[point])[step + 1]
    if int(instruction) == 1:
        return point + step
    return memory[point + step]


def switch(operation, param="NaN"):
    if operation == 1:
        addition()
    elif operation == 2:
        multiplication()
    elif operation == 3:
        if param != "NaN":
            save(param)
        else:
            save()
    elif operation == 4:
        return output()
    elif operation == 5:
        jump_if_true()
    elif operation == 6:
        jump_if_false()
    elif operation == 7:
        less_than()
    elif operation == 8:
        equals()
    else:
        print("ERROR!")


def amplifier(user_input, phase):
    global memory
    global pointer
    memory = program.copy()
    pointer = 0
    amp_out = -1
    write = phase
    while memory[pointer] != 99:
        amp_out = switch(int(reverse_integer(memory[pointer])[0]), write)
        write = user_input
    return amp_out


highest_signal = 0
amp_settings = permutations(range(5))
for setting in amp_settings:
    out = amplifier(amplifier(amplifier(amplifier(amplifier(0, setting[0]), setting[1]), setting[2]), setting[3]), setting[4])
    highest_signal = max(highest_signal, out)
print(highest_signal)
