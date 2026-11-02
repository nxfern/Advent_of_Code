import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    galaxies = [(r, c) for r, row in enumerate(f.read().splitlines())
                for c, ch in enumerate(row) if ch == "#"]

def expand(universe: list[tuple[int, int]], n: int = 1) -> int:
    rows = {r for r, _ in galaxies}
    empty_rows = [r for r in range(max(rows)) if r not in rows]
    cols = {c for _, c in galaxies}
    empty_cols = [c for c in range(max(cols)) if c not in cols]
    expanded: list[tuple[int, int]] = []
    for r, c in galaxies:
        er = sum(e < r for e in empty_rows) * (n - 1)
        ec = sum(e < c for e in empty_cols) * (n - 1)
        expanded.append((r+er, c+ec))

    return sum(abs(r2-r1) + abs(c2-c1) for (r1, c1), (r2, c2) in combinations(expanded, 2))

print(f"Part 1: {expand(galaxies)}")
print(f"Part 2: {expand(galaxies, 1_000_000)}")