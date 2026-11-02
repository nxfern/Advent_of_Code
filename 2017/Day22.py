import sys

# Functionalizing everything because local variables for long loops are faster than global ones
def get_start_info(grid: list[str]) -> tuple[dict[complex, str], int, int]:
    rows, cols = len(grid), len(grid[0])
    return {
        complex(c, r): 'I'
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] == '#'
    }, rows, cols

def part1(grid: dict[complex, str], rows: int, cols: int) -> int:
    pos, d = complex(cols // 2, rows // 2), -1j     # start dir = up
    count = 0
    for _ in range(10_000):
        s = grid.get(pos)
        if s == 'I':
            grid.pop(pos)
            d *= 1j     # right turn
        else:
            grid[pos] = 'I'
            d *= -1j    # left turn
            count += 1
        pos += d
    return count

def part2(grid: dict[complex, str], rows: int, cols: int) -> int:
    pos, d = complex(cols // 2, rows // 2), -1j     # start dir = up
    count = 0
    for _ in range(10_000_000):
        s = grid.get(pos)
        if s == 'W':
            grid[pos] = 'I'
            count += 1
        elif s == 'I':
            grid[pos] = 'F'
            d *= 1j     # right turn
        elif s == 'F':
            grid.pop(pos)
            d *= -1     # reverse dir
        else:
            grid[pos] = 'W'
            d *= -1j    # left turn
        pos += d
    return count

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()

print(f"Part 1: {part1(*get_start_info(grid))}")
print(f"Part 2: {part2(*get_start_info(grid))}")