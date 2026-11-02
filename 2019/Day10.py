import sys
from math import gcd, atan2, pi
from collections import defaultdict

def laser_angle(dx: int, dy: int) -> float:
    a = atan2(dx, -dy)
    return a + 2*pi if a < 0 else a

with open(sys.argv[1]) as f:
    asteroids = [(x, y) for y, line in enumerate(f.read().splitlines())
                 for x, ch in enumerate(line) if ch == "#"]

def group_by_direction(sx: int, sy: int) -> defaultdict:
    groups: defaultdict[tuple[int,int], list[tuple[int,int]]] = defaultdict(list)
    for ax, ay in asteroids:
        if (ax, ay) == station: continue
        dx, dy = ax - sx, ay - sy
        g = gcd(abs(dx), abs(dy))
        groups[(dx // g, dy // g)].append((ax, ay))
    for v in groups.values():
        v.sort(key=lambda a: abs(a[0]-sx) + abs(a[1]-sy))
    return groups

def count_visible(sx: int, sy: int) -> int:
    def direction(ax, ay):
        dx, dy = ax - sx, ay - sy
        g = gcd(abs(dx), abs(dy))
        return dx // g, dy // g
    return len({direction(ax, ay) for ax, ay in asteroids if (ax, ay) != (sx, sy)})

station = max(asteroids, key=lambda c: count_visible(*c))
groups = group_by_direction(*station)
dirs = sorted(groups, key=lambda d: laser_angle(*d))
print(f"Part 1: {len(dirs)}")

order = []
while any(groups[d] for d in dirs):
    for d in dirs:
        if groups[d]:
            order.append(groups[d].pop(0))

x, y = order[199]
print(f"Part 2: {x*100 + y}")