import GetInput
import IntcodeComputer


values = [104,1337,99]
values = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] # prints itself
values = [1102,34915192,34915192,7,4,7,99,0] # prints 16-digit number
values = [104,1125899906842624,99] # prints 1125899906842624
values = GetInput.get_numbered_line("../Input/Day9.txt")


comp = IntcodeComputer.IntcodeComputer(values)
out = comp.run()
while out is not None:
    print(str(out))
    out = comp.run()
