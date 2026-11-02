import sys
from collections import defaultdict
from itertools import combinations

antennas: defaultdict[str, list[complex]] = defaultdict(list)
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    ROWS, COLS = len(lines), len(lines[0])
    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch != ".":
                antennas[ch].append(complex(c, r))

def inbounds(pos: complex) -> bool:
    return 0 <= pos.imag < ROWS and 0 <= pos.real < COLS

def antis(p1: complex, p2: complex, multiple: bool = False) -> set[complex]:
    dx = p2 - p1
    result = set()
    for p, d in [(p1, -dx), (p2, dx)]:
        if inbounds(p+d):
            result.add(p+d)
        if multiple:
            result.update({p1, p2})
            while inbounds(p+d):
                result.add(p+d)
                p += d
    return result

part1: set[complex] = set()
part2: set[complex] = set()
for coords in antennas.values():
    for p1, p2 in combinations(coords, 2):
        part1.update(antis(p1, p2))
        part2.update(antis(p1, p2, multiple=True))

print(f"Part 1: {len(part1)}")
print(f"Part 2: {len(part2)}")