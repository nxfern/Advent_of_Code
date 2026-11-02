import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    prog = Computer(list(map(int, f.read().split(","))))

inputs: list[int] = []
while True:
    outputs: list[int] = []
    while (out := prog.run(inputs=inputs, feedback=True)) is not None:
        outputs.append(out)
    print("".join(map(chr, outputs)), end="")
    
    if prog.halted:
        break
    inputs = [ord(c) for c in input()] + [10]