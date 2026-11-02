import sys
from collections import deque

with open(sys.argv[1]) as f:
    rolls = {complex(c, r) for r, row in enumerate(f.read().splitlines())
             for c, ch in enumerate(row) if ch == "@"}

NEIGHBORS = lambda p: [p+1, p+1+1j, p+1-1j, p-1, p-1+1j, p-1-1j, p+1j, p-1j]
count = {p: sum(np in rolls for np in NEIGHBORS(p)) for p in rolls}
queue = deque(p for p, n in count.items() if n < 4)
removed = set(queue)
print(f"Part 1: {len(queue)}")

while queue:
    p = queue.popleft()
    for np in NEIGHBORS(p):
        if np in count and np not in removed:
            count[np] -= 1
            if count[np] < 4:
                removed.add(np)
                queue.append(np)

print(f"Part 2: {len(removed)}")