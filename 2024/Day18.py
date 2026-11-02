import sys
from collections import deque

with open(sys.argv[1]) as f:
    corrupted = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

def bfs(bytes: list[tuple[int, ...]]) -> int:
    walls = set(bytes)
    queue = deque([(0, 0, 0)])  # row, col, steps
    visited = {(0, 0)}
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == (70, 70):
            return steps

        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr <= 70 and 0 <= nc <= 70 and (nr, nc) not in visited and (nr, nc) not in walls:
                queue.append((nr, nc, steps+1))
                visited.add((nr, nc))
    return -1   # no solution found

print(f"Part 1: {bfs(corrupted[:1024])}")

lo, hi = 0, len(corrupted)-1
while lo < hi:
    mid = (lo + hi) // 2
    if bfs(corrupted[:mid+1]) != -1:
        lo = mid + 1
    else:
        hi = mid

print(f"Part 1: {corrupted[lo]}")