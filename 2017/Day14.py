import sys
from Day10 import knot_hash

def to_bin(hex_string: str) -> str:
    return "".join(f"{int(c, 16):04b}" for c in hex_string)

def dfs(grid: list[list[str]], r: int, c: int) -> None:
    rows, cols = len(grid), len(grid[0])
    stack = [(r, c)]
    while stack:
        nr, nc = stack.pop()
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
            grid[nr][nc] = "0"
            stack.extend([(nr-1, nc), (nr+1, nc), (nr, nc-1), (nr, nc+1)])

with open(sys.argv[1]) as f:
    key = f.read()

grid = [list(to_bin(str(knot_hash(key + "-" + str(i), p2=True)))) for i in range(128)]
print(f"Part 1: {sum(row.count("1") for row in grid)}")

part2 = 0
rows, cols = len(grid), len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "1":
            dfs(grid, r, c)
            part2 += 1
print(f"Part 2: {part2}")