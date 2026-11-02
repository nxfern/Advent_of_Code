import sys

def check_mirror(grid: list[list[str]], l: int, r: int, mismatches: int) -> bool:
    length = min(l+1, len(grid)-r)
    found = 0
    for i in range(length):
        found += sum(a != b for a, b in zip(grid[l-i], grid[r+i]))
        if found > mismatches:
            return False        # stops loop short if found already exceeds limit
    return found == mismatches  # matches allowed amount after full loop

def find_reflection(grid: list[list[str]], smudges: int) -> int | None:
    for r in range(1, len(grid)):
        if check_mirror(grid, r-1, r, smudges):
            return r

def all_reflections(blocks: list[str], smudges: int = 0) -> int:
    total = 0
    for block in blocks:
        grid = [list(row) for row in block.splitlines()]
        transposed = list(map(list, zip(*grid)))
        if (r := find_reflection(grid, smudges)):
            total += r * 100
        else:
            total += v if (v := find_reflection(transposed, smudges)) else 0
    return total

with open(sys.argv[1]) as f:
    puzzle = f.read().split("\n\n")

print(f"Part 1: {all_reflections(puzzle)}")
print(f"Part 2: {all_reflections(puzzle, smudges=1)}")