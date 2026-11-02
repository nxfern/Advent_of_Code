import sys
from math import prod

with open(sys.argv[1]) as f:
    slope = f.read().splitlines()

def trees_hit(dr: int, dc: int) -> int:
    r = c = trees = 0
    while r < len(slope):
        trees += slope[r][c] == "#"
        r, c = r+dr, (c+dc) % len(slope[0])
    return trees

print(f"Part 1: {trees_hit(1, 3)}")
print(f"Part 2: {prod(trees_hit(*s) for s in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])}")