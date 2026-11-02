import sys, math

with open(sys.argv[1]) as f:
    *rows, ops = f.read().splitlines()

width = max(map(len, rows + [ops]))
rows = [r.ljust(width) for r in rows]
ops = ops.ljust(width)

starts = [i for i, ch in enumerate(ops) if ch in "+*"]
ends = starts[1:] + [width + 1]

cephs = [[r[s:e - 1] for r in rows] for s, e in zip(starts, ends)]
ops = ops.split()

def solve(nums, o):
    return sum(nums) if o == "+" else math.prod(nums)

print("Part 1:", sum(solve(list(map(int, c)), o) for c, o in zip(cephs, ops)))
print("Part 2:", sum(solve([int("".join(col)) for col in zip(*c)], o) for c, o in zip(cephs, ops)))