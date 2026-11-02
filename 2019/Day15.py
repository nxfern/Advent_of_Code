import sys
from intcode import Computer
from collections import deque

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

dirs: dict[int, complex] = {1: -1j, 2: 1j, 3: -1, 4: 1}
visited: set[complex] = set()
explore: deque[tuple[complex, Computer, int]] = deque([(0, Computer(data), 0)]) # pos, prog, steps
tank = part1 = 0
while explore:
    pos, prog, steps = explore.popleft()
    if pos in visited:
        continue
    visited.add(pos)
    for d in range(1, 5):
        if (new_pos := pos + dirs[d]) in visited:
            continue
        branch = Computer(list(prog.mem.values()))
        branch.ip = prog.ip
        branch.base = prog.base
        branch.halted = prog.halted
        status = branch.run(d, feedback=True)
        if status == 0:
            continue
        if status == 2:
            tank = new_pos
            part1 = steps + 1
        explore.append((new_pos, branch, steps + 1))

flood: deque[tuple[complex, int]] = deque([(tank, 0)])
seen: set[complex] = set()
part2 = 0
while flood:
    pos, minutes = flood.popleft()
    if pos in seen:
        continue
    seen.add(pos)
    part2 = max(part2, minutes)
    for d in dirs.values():
        if (new_pos := pos + d) in visited and new_pos not in seen:
            flood.append((new_pos, minutes + 1))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")