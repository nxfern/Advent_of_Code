import sys
from collections import deque
from itertools import permutations

WALLS: set[complex] = set()
positions: dict[int, complex] = {}
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            if ch == "#":
                WALLS.add(complex(r, c))
            elif ch.isdigit():
                positions[int(ch)] = complex(r, c)

pos_to_key = {v: k for k, v in positions.items()}
keys = sorted(positions.keys())
distances: dict[int, dict[int, int]] = {}
for k in keys:
    queue = deque([(positions[k], 0)])
    visited = {positions[k]}
    dist = {}
    while queue:
        pos, steps = queue.popleft()
        if pos in pos_to_key and pos != positions[k]:
            dist[pos_to_key[pos]] = steps
        for np in [pos+1, pos-1, pos+1j, pos-1j]:
            if np in WALLS or np in visited:
                continue
            visited.add(np)
            queue.append((np, steps+1))
    distances[k] = dist

to_visit = keys[1:]
part1 = part2 = float('inf')
for order in permutations(to_visit):
    path = (0,) + order
    steps = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
    part1 = min(part1, steps)
    part2 = min(part2, steps + distances[order[-1]][0])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")