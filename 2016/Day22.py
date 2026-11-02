import sys
import re
from itertools import permutations
from collections import deque

nodes: dict[tuple[int, int], tuple[int, int, int]] = {}
max_x = max_y = 0
empty_node = None
with open(sys.argv[1]) as f:
    for line in f.read().splitlines()[2:]:
        x, y, size, used, avail, _ = map(int, re.findall(r"\d+", line))
        nodes[(x, y)] = (size, used, avail)
        max_x, max_y = max(max_x, x), max(max_y, y)
        if used == 0:
            empty_node = (x, y)

print(f"Part 1: {sum(a[1] > 0 and b[2] >= a[1] for a, b in permutations(nodes.values(), 2))}")

assert empty_node
target = (max_x, 0)
bfs_goal = (max_x - 1, 0)
max_avail = max(t[2] for t in nodes.values())
walls = {pos for pos, (_, u, _) in nodes.items() if u > max_avail}
queue: deque[tuple[tuple[int, int], int]] = deque([(empty_node, 0)])
visited: set[tuple[int, int]] = {empty_node}
steps_to_position = -1
while queue:
    (x, y), steps = queue.popleft()
    if (x, y) == bfs_goal:
        steps_to_position = steps
        break
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if (0 <= nx <= max_x and 0 <= ny <= max_y and
            (nx, ny) not in walls and (nx, ny) not in visited and (nx, ny) != target):
            visited.add((nx, ny))
            queue.append(((nx, ny), steps + 1))

print(f"Part 2: {steps_to_position + 5 * (max_x - 1) + 1}")