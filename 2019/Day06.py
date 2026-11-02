import sys
from collections import defaultdict, deque

graph: defaultdict[str, list[str]] = defaultdict(list)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        a, b = line.split(")")
        graph[a].append(b)
        graph[b].append(a)

def bfs(start: str, target: str|None=None) -> int:
    depth = 0
    queue: deque[tuple[str, int]] = deque([(start, 0)])
    visited: set[str] = {start}
    while queue:
        node, steps = queue.popleft()
        depth += steps
        for neighbor in graph[node]:
            if neighbor == target:
                return steps-1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps+1))
    return depth

print(f"Part 1: {bfs(start="COM")}")
print(f"Part 2: {bfs(start="YOU", target="SAN")}")