import sys
from collections import defaultdict, deque

grid: dict[complex, str] = {}
HEIGHT = WIDTH = 0
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            if ch != " ":
                HEIGHT = max(HEIGHT, r)
                WIDTH = max(WIDTH, c)
                grid[complex(c, r)] = ch

portals: defaultdict[str, list[complex]] = defaultdict(list)
for pos, ch in grid.items():
    if ch.isalpha():
        for d in [1j, 1]:                       # down, right
            if (letter := grid.get(pos+d, "")).isupper():
                name = ch + letter
                if grid.get(pos-d) == ".":      # opposite direction
                    portals[name].append(pos-d)
                elif grid.get(pos+d+d) == ".":  # one more in initial dir
                    portals[name].append(pos+d+d)

start, target = portals.pop("AA")[0], portals.pop("ZZ")[0]
links: dict[complex, complex] = {}
for a, b in portals.values():
    links[a] = b
    links[b] = a

def is_largest(pos: complex) -> bool:
    x, y = pos.real, pos.imag
    return x <= 2 or y <= 2 or x >= WIDTH-3 or y >= HEIGHT-3

queue: deque[tuple[complex, int, int]] = deque([(start, 0, 0)])
visited: set[tuple[complex, int]] = {(start, 0)}
part1 = part2 = 0
while queue:
    pos, level, steps = queue.popleft()
    if pos == target:
        part1 = steps if part1 == 0 else part1
        if level == 0:
            part2 = steps
            break
    
    if (n_pos := links.get(pos)):
        if (n_level := level - 1 if is_largest(pos) else level + 1) >= 0:
            if (n_pos, n_level) not in visited:
                visited.add((n_pos, n_level))
                queue.append((n_pos, n_level, steps+1))
    
    for n_pos in [pos+1j, pos-1j, pos+1, pos-1]:
        if (n_pos, level) not in visited and grid.get(n_pos) == ".":
            visited.add((n_pos, level))
            queue.append((n_pos, level, steps+1))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")