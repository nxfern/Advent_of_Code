import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    dir_sizes: dict[tuple[str, ...], int] = defaultdict(int)
    path: list[str] = []
    for line in f.read().splitlines():
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[-1] == "/":
                    path.clear()
                elif parts[-1] == "..":
                    path.pop()
                else:
                    path.append(parts[-1])
        elif parts[0] != "dir":
            for i in range(len(path) + 1):
                dir_sizes[tuple(path[:i])] += int(parts[0])

sizes = list(dir_sizes.values())
print(f"Part 1: {sum(s for s in sizes if s <= 100_000)}")
print(f"Part 2: {min(s for s in sizes if s >= max(sizes) - 40_000_000)}")