import sys
from collections import deque

with open(sys.argv[1]) as f:
    N = int(f.read())

def is_wall(pos: complex) -> bool:
    x, y = int(pos.real), int(pos.imag)
    f = x*x + 3*x + 2*x*y + y + y*y + N
    return bin(f)[2:].count("1") % 2 == 1

target = 31 + 39j
queue = deque([(1+ 1j, 0)])   # start pos, steps
visited: set[complex] = {1 + 1j}
part1 = part2 = 0
while queue:
    pos, steps = queue.popleft()
    if part2 == 0 and steps >= 50:
        part2 = len(visited)
    if pos == target:
        part1 = steps
        break
    for np in [pos+1, pos-1, pos+1j, pos-1j]:
        if np.real < 0 or np.imag < 0 or np in visited or is_wall(np):
            continue
        visited.add(np)
        queue.append((np, steps+1))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")