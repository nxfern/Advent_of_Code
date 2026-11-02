import sys

def manhattan(p1: tuple[int, ...], p2: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(p1, p2))

with open(sys.argv[1]) as f:
    points = [tuple(map(int, line.split(","))) for line in f.readlines()]

constellations: list[set[tuple[int, ...]]] = []
for point in points:
    matching = [c for c in constellations if any(manhattan(point, p) <=3 for p in c)]
    if matching:
        merged = {point}
        for c in matching:
            merged |= c
            constellations.remove(c)
        constellations.append(merged)
    else:
        constellations.append({point})

print(f"Answer: {len(constellations)}")