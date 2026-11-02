import sys

with open(sys.argv[1]) as v:
    dots, folds = v.read().split("\n\n")
    dots = set(tuple(map(int, line.split(","))) for line in dots.splitlines())
    folds = [(a, int(v)) for line in folds.splitlines() for a, v in [line.split()[-1].split("=")]]

for i, (a, v) in enumerate(folds):
    new_dots: set[tuple[int, int]] = set()
    for x, y in dots:
        nx = 2*v - x if a == "x" and x > v else x
        ny = 2*v - y if a == "y" and y > v else y
        new_dots.add((nx, ny))
    dots = new_dots
    if i == 0:
        print(f"Part 1: {len(dots)}")

cols, rows = tuple(max(p) for p in zip(*dots))
grid = ["".join("#" if (x, y) in dots else "." for x in range(cols+1)) for y in range(rows+1)]
for row in grid:
    print(row)