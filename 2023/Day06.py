import sys
from math import sqrt, floor, ceil, prod

def parse_lines(data: str) -> list[list[int]]:
    return [list(map(int, line.split()[1:])) for line in data.splitlines()]

def combine_spaces(data: str) -> list[int]:
    return [int("".join(line.split()[1:])) for line in data.splitlines()]
    
def quadratic(T: int, D: int) -> int:
    disc_sqrt = sqrt(pow(T, 2) - 4 * D) # quadratic formula: t^2 - Tt + D = 0
    t_min = (T - disc_sqrt) / 2
    t_max = (T + disc_sqrt) / 2
    low = ceil(t_min + 1e-9)            # floating point precision error accounting
    high = floor(t_max - 1e-9)
    return max(0, high - low + 1)

with open(sys.argv[1]) as f:
    puzzle = f.read()

print(f"Part 1: {prod(quadratic(t, d) for t, d in zip(*parse_lines(puzzle)))}")
print(f"Part 2: {quadratic(*combine_spaces(puzzle))}")