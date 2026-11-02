import sys
import numpy as np

def shift(grid, i, j):
    rolled = np.roll(np.roll(grid, i, axis=0), j, axis=1)
    if i == 1:  rolled[0, :] = False
    if i == -1: rolled[-1, :] = False
    if j == 1:  rolled[:, 0] = False
    if j == -1: rolled[:, -1] = False
    return rolled

with open(sys.argv[1]) as f:
    part1 = np.array([[c == "#" for c in line] for line in f.read().splitlines()], dtype=bool)

part2 = part1.copy()
part2[[0, 0, -1, -1], [0, -1, 0, -1]] = True
for _ in range(100):
    n1 = sum(shift(part1, i, j)
             for i in [-1, 0, 1]
             for j in [-1, 0, 1]
             if not (i == 0 and j == 0))
    n2 = sum(shift(part2, i, j)
             for i in [-1, 0, 1]
             for j in [-1, 0, 1]
             if not (i == 0 and j == 0))

    part1 = (n1 == 3) | (part1 & (n1 == 2))
    part2 = (n2 == 3) | (part2 & (n2 == 2))
    part2[[0, 0, -1, -1], [0, -1, 0, -1]] = True

print(f"Part 1: {part1.sum()}")
print(f"Part 2: {part2.sum()}")