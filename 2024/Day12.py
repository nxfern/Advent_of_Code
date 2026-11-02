import sys

grid: dict[tuple[int, int], str] = {}
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            grid[r, c] = ch

seen: set[tuple[int, int]] = set()
part1 = part2 = 0
for start, ch in grid.items():
    if start in seen:
        continue
    seen.add(start)
    stack = [start]
    area = perim = corners = 0
    while stack:
        r, c = stack.pop()
        area += 1
        for nb in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if grid.get(nb) == ch:
                if nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
            else:
                perim += 1
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            a = grid.get((r, c + dc)) == ch
            b = grid.get((r + dr, c)) == ch
            d = grid.get((r + dr, c + dc)) == ch
            corners += a == b and not (a and d)
    part1 += area * perim
    part2 += area * corners

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")