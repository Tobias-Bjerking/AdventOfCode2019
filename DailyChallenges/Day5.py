import GetInput

memory = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
memory = GetInput.get_numbered_line("../Input/Day5.txt")
pointer = 0

def addition():
    global pointer
    memory[get_value(3)] = memory[get_value(1)] + memory[get_value(2)]
    pointer += 4


def multiplication():
    global pointer
    memory[get_value(3)] = memory[get_value(1)] * memory[get_value(2)]
    pointer += 4


def save():
    global pointer
    memory[memory[pointer + 1]] = 5
    pointer += 2


def output():
    global pointer
    print(memory[get_value(1)])
    pointer += 2


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


def get_value(step):
    instruction = get_operations(memory[pointer])[step+1]
    if int(instruction) == 1:
        return pointer + step
    return memory[pointer + step]


def switch(operation):
    if operation == 1:
        addition()
    elif operation == 2:
        multiplication()
    elif operation == 3:
        save()
    elif operation == 4:
        output()
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


while memory[pointer] != 99:
    switch(int(reverse_integer(memory[pointer])[0]))