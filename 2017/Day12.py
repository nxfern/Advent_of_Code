import sys
from collections import deque

graph: dict[int, list[int]] = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        left, right = line.split(" <-> ")
        node = int(left)
        neighbors = list(map(int, right.split(", ")))
        graph[node] = neighbors

visited: set[int] = set()
part1 = part2 = 0
for start in graph.keys():
    if start in visited:
        continue

    queue: deque[int] = deque([start])
    group: set[int] = set()
    while queue:
        node = queue.popleft()
        if node in group:
            continue
        group.add(node)
        queue.extend(graph[node])
    visited |= group
    part2 += 1
    if 0 in group:
        part1 = len(group)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")