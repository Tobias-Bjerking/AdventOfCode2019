class IntcodeComputer:
    def __init__(self, program, input_func=None):
        self.memory = program.copy()
        self.pointer = 0
        self.rel_base = 0
        self.sim_input = []
        self.input_func = input_func

        for i in range(10000):
            self.memory.append(0)

    def run(self, sim_input=None):
        opcode = int(str(self.memory[self.pointer])[-2:])
        out = None
        if sim_input is not None:
            for i in sim_input:
                self.sim_input.append(i)
        while opcode != 99:
            out = self.__opcode(opcode)
            if out is not None:
                return out
            opcode = int(str(self.memory[self.pointer])[-2:])

    def __get_param(self, parameter, param):
        return self.memory[self.__get_param_address(parameter, param)]

    def __set_param(self, parameter, param, value):
        self.memory[self.__get_param_address(parameter, param)] = value

    def __get_param_address(self, parameter, param):
        param_type = 0
        try:
            param_type = int(parameter[-param])
        except:
            pass
        if param_type == 0:
            return self.memory[self.pointer + param]
        elif param_type == 1:
            return self.pointer + param
        elif param_type == 2:
            offset = self.memory[self.pointer + param]
            return self.rel_base + offset
        else:
            print('Param type error')
            return 0

    def __addition(self, parameter):
        self.__set_param(parameter, 3, self.__get_param(parameter, 1) + self.__get_param(parameter, 2))
        self.pointer += 4

    def __multiplication(self, parameter):
        self.__set_param(parameter, 3, self.__get_param(parameter, 1) * self.__get_param(parameter, 2))
        self.pointer += 4

    def __input(self, parameter):
        if self.input_func is not None:
            self.__set_param(parameter, 1, self.input_func())
        else:
            if len(self.sim_input) > 0:
                inp = self.sim_input.pop(0)
                self.__set_param(parameter, 1, inp)
            else:
                self.__set_param(parameter, 1, int(input(">")))
        self.pointer += 2

    def __output(self, parameter):
        out = self.__get_param(parameter, 1)
        self.pointer += 2
        return out

    def __jump_if_true(self, parameter):
        if self.__get_param(parameter, 1) != 0:
            self.pointer = self.__get_param(parameter, 2)
        else:
            self.pointer += 3

    def __jump_if_false(self, parameter):
        if self.__get_param(parameter, 1) == 0:
            self.pointer = self.__get_param(parameter, 2)
        else:
            self.pointer += 3

    def __less_than(self, parameter):
        if self.__get_param(parameter, 1) < self.__get_param(parameter, 2):
            self.__set_param(parameter, 3, 1)
        else:
            self.__set_param(parameter, 3, 0)
        self.pointer += 4

    def __equals(self, parameter):
        if self.__get_param(parameter, 1) == self.__get_param(parameter, 2):
            self.__set_param(parameter, 3, 1)
        else:
            self.__set_param(parameter, 3, 0)
        self.pointer += 4

    def __set_relative_base(self, parameter):
        self.rel_base += self.__get_param(parameter, 1)
        self.pointer += 2

    def __opcode(self, opcode):
        parameter = str(self.memory[self.pointer])[:-2]
        if opcode == 1:
            self.__addition(parameter)
        elif opcode == 2:
            self.__multiplication(parameter)
        elif opcode == 3:
            self.__input(parameter)
        elif opcode == 4:
            return self.__output(parameter)
        elif opcode == 5:
            self.__jump_if_true(parameter)
        elif opcode == 6:
            self.__jump_if_false(parameter)
        elif opcode == 7:
            self.__less_than(parameter)
        elif opcode == 8:
            self.__equals(parameter)
        elif opcode == 9:
            self.__set_relative_base(parameter)
        else:
            print("Error!")