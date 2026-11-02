import sys
import re
from heapq import heappop, heappush

def manhattan(p1: tuple[int, ...], p2: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(p1, p2))

NANOBOTS: dict[tuple[int, int, int], int] = {}
x_min = y_min = z_min = float("inf")
x_max = y_max = z_max = float("-inf")
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        x, y, z, r = map(int, re.findall(r'-?\d+', line))
        x_min, x_max = min(x_min, x), max(x_max, x)
        y_min, y_max = min(y_min, y), max(y_max, y)
        z_min, z_max = min(z_min, z), max(z_max, z)
        NANOBOTS[(x, y, z)] = r

# Part 1
strongest = max(NANOBOTS, key=lambda k: NANOBOTS[k])
part1 = sum(manhattan(strongest, k) <= NANOBOTS[strongest] for k in NANOBOTS)
print(f"Part 1: {part1}")

# Part 2
Box = tuple[int, int, int, int, int, int]
def split_box(box: Box) -> list[Box]:
    x_min, x_max, y_min, y_max, z_min, z_max = box
    x_mid = (x_min + x_max) // 2
    y_mid = (y_min + y_max) // 2
    z_mid = (z_min + z_max) // 2
    return [
        (x1, x2, y1, y2, z1, z2)
        for x1, x2 in [(x_min, x_mid), (x_mid+1, x_max)]
        for y1, y2 in [(y_min, y_mid), (y_mid+1, y_max)]
        for z1, z2 in [(z_min, z_mid), (z_mid+1, z_max)]
        if x1 <= x2 and y1 <= y2 and z1 <= z2
    ]

def count_and_dist(box: Box) -> tuple[int, int]:
    x_min, x_max, y_min, y_max, z_min, z_max = box
    n = 0
    for (bx, by, bz), r in NANOBOTS.items():
        dx = max(x_min - bx, 0, bx - x_max)
        dy = max(y_min - by, 0, by - y_max)
        dz = max(z_min - bz, 0, bz - z_max)
        if dx + dy + dz <= r:
            n += 1
    dist = max(x_min, 0, -x_max) + max(y_min, 0, -y_max) + max(z_min, 0, -z_max)
    return n, dist

start_box = int(x_min), int(x_max), int(y_min), int(y_max), int(z_min), int(z_max)
heap = [(-len(NANOBOTS), 0, start_box)] # count, dist, box
best_coord = (0, 0, 0)
while heap:
    _, _, box = heappop(heap)
    if all(box[i] == box[i+1] for i in range(0, 6, 2)):
        best_coord = box[::2]
        break
    for split in split_box(box):
        n, dist = count_and_dist(split)
        size = -(split[1] - split[0])
        heappush(heap, (-n, dist, split))

part2 = manhattan((0, 0, 0), best_coord)
print(f"Part 2: {part2}")