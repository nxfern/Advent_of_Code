import sys
from collections import deque

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()

start = next((r, row.index("S")) for r, row in enumerate(grid) if "S" in row)
dists = {start: 0}
queue = deque([start])
while queue:
    r, c = queue.popleft()
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if grid[nr][nc] != "#" and (nr, nc) not in dists:
            dists[(nr, nc)] = dists[(r, c)] + 1
            queue.append((nr, nc))

def count_shortcuts(max_cheat: int, min_saving: int = 100) -> int:
    offsets = [
        (dr, dc, abs(dr) + abs(dc))
        for dr in range(-max_cheat, max_cheat + 1)
        for dc in range(-max_cheat, max_cheat + 1)
        if 2 <= abs(dr) + abs(dc) <= max_cheat
    ]
    count = 0
    for (r, c), d in dists.items():
        for dr, dc, cost in offsets:
            d2 = dists.get((r + dr, c + dc))
            if d2 is not None and d2 - d - cost >= min_saving:
                count += 1
    return count

print(f"Part 1: {count_shortcuts(2)}")
print(f"Part 2: {count_shortcuts(20)}")