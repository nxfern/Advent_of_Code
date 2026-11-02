import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def alarm(noun: int|None=None, verb: int|None=None) -> int:
    prog = Computer(data)
    prog.mem[1] = noun if noun is not None else prog.mem[1]
    prog.mem[2] = verb if verb is not None else prog.mem[2]
    for i in range(0, len(prog.mem), 4):
        op, a, b, c = [prog.mem[i+j] for j in range(4)]
        if op == 99:
            return prog.mem[0]
        prog.mem[c] = Computer.OPS[op](prog.mem[a], prog.mem[b])
    return prog.mem[0]  # unlikely to be correct if triggered

part1 = part2 = None
for noun in range(100):
    for verb in range(100):
        result = alarm(noun=noun, verb=verb)
        if (noun, verb) == (12, 2):
            part1 = result
        if result == 19_690_720:
            part2 = 100 * noun + verb
        if part1 is not None and part2 is not None:
            break
    
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")