import sys
import re

Cuboid = tuple[int, int, int, int, int, int]

def clip(lo: int, hi: int) -> tuple[int, int] | None:
    lo = max(lo, -50)
    hi = min(hi, 50)
    if lo > hi:
        return None
    return lo, hi

with open(sys.argv[1]) as f:
    steps: list[tuple[bool, Cuboid]] = []
    clipped: list[tuple[bool, Cuboid]] = []
    for line in f.read().splitlines():
        s, n = line.split()
        s = s == "on"
        x1, x2, y1, y2, z1, z2 = list(map(int, re.findall(r'-?\d+', n)))
        steps.append((s, (x1, x2, y1, y2, z1, z2)))
        cx = clip(x1, x2)
        cy = clip(y1, y2)
        cz = clip(z1, z2)
        if cx is None or cy is None or cz is None:
            continue
        clipped.append((s, (*cx, *cy, *cz)))

grid: set[tuple[int, int, int]] = set()
for s, (x1, x2, y1, y2, z1, z2) in clipped:
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                if s:
                    grid.add((x, y, z))
                else:
                    grid.discard((x, y, z))

print(f"Part 1: {len(grid)}")

def intersect(a: Cuboid, b: Cuboid) -> Cuboid | None:
    ax1, ax2, ay1, ay2, az1, az2 = a
    bx1, bx2, by1, by2, bz1, bz2 = b
    x1, x2 = max(ax1, bx1), min(ax2, bx2)
    if x1 > x2:
        return None
    y1, y2 = max(ay1, by1), min(ay2, by2)
    if y1 > y2:
        return None
    z1, z2 = max(az1, bz1), min(az2, bz2)
    if z1 > z2:
        return None
    return (x1, x2, y1, y2, z1, z2)

def volume(c: Cuboid) -> int:
    x1, x2, y1, y2, z1, z2 = c
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

signed: list[tuple[Cuboid, int]] = []
for s, cube in steps:
    new: list[tuple[Cuboid, int]] = []
    for box, sign in signed:
        if (overlap := intersect(box, cube)):
            new.append((overlap, -sign))
    if s:
        new.append((cube, 1))

    signed.extend(new)

print(f"Part 2: {sum(s * volume(c) for c, s in signed)}")