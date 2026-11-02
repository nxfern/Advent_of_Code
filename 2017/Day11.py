import sys

dirs: dict[str, tuple[int, int, int]] = {
    "n": (0, -1, 1),
    "ne": (1, -1, 0),
    "nw": (-1, 0, 1),
    "s": (0, 1, -1),
    "se": (1, 0, -1),
    "sw": (-1, 1, 0)
}

with open(sys.argv[1]) as f:
    path = list(map(lambda p: dirs[p], f.read().split(",")))

pos = (0, 0, 0)
part2 = 0
for p in path:
    pos = tuple(map(sum, zip(pos, p)))
    part2 = max(part2, max(abs(v) for v in pos))

print(f"Part 1: {max(abs(v) for v in pos)}")
print(f"Part 2: {part2}")