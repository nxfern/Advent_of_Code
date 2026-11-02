import sys
from collections import defaultdict

symbols: set[complex] = set()
gears: set[complex] = set()
numbers: list[tuple[int, set[complex]]] = []
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        num_str = ""
        coords: set[complex] = set()
        for c, ch in enumerate(row):
            if ch.isnumeric():
                num_str += ch
                coords.add(complex(c, r))
            else:
                if num_str:
                    numbers.append((int(num_str), coords))
                    num_str, coords = "", set()
                if ch != ".":
                    symbols.add(complex(c, r))
                    if ch == "*":
                        gears.add(complex(c, r))
        if num_str:
            numbers.append((int(num_str), coords))

offsets = (1j, 1+1j, -1+1j, -1j, -1-1j, 1-1j, 1, -1)
adjacent: defaultdict[complex, list[int]] = defaultdict(list)
part1 = 0
for value, coords in numbers:
    neighbors = {c + off for c in coords for off in offsets}
    if neighbors & symbols:
        part1 += value

    for g in neighbors & gears:
        adjacent[g].append(value)

print(f"Part 1: {part1}")
print(f"Part 2: {sum(v[0] * v[1] for v in adjacent.values() if len(v) == 2)}")