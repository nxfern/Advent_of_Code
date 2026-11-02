import sys
import re
from collections import defaultdict

with open(sys.argv[1]) as f:
    flip = [re.findall(r"ne|nw|se|sw|e|w", line) for line in f.read().splitlines()]

DIRS = {"e":  (1, -1, 0), "se": (0, -1, 1), "sw": (-1, 0, 1),
        "w":  (-1, 1, 0), "nw": (0, 1, -1), "ne": (1, 0, -1)}

tiles: defaultdict[tuple[int, int, int], bool] = defaultdict(bool)
for line in flip:
    x, y, z = 0, 0, 0
    for d in line:
        dx, dy, dz = DIRS[d]
        x += dx
        y += dy
        z += dz
    tiles[(x, y, z)] = not tiles[(x, y, z)]

tiles = defaultdict(bool, {k: v for k, v in tiles.items() if v})
print(f"Part 1: {sum(tiles.values())}")

for _ in range(100):
    candidates: set[tuple[int, int, int]] = set(tiles.keys())
    for x, y, z in tiles:
        for dx, dy, dz in DIRS.values():
            candidates.add((x+dx, y+dy, z+dz))

    updates: list[tuple[int, int, int]] = []
    for x, y, z in candidates:
        count = sum(tiles.get((x+dx, y+dy, z+dz), False) for dx, dy, dz in DIRS.values())
        color = tiles.get((x, y, z), False)
        if color and (count == 0 or count > 2):
            updates.append((x, y, z))
        elif not color and count == 2:
            updates.append((x, y, z))

    for u in updates:
        tiles[u] = not tiles[u]

    tiles = defaultdict(bool, {k: v for k, v in tiles.items() if v})

print(f"Part 2: {sum(tiles.values())}")