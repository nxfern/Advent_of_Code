import sys
from hashlib import md5
from collections import deque

with open(sys.argv[1]) as f:
    passcode = f.read()

dirs: dict[int, tuple[complex, str]] = {0: (-1j, "U"), 1: (1j, "D"), 2: (-1, "L"), 3: (1, "R")}
queue: deque[tuple[complex, str]] = deque([(0+0j, "")])
part1 = part2 = ""
while queue:
    pos, path = queue.popleft()
    if pos == 3 + 3j:
        if not part1:
            part1 = path
        part2 = path
        continue
    doors = md5((passcode + path).encode()).hexdigest()[:4]
    for i, door in enumerate(doors):
        if door in "bcdef":
            dp, d = dirs[i]
            np = pos + dp
            if 0 <= np.real <= 3 and 0 <= np.imag <= 3:
                queue.append((np, path+d))

print(f"Part 1: {part1}")
print(f"Part 2: {len(part2)}")