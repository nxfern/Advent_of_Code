import sys
import re

class Point:
    def __init__(self, x: int, y: int, dx: int, dy: int) -> None:
        self.pos: tuple[int, ...] = (x, y)
        self.vel: tuple[int, ...] = (dx, dy)
    
    def elapse(self, t: int) -> None:
        self.pos = tuple(p + (v * t) for p, v in zip(self.pos, self.vel))

    def __repr__(self) -> str:
        return f"pos=<{self.pos} vel=<{self.vel}"

def show_grid(points: list[Point]) -> None:
    coords = set()
    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")
    for p in points:
        min_x, max_x = min(min_x, p.pos[0]), max(max_x, p.pos[0])
        min_y, max_y = min(min_y, p.pos[1]), max(max_y, p.pos[1])
        coords.add(p.pos)

    print("\n".join(
        "".join("#" if (x, y) in coords else "."
                for x in range(int(min_x), int(max_x)+1))
                for y in range(int(min_y), int(max_y)+1)))

with open(sys.argv[1]) as f:
    data = [Point(*map(int, re.findall(r'[-]?\d+', line))) for line in f.read().splitlines()]

for point in data:
    point.elapse(10619)
show_grid(data)