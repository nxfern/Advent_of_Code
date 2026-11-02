import sys
from itertools import chain

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    ip = int(lines[0].split()[1])
    instructions = lines[1:]

regs = {r: 0 for r in range(6)}
ops = {
    'addr': lambda r, a, b: r[a] + r[b],
    'addi': lambda r, a, b: r[a] + b,
    'mulr': lambda r, a, b: r[a] * r[b],
    'muli': lambda r, a, b: r[a] * b,
    'setr': lambda r, a, b: r[a],
    'seti': lambda r, a, b: a,
    'gtrr': lambda r, a, b: 1 if r[a] > r[b] else 0,
    'eqrr': lambda r, a, b: 1 if r[a] == r[b] else 0
}

pc = 0
while 0 <= pc < len(instructions):
    regs[ip] = pc
    op, *abc = instructions[pc].split()
    a, b, c = map(int, abc)
    regs[c] = ops[op](regs, a, b)
    pc = regs[ip] + 1

print(f"Part 1: {regs[0]}")

n = 10551389    # Found by reverse engineering my input
part2 = sum(set(chain.from_iterable((i, n // i) for i in range(1, int(n**0.5) + 1) if not n % i)))
print(f"Part 2: {part2}")