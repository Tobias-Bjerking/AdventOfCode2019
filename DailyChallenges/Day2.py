import GetInput
goal = 19690720


def instruction(noun: int, verb: int) -> int:
    memory = GetInput.get_numbered_line("../Input/Day2.txt")
    memory[1] = noun
    memory[2] = verb
    pointer = 0
    while memory[pointer] != 99:
        if memory[pointer] == 1:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
        elif memory[pointer] == 2:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
        pointer += 4
    return memory[0]


print(instruction(12, 2))
