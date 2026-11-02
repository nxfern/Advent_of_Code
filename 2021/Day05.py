import sys
from collections import defaultdict

part1: defaultdict[tuple[int, int], int] = defaultdict(int)
part2: defaultdict[tuple[int, int], int] = defaultdict(int)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        start, end = line.split(" -> ")
        x1, y1, x2, y2 = map(int, start.split(",") + end.split(","))
        dx = (x2 > x1) - (x2 < x1)  # 1, 0, or -1
        dy = (y2 > y1) - (y2 < y1)  # 1, 0, or -1
        while True:
            part2[(x1, y1)] += 1
            if dx == 0 or dy == 0:
                part1[(x1, y1)] += 1
            if (x1, y1) == (x2, y2):
                break
            x1 += dx
            y1 += dy

print(f"Part 1: {sum(c > 1 for c in part1.values())}")
print(f"Part 1: {sum(c > 1 for c in part2.values())}")