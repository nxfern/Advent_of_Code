import sys

def get_coords(grid: list[str]) -> set[int]:
    return {r*5 + c for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"}        

locks: list[set[int]] = []
keys: list[set[int]] = []
with open(sys.argv[1]) as f:
    for block in f.read().split("\n\n"):
        grid = block.splitlines()
        if grid[0].count("#") == 5:
            locks.append(get_coords(grid))
        else:
            keys.append(get_coords(grid))

print(f"Answer: {sum(l.isdisjoint(k) for l in locks for k in keys)}")