import sys
import numpy as np

EMPTY, TREES, LUMBER = 0, 1, 2

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

char_to_int = {'.': EMPTY, '|': TREES, '#': LUMBER}
grid = np.array([[char_to_int[ch] for ch in row] for row in lines], dtype=np.int8)

minutes = int(sys.argv[2])

def step(grid: np.ndarray) -> np.ndarray:
    # Cast to int8 BEFORE summing — bool + bool stays bool in NumPy (True+True=True, not 2)
    p = np.pad(grid == TREES, 1).astype(np.int8)
    l = np.pad(grid == LUMBER, 1).astype(np.int8)

    tree_neighbors = (p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
                      p[1:-1, :-2]                + p[1:-1, 2:] +
                      p[2:,  :-2] + p[2:,  1:-1] + p[2:,  2:])
    lumb_neighbors = (l[:-2, :-2] + l[:-2, 1:-1] + l[:-2, 2:] +
                      l[1:-1, :-2]                + l[1:-1, 2:] +
                      l[2:,  :-2] + l[2:,  1:-1] + l[2:,  2:])

    is_empty  = grid == EMPTY
    is_trees  = grid == TREES
    is_lumber = grid == LUMBER

    new_grid = grid.copy()
    new_grid[is_empty  & (tree_neighbors >= 3)] = TREES
    new_grid[is_trees  & (lumb_neighbors >= 3)] = LUMBER
    new_grid[is_lumber & ~((lumb_neighbors >= 1) & (tree_neighbors >= 1))] = EMPTY

    return new_grid

def score(grid: np.ndarray) -> int:
    return int(np.sum(grid == TREES)) * int(np.sum(grid == LUMBER))

seen: dict[bytes, int] = {}
history: list[np.ndarray] = []
part1 = 0

for minute in range(1, minutes + 1):
    grid = step(grid)

    if minute == 10:
        part1 = score(grid)

    key = grid.tobytes()
    if key in seen:
        cycle_start = seen[key]
        cycle_length = minute - cycle_start
        remaining = (minutes - cycle_start) % cycle_length
        grid = history[cycle_start + remaining - 1]
        break

    seen[key] = minute
    history.append(grid)

print(f"Part 1: {part1}")
print(f"Part 2: {score(grid)}")