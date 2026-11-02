import sys
import re
from collections import defaultdict, deque

with open(sys.argv[1]) as f:
    sample, manual = f.read().split("\n\n\n\n")
    sample = [[tuple(map(int, re.findall(r'-?\d+', s))) for s in line.splitlines()] for line in sample.split("\n\n")]
    manual = [tuple(map(int, line.split())) for line in manual.splitlines()]

ops = {
    'addr': lambda regs, a, b: regs[a] + regs[b],
    'addi': lambda regs, a, b: regs[a] + b,
    'mulr': lambda regs, a, b: regs[a] * regs[b],
    'muli': lambda regs, a, b: regs[a] * b,
    'banr': lambda regs, a, b: regs[a] & regs[b],
    'bani': lambda regs, a, b: regs[a] & b,
    'borr': lambda regs, a, b: regs[a] | regs[b],
    'bori': lambda regs, a, b: regs[a] | b,
    'setr': lambda regs, a, b: regs[a],
    'seti': lambda regs, a, b: a,
    'gtir': lambda regs, a, b: 1 if a > regs[b] else 0,
    'gtri': lambda regs, a, b: 1 if regs[a] > b else 0,
    'gtrr': lambda regs, a, b: 1 if regs[a] > regs[b] else 0,
    'eqir': lambda regs, a, b: 1 if a == regs[b] else 0,
    'eqri': lambda regs, a, b: 1 if regs[a] == b else 0,
    'eqrr': lambda regs, a, b: 1 if regs[a] == regs[b] else 0,
}

part1 = 0
possible: defaultdict[int, set[str]] = defaultdict(lambda: set(ops.keys()))
for (before, (code, a, b, c), after) in sample:
    correct = 0
    for op in ops:
        if ops[op](before, a, b) == after[c]:
            correct += 1
        else:
            possible[code].discard(op)
    part1 += 1 if correct >= 3 else 0

print(f"Part 1: {part1}")

mapped: dict[int, str] = {}
queue = deque(code for code, candidates in possible.items() if len(candidates) == 1)
while queue:
    code = queue.popleft()
    if not possible[code]:
        continue
    op = possible[code].pop()
    mapped[code] = op
    for other_code, candidates in possible.items():
        if op in candidates:
            candidates.discard(op)
            if len(candidates) == 1:
                queue.append(other_code)

regs = [0, 0, 0, 0]
for (code, a, b, c) in manual:
    regs[c] = ops[mapped[code]](regs, a, b)

print(f"Part 2: {regs[0]}")