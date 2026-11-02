import sys
from math import ceil, sqrt
from typing import Iterator

with open(sys.argv[1]) as f:
    n = int(f.read())

k = ceil((sqrt(n) - 1) / 2)
part1 = k + abs((n - pow(2*k - 1, 2) - 1) % (2*k) - (k-1))
print(f"Part 1: {part1}")

def spiral() -> Iterator[tuple[int, int]]:
    x = y = 0
    yield x, y
    step = 1
    while True:
        for _ in range(step):
            x += 1; yield x, y
        for _ in range(step):
            y += 1; yield x, y
        step += 1
        for _ in range(step):
            x -= 1; yield x, y
        for _ in range(step):
            y -= 1; yield x, y
        step += 1

grid: dict[tuple[int, int], int] = {}
for x, y in spiral():
    val = sum(grid.get((x+dx, y+dy), 0)
              for dx in (-1, 0, 1)
              for dy in (-1, 0, 1)) or 1
    grid[(x, y)] = val
    if val > n:
        print(f"Part 2: {val}")
        break