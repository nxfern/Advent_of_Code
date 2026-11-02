import sys
import re
from collections import deque

flows: dict[str, int] = {}
conns: dict[str, list[str]] = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        valve, flow, *tunnels = re.findall(r"([A-Z]{2}|-?\d+)", line)
        flows[valve] = int(flow)
        conns[valve] = tunnels

distances: dict[tuple[str, str], int] = {}
for start in conns:
    visited = {start: 0}
    queue = deque([start])
    while queue:
        valve = queue.popleft()
        for node in conns[valve]:
            if node not in visited:
                visited[node] = visited[valve] + 1
                queue.append(node)
    for end, d in visited.items():
        distances[(start, end)] = d

USEFUL = [(i, v) for i, v in enumerate([v for v in flows if flows[v] > 0])]
N = len(USEFUL)
FULL_MASK = (1 << N) - 1

best: dict[int, int] = {}
def dfs(pos: str, time_left: int, mask: int, score: int) -> None:
    best[mask] = max(best.get(mask, 0), score)
    for i, valve in USEFUL:
        if mask & (1 << i):
            continue
        cost = distances[(pos, valve)] + 1
        remaining = time_left - cost
        if remaining <= 0:
            continue
        dfs(valve, remaining, mask | (1 << i), score + remaining * flows[valve])

dfs("AA", 30, 0, 0)
print(f"Part 1: {max(dict(best).values())}")

best.clear()
dfs("AA", 26, 0, 0)
for i in range(N):
    bit = 1 << i
    for mask in range(1 << N):
        if mask & bit:
            best[mask] = max(best.get(mask, 0), best.get(mask ^ bit, 0))

print(f"Part 2: {max(best.get(mask, 0) + best.get(FULL_MASK ^ mask, 0) for mask in range(1 << N))}")