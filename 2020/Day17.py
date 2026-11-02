import sys
from itertools import product
from collections import Counter

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

def get_neighbors(coord: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [
        tuple(c + d for c, d in zip(coord, offsets))
        for offsets in product([-1, 0, 1], repeat=len(coord))
        if any(d != 0 for d in offsets)
    ]

def cubes(n: int) -> int:
    active: set[tuple[int, ...]] = {(x, y, *([0] * (n - 2))) for y, row in enumerate(data)
                                    for x, ch in enumerate(row) if ch == "#"}
    for _ in range(6):
        neighbor_counts = Counter(neighbor for c in active
                                for neighbor in get_neighbors(c))
        active = {c for c, count in neighbor_counts.items()
                if count == 3 or (count == 2 and c in active)}
    
    return len(active)

print(f"Part 1: {cubes(3)}")
print(f"Part 2: {cubes(4)}")