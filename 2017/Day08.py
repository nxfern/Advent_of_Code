import sys
from collections import defaultdict

OPS = {
    "inc": lambda regs, r1, x: regs[r1] + x,
    "dec": lambda regs, r1, x: regs[r1] - x,
}

CONDS = {
    ">": lambda regs, r2, y: regs[r2] > y,
    ">=": lambda regs, r2, y: regs[r2] >= y,
    "<": lambda regs, r2, y: regs[r2] < y,
    "<=": lambda regs, r2, y: regs[r2] <= y,
    "==": lambda regs, r2, y: regs[r2] == y,
    "!=": lambda regs, r2, y: regs[r2] != y, 
}

with open(sys.argv[1]) as f:
    instructions = [line.split() for line in f.read().splitlines()]

regs: defaultdict[str, int] = defaultdict(int)
part2 = 0
for r1, op, x, _, r2, c, y in instructions:
    regs[r1] = OPS[op](regs, r1, int(x)) if CONDS[c](regs, r2, int(y)) else regs[r1]
    part2 = max(part2, max(regs.values()))

print(f"Part 1: {max(regs.values())}")
print(f"Part 2: {part2}")