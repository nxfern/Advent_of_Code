import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def spring(data: list[int], inputs: list[int]) -> int:
    prog = Computer(data)
    while not prog.halted:
        if (out := prog.run(inputs=inputs)) and out > 255:
            return out
    return -1

script1 = [ord(c) for c in "\n".join(["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J", "WALK"]) + "\n"]
print(f"Part 1: {spring(data, inputs=script1)}")

script2 = [ord(c) for c in "\n".join(["NOT A J","NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J",
                                      "NOT E T", "NOT T T", "OR H T", "AND T J", "RUN"]) + "\n"]
print(f"Part 2: {spring(data, inputs=script2)}")