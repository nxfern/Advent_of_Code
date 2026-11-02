import sys
from copy import deepcopy

UPDATES: dict[str, str] = {"#": ".", ".": "#"}
with open(sys.argv[1]) as f:
    grid = [list(row) for row in f.read().splitlines()]

def update_grid(grid: list[list[str]]) -> str:
    changes: list[tuple[int, int]] = []
    for r in range(5):
        for c in range(5):
            bugs = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 5 and 0 <= nc < 5:
                    bugs += grid[nr][nc] == "#"

            if grid[r][c] == "#" and bugs != 1:
                changes.append((r, c))
            if grid[r][c] == "." and 1 <= bugs <= 2:
                changes.append((r, c))
    
    for r, c in changes:
        grid[r][c] = UPDATES[grid[r][c]]

    return "".join("".join(row) for row in grid)

p1_grid = deepcopy(grid)
states: set[str] = {"".join("".join(row) for row in p1_grid)}
while (state := update_grid(p1_grid)) not in states:
    states.add(state)

print(f"Part 1: {sum(pow(2, i) for i, ch in enumerate(state) if ch == "#")}")

def empty_grid() -> list[list[str]]:
    return [["."] * 5 for _ in range(5)]

def count_adjacent(grids: dict[int, list[list[str]]], level: int, r: int, c: int) -> int:
    adjacent = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (nr, nc) == (2, 2):
            inner = grids.get(level + 1, empty_grid())
            if dr == 1:
                adjacent += sum(inner[0][i] == "#" for i in range(5))
            elif dr == -1:
                adjacent += sum(inner[4][i] == "#" for i in range(5))
            elif dc == 1:
                adjacent += sum(inner[i][0] == "#" for i in range(5))
            elif dc == -1:
                adjacent += sum(inner[i][4] == "#" for i in range(5))
        elif not (0 <= nr < 5 and 0 <= nc < 5):
            outer = grids.get(level - 1, empty_grid())
            adjacent += outer[2 + dr][2 + dc] == "#"
        else:
            adjacent += grids[level][nr][nc] == "#"
    return adjacent

def update_all_grids(grids: dict[int, list[list[str]]]) -> dict[int, list[list[str]]]:
    min_level, max_level = min(grids.keys()), max(grids.keys())
    for level in range(min_level - 1, max_level + 2):
        grids.setdefault(level, empty_grid())
    new_grids = {}
    for level in range(min_level - 1, max_level + 2):
        grid = grids[level]
        next_grid = [row[:] for row in grid]
        for r in range(5):
            for c in range(5):
                if (r, c) == (2, 2):
                    continue
                bugs = count_adjacent(grids, level, r, c)
                next_grid[r][c] = "#" if (ch := grid[r][c] == "#" and bugs == 1) or (ch == "." and 1 <= bugs <= 2) else "."
        if any("#" in row for row in next_grid):
            new_grids[level] = next_grid
    return new_grids

def recursive_simulation(initial: list[list[str]], minutes: int) -> int:
    grids = {0: initial}
    for _ in range(minutes):
        grids = update_all_grids(grids)
    return sum(row.count("#") for grid in grids.values() for row in grid)

print(f"Part 2: {recursive_simulation(grid, 200)}")