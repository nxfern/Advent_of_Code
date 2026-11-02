import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    pts = [tuple(map(int, line.split(","))) for line in f.read().splitlines() if line]

edges = [(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1])]
candidates = sorted(
    (
        ((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1),
         min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        for (x1, y1), (x2, y2) in combinations(pts, 2)
    ),
    reverse=True
)

print(f"Part 1: {candidates[0][0]}")

for area, xmin, ymin, xmax, ymax in candidates:
    if not any(ex2 > xmin and ex1 < xmax and ey2 > ymin and ey1 < ymax for ex1, ey1, ex2, ey2 in edges):
        print(f"Part 2: {area}")
        break