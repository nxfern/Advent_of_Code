import sys
from collections import deque
from math import prod

with open(sys.argv[1]) as f:
    cave = [list(map(int, row)) for row in f.read().splitlines()]


lows: list[tuple[int, int]] = []
part1 = 0
for r in range(len(cave)):
    for c in range(len(cave[0])):
        curr = cave[r][c]
        for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
            if nr < 0 or nr >= len(cave) or nc < 0 or nc >= len(cave[0]):
                continue
            if curr >= cave[nr][nc]:
                break
        else:
            part1 += curr + 1
            lows.append((r, c))

print(f"Part 1: {part1}")

def flood(sr: int, sc: int, seen: set[tuple[int, int]]) -> int:
    queue: deque[tuple[int, int]] = deque([(sr, sc)])
    seen.add((sr, sc))
    size = 0
    while queue:
        r, c = queue.popleft()
        size += 1
        for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
            if nr < 0 or nr >= len(cave) or nc < 0 or nc >= len(cave[0]):
                continue
            if (nr, nc) in seen or cave[nr][nc] == 9:
                continue
            seen.add((nr, nc))
            queue.append((nr, nc))
    return size

basins: list[int] = []
seen: set[tuple[int, int]] = set()
for r, c in lows:
    if (r, c) not in seen:
        basins.append(flood(r, c, seen))

print(f"Part 2: {prod(sorted(basins)[-3:])}")