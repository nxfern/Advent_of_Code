import sys
from collections import deque

with open(sys.argv[1]) as f:
    octopi = [list(map(int, row)) for row in f.read().splitlines()]
    ROWS, COLS = len(octopi), len(octopi[0])

def step() -> int:
    queue: deque[tuple[int, int]] = deque()
    for r in range(ROWS):
        for c in range(COLS):
            octopi[r][c] += 1
            if octopi[r][c] > 9:
                queue.append((r, c))

    flashed = set(queue)
    while queue:
        r, c = queue.popleft()
        for nr, nc in [(r+1,c), (r+1,c-1), (r,c-1), (r-1,c-1), (r-1,c), (r-1,c+1), (r,c+1), (r+1,c+1)]:
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                octopi[nr][nc] += 1
                if octopi[nr][nc] > 9 and (nr, nc) not in flashed:
                    flashed.add((nr, nc))
                    queue.append((nr, nc))

    for r, c in flashed:
        octopi[r][c] = 0

    return len(flashed)

print(f"Part 1: {sum(step() for _ in range(100))}")

part2 = 101 # 100 steps already done, accounting for off by 1
while step() != 100:
    part2 += 1
print(f"Part 2: {part2}")