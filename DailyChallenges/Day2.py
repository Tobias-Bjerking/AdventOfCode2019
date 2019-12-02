import GetInput


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


def get_target_noun_and_verb(goal: int) -> int:
    for i in range(100):
        for j in range(100):
            if instruction(i, j) == goal:
                return i, j


print(instruction(12, 2))
result = get_target_noun_and_verb(19690720)
print((100 * result[0]) + result[1])
