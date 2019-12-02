import GetInput


def loop(values):
    operators = values
    for operator in range(0, len(operators), 4):
        if operators[operator] == 1:
            operators[operators[operator + 3]] = operators[operators[operator + 1]] + operators[operators[operator + 2]]
        elif operators[operator] == 2:
            operators[operators[operator + 3]] = operators[operators[operator + 1]] * operators[operators[operator + 2]]
        elif operators[operator] == 99:
            print("DONE!")
            return operators
        else:
            print("ERROR!")
    print("loop finished")
    return operators


values = GetInput.get_numbered_line("../Input/Day2.txt")
values[1] = 12
values[2] = 2
test = [1,9,10,3,2,3,11,0,99,30,40,50]
print(loop(values))