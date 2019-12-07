import IntcodeComputer
import GetInput
import sys
from itertools import permutations

program = GetInput.get_numbered_line("../Input/Day7.txt")


def part_two():
    highest_signal = -1
    amp_settings = permutations(range(5, 10))
    for setting in amp_settings:
        amp_a = IntcodeComputer.IntcodeComputer(program, setting[0])
        amp_b = IntcodeComputer.IntcodeComputer(program, setting[1])
        amp_c = IntcodeComputer.IntcodeComputer(program, setting[2])
        amp_d = IntcodeComputer.IntcodeComputer(program, setting[3])
        amp_e = IntcodeComputer.IntcodeComputer(program, setting[4])

        amps = [amp_e, amp_d, amp_c, amp_b, amp_a]
        amp_input = 0
        result = -1
        while amp_input is not None:
            for amp in amps:
                amp.give_input(amp_input)
                amp_input = amp.run()
            if amp_input is not None:
                result = amp_input
        highest_signal = max(highest_signal, result)

    return highest_signal


def part_one():
    highest_signal = 0
    amp_settings = permutations(range(5))
    for setting in amp_settings:
        amp_a = IntcodeComputer.IntcodeComputer(program, setting[0])
        amp_b = IntcodeComputer.IntcodeComputer(program, setting[1])
        amp_c = IntcodeComputer.IntcodeComputer(program, setting[2])
        amp_d = IntcodeComputer.IntcodeComputer(program, setting[3])
        amp_e = IntcodeComputer.IntcodeComputer(program, [setting[4], 0])

        amp_d.give_input(amp_e.run())
        amp_c.give_input(amp_d.run())
        amp_b.give_input(amp_c.run())
        amp_a.give_input(amp_b.run())
        highest_signal = max(highest_signal, amp_a.run())
    return highest_signal


print("Part 1:", part_one())
print("Part 2:", part_two())
