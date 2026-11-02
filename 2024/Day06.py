import sys, bisect
from collections import defaultdict

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()
    ROWS, COLS = len(grid), len(grid[0])
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

Obstacles = defaultdict[int, list[int]]
row_obs: Obstacles = defaultdict(list)  # row -> sorted obstacle columns in that row
col_obs: Obstacles = defaultdict(list)  # col -> sorted obstacle rows in that col
start = (0, 0)
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            row_obs[r].append(c)
            col_obs[c].append(r)
        elif ch == "^":
            start = (r, c)

def next_stop(r: int, c: int, d: int, row_o: Obstacles, col_o: Obstacles) -> tuple[int, int] | None:
    if d == 0:  # up
        obs = col_o[c]
        idx = bisect.bisect_left(obs, r)
        return None if idx == 0 else (obs[idx - 1] + 1, c)
    if d == 2:  # down
        obs = col_o[c]
        idx = bisect.bisect_right(obs, r)
        return None if idx == len(obs) else (obs[idx] - 1, c)
    if d == 3:  # left
        obs = row_o[r]
        idx = bisect.bisect_left(obs, c)
        return None if idx == 0 else (r, obs[idx - 1] + 1)
    obs = row_o[r]  # d == 1, right
    idx = bisect.bisect_right(obs, c)
    return None if idx == len(obs) else (r, obs[idx] - 1)

def walk_visited(row_o: Obstacles, col_o: Obstacles, pos: tuple[int, int]):
    r, c, d = *pos, 0
    visited = {(r, c)}
    while True:
        stop = next_stop(r, c, d, row_o, col_o)
        dr, dc = DIRS[d]
        if stop is None:
            while 0 <= r < ROWS and 0 <= c < COLS:
                visited.add((r, c))
                r, c = r + dr, c + dc
            return visited
        nr, nc = stop
        steps = max(abs(nr - r), abs(nc - c))
        for i in range(1, steps + 1):
            visited.add((r + dr * i, c + dc * i))
        r, c, d = nr, nc, (d + 1) % 4

def has_loop(row_o: Obstacles, col_o: Obstacles, pos: tuple[int, int]):
    r, c, d = *pos, 0
    seen = set()
    while True:
        if (r, c, d) in seen:
            return True
        seen.add((r, c, d))
        stop = next_stop(r, c, d, row_o, col_o)
        if stop is None:
            return False
        r, c = stop
        d = (d + 1) % 4

visited = walk_visited(row_obs, col_obs, start)
print(f"Part 1: {len(visited)}")

count = 0
for (r, c) in visited - {start}:
    bisect.insort(row_obs[r], c)
    bisect.insort(col_obs[c], r)
    if has_loop(row_obs, col_obs, start):
        count += 1
    row_obs[r].remove(c)
    col_obs[c].remove(r)

print(f"Part 2: {count}")