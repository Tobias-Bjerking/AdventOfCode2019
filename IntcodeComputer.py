class IntcodeComputer:

    def __init__(self, intcode: list, simulated_input=[]):
        self.program = intcode
        self.memory = self.program
        self.pointer = 0
        if isinstance(simulated_input,list):
            self.sim_input = simulated_input
        else:
            self.sim_input = [simulated_input]

    def run(self):
        out = None
        while self.memory[self.pointer] != 99:
            out = self.switch(int(self.reverse_integer(self.memory[self.pointer])[0]))
            if out != None:
                return out


    def give_input(self, simulated_input):
        self.sim_input.append(simulated_input)

    def addition(self):
        self.memory[self.get_value(3)]= self.memory[self.get_value(1)] + self.memory[self.get_value(2)]
        self.pointer += 4


    def multiplication(self):
        self.memory[self.get_value(3)] = self.memory[self.get_value(1)] * self.memory[self.get_value(2)]
        self.pointer += 4


    def save(self, user_input="NaN"):
        if len(self.sim_input) < 1:
            self.memory[self.memory[self.pointer + 1]] = int(input(">"))
        else:
            self.memory[self.memory[self.pointer + 1]] = self.sim_input.pop(0)
        self.pointer += 2


    def output(self):
        self.pointer += 2
        return self.memory[self.get_value(1, self.pointer-2)]


    def jump_if_true(self):
        if self.memory[self.get_value(1)] != 0:
            self.pointer = self.memory[self.get_value(2)]
        else:
            self.pointer += 3


    def jump_if_false(self):
        if self.memory[self.get_value(1)] == 0:
            self.pointer = self.memory[self.get_value(2)]
        else:
            self.pointer += 3


    def less_than(self):
        if self.memory[self.get_value(1)] < self.memory[self.get_value(2)]:
            self.memory[self.get_value(3)] = 1
        else:
            self.memory[self.get_value(3)] = 0
        self.pointer += 4


    def equals(self):
        if self.memory[self.get_value(1)] == self.memory[self.get_value(2)]:
            self.memory[self.get_value(3)] = 1
        else:
            self.memory[self.get_value(3)] = 0
        self.pointer += 4


    def get_operations(self, operation):
        operation = self.reverse_integer(operation)
        while len(operation) < 5:
            operation += "0"
        return operation


    def reverse_integer(self, number):
        return str(number)[::-1]


    def get_value(self, step, point="NaN"):
        if point =="NaN":
            point = self.pointer
        instruction = self.get_operations(self.memory[point])[step + 1]
        if int(instruction) == 1:
            return point + step
        return self.memory[point + step]


    def switch(self, operation):
        if operation == 1:
            self.addition()
        elif operation == 2:
            self.multiplication()
        elif operation == 3:
            self.save()
        elif operation == 4:
            return self.output()
        elif operation == 5:
            self.jump_if_true()
        elif operation == 6:
            self.jump_if_false()
        elif operation == 7:
            self.less_than()
        elif operation == 8:
            self.equals()
        else:
            print("ERROR!")