import sys
import numpy as np

with open(sys.argv[1]) as f:
    SERIAL = int(f.read())

xs, ys = np.arange(301), np.arange(301)
rack = xs[:, None] + 10
power = (rack * ys[None, :] + SERIAL) * rack // 100 % 10 - 5
power[0, :] = power[:, 0] = 0
grid = power.cumsum(axis=0).cumsum(axis=1)  # 2d prefix sum

def sum_size(size):
    totals = (grid[size:, size:] - grid[size:, :-size] 
                                 - grid[:-size, size:] + grid[:-size, :-size])
    idx = np.argmax(totals)
    x, y = np.unravel_index(idx, totals.shape)
    return totals[x, y], (x + 1, y + 1), size

part1 = part2 = (0, (0, 0), 0)
for block in range(1, 301):
    if block ** 2 * 4 < part2[0]:  # upper bound can't beat current best
        break
    result = sum_size(block)
    part2 = max(part2, result)
    if block == 3:
        part1 = result

print(f"Part 1: {part1[1]}")
print(f"Part 2: {*part2[1], part2[2]}")