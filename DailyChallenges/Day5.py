import GetInput

#memory = [11001, 4, 1, 3, 99, 1, 1, 1, 1, 1]
memory = GetInput.get_numbered_line("../Input/Day5.txt")
pointer = 0


def addition():
    global pointer
    operation = get_operations(memory[pointer])
    memory[get_value(3, operation[4])] = memory[get_value(1, operation[2])] + memory[get_value(2, operation[3])]
    pointer = pointer + 4


def multiplication():
    global pointer
    operation = get_operations(memory[pointer])
    memory[get_value(3, operation[4])] = memory[get_value(1, operation[2])] * memory[get_value(2, operation[3])]
    pointer = pointer + 4


def get_operations(operation):
    operation = reverse_integer(operation)
    while len(operation) < 5:
        operation += "0"
    return operation


def reverse_integer(number):
    return str(number)[::-1]


def get_value(step, instruction):
    if int(instruction) == 1:
        return pointer+step
    return memory[pointer+step]


def switch(operation):
    if operation == 1:
        addition()
    elif operation == 2:
        multiplication()
    else: print("ERROR!")


def read_instruction():
    while memory[pointer] != 99:
        switch(int(reverse_integer(memory[pointer])[0]))
    print(memory)


read_instruction()
