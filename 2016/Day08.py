import sys
import re
import numpy as np

strips: list[tuple[str, int, int]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        a, b = map(int, re.findall(r"\d+", line))
        inst = [w for w in list(re.findall(r"[a-z]+", line)) if w in ["rect", "row", "column"]][0]
        strips.append((inst, a, b))

grid = np.zeros((6, 50), dtype=bool)
for (op, a, b) in strips:
    if op == "rect":
        grid[:b, :a] = True
    elif op == "row":
        grid[a, :] = np.roll(grid[a, :], b)
    else:
        grid[:, a] = np.roll(grid[:, a], b)

print(f"Part 1: {grid.sum()}")
for row in grid:
    print("".join("#" if cell else "." for cell in row))