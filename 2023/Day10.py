import sys
from collections import deque
from typing import Generator

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()
    rows, cols = len(grid), len(grid[0])
    start = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S')

PIPE_DIRS = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
}

def neighbors(r: int, c: int) -> Generator[tuple[int, int]]:
    ch = grid[r][c]
    if ch == 'S':
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                npipe = grid[nr][nc]
                if npipe in PIPE_DIRS and (-dr, -dc) in PIPE_DIRS[npipe]:
                    yield nr, nc
    elif ch in PIPE_DIRS:
        for dr, dc in PIPE_DIRS[ch]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

dist = {start: 0}
q = deque([start])
while q:
    cur = q.popleft()
    for nxt in neighbors(*cur):
        if nxt not in dist:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

loop = [start]
prev, cur = None, start
while True:
    nbrs = [n for n in neighbors(*cur) if n != prev]
    nxt = nbrs[0]
    if nxt == start:
        break
    loop.append(nxt)
    prev, cur = cur, nxt

area2 = 0
n = len(loop)
for i in range(n):
    r1, c1 = loop[i]
    r2, c2 = loop[(i + 1) % n]
    area2 += (c1 * r2) - (c2 * r1)
    
area = abs(area2) // 2
boundary = n

print(f"Part 1: {max(dist.values())}")
print(f"Part 2: {area - boundary // 2 + 1}")