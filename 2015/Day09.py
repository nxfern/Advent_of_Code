import sys
from itertools import permutations

distances: dict[tuple[str, str], int] = {}
cities: set[str] = set()
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = line.split()
        distances[(parts[0], parts[2])] = int(parts[-1])
        distances[(parts[2], parts[0])] = int(parts[-1])
        cities.update([parts[0], parts[2]])

lengths: list[int] = []
for p in permutations(cities):
    lengths.append(sum(distances[(p[i], p[i+1])] for i in range(len(p)-1)))

# Part 1
part1 = min(lengths)
print(f"Part 1: {part1}")

# Part 2
part2 = max(lengths)
print(f"Part 2: {part2}")