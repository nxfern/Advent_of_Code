import sys
from collections import deque

ALPHA_NUM = {chr(i): i-96 for i in range(97, 123)}
GRID: dict[complex, int] = {}
START = PEAK = 0
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            if ch == "S":
                START = complex(r, c)
                ch = "a"
            elif ch == "E":
                PEAK = complex(r, c)
                ch = "z"
            GRID[complex(r, c)] = ALPHA_NUM[ch]

queue = deque([(PEAK, 0)])
visited = {PEAK}
part1 = part2 = None
while queue:
    pos, steps = queue.popleft()
    if pos == START and part1 is None:
        part1 = steps
    if GRID[pos] == 1 and part2 is None:
        part2 = steps
    if part1 is not None and part2 is not None:
        break

    for np in (pos+1, pos-1, pos+1j, pos-1j):
        if np in visited or np not in GRID or GRID[np] < GRID[pos]-1:
            continue
        visited.add(np)
        queue.append((np, steps+1))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")