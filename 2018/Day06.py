import sys
from collections import Counter

coords: list[tuple[int, int]] = []
min_x = min_y = 1_000_000_000_000
max_x = max_y = 0
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        x, y = map(int, line.split(", "))
        coords.append((x, y))
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)

def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)

def closest(x: int, y: int) -> int:
    best, second = float("inf"), float("inf")
    best_i = -1
    for i, (cx, cy) in enumerate(coords):
        d = manhattan(cx, cy, x, y)
        if d < best:
            best, second, best_i = d, best, i
        elif d < second:
            second = d
    return -1 if best == second else best_i

infinite: set[int] = set()
area: Counter[int] = Counter()
limit = int(sys.argv[2])
part2 = 0
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        if sum(manhattan(cx, cy, x, y) for cx, cy in coords) < limit:
            part2 += 1
        c = closest(x, y)
        if c == -1:
            continue
        if x in (min_x, max_x) or y in (min_y, max_y):
            infinite.add(c)
        area[c] += 1

print(f"Part 1: {max(v for k, v in area.items() if k not in infinite)}")
print(f"Part 2: {part2}")