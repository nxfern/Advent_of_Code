import sys
from typing import Iterator

Grid = tuple[str, ...]

def rotate(grid: Grid) -> Grid:
    n = len(grid)
    return tuple(''.join(grid[n - 1 - j][i] for j in range(n)) for i in range(n))

def flip(grid: Grid) -> Grid:
    return tuple(row[::-1] for row in grid)

def variants(grid: Grid) -> Iterator[Grid]:
    current = grid
    for _ in range(4):
        yield current
        yield flip(current)
        current = rotate(current)

def parse_rules(lines: list[str]) -> dict[Grid, Grid]:
    rules: dict[Grid, Grid] = {}
    for line in lines:
        pattern, output = [tuple(p.split("/")) for p in line.split(" => ")]
        for v in variants(pattern):
            rules[v] = output
    return rules

def split(grid: Grid) -> list[Grid]:
    n = len(grid)
    size = 2 if n % 2 == 0 else 3
    return [tuple(grid[i + x][j:j + size] for x in range(size))
            for i in range(0, n, size)
            for j in range(0, n, size)]

def join(blocks: list[Grid]) -> Grid:
    size = len(blocks[0])
    n = int(len(blocks) ** 0.5)
    return tuple(''.join(blocks[i * n + j][row] for j in range(n))
                 for i in range(n)
                 for row in range(size))

with open(sys.argv[1]) as f:
    rules = parse_rules(f.read().splitlines())

part1 = 0
grid: Grid = (".#.", "..#", "###")
for k in range(1, 19):
    grid = join([rules[block] for block in split(grid)])
    if k == 5:
        part1 = sum(row.count("#") for row in grid)

print(f"Part 1: {part1}")
print(f"Part 2: {sum(row.count("#") for row in grid)}")