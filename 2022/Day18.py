import sys
from collections import deque

with open(sys.argv[1]) as f:
    cubes = {tuple(map(int, line.split(","))) for line in f.read().splitlines()}

def neighbors(x: int, y: int, z: int) -> list[tuple[int, int, int]]:
    return [(x+1, y, z), (x-1, y, z),
            (x, y+1, z), (x, y-1, z),
            (x, y, z+1), (x, y, z-1)]

xs, ys, zs = zip(*cubes)
xmin, xmax = min(xs)-1, max(xs)+1
ymin, ymax = min(ys)-1, max(ys)+1
zmin, zmax = min(zs)-1, max(zs)+1

seen: set[tuple[int, int, int]] = set()
queue = deque([(xmin, ymin, zmin)])
part2 = 0
while queue:
    cube = queue.popleft()
    for nx, ny, nz in neighbors(*cube):
        if (nx, ny, nz) in cubes:
            part2 += 1
        elif (nx, ny, nz) not in seen and xmin <= nx <= xmax and ymin <= ny <= ymax and zmin <= nz <= zmax:
            seen.add((nx, ny, nz))
            queue.append((nx, ny, nz))

print(f"Part 1: {sum(n not in cubes for c in cubes for n in neighbors(*c))}")
print(f"Part 2: {part2}")