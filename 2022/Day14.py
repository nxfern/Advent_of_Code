import sys

walls: set[complex] = set()
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        coords = [tuple(map(int, c.split(","))) for c in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    walls.add(complex(x, y))

ymax = max(w.imag for w in walls) + 1
occupied = set(walls)
source = complex(500, 0)

part1 = None
count = 0
stack = [source]
while stack:
    pos = stack[-1]
    if pos.imag == ymax:
        occupied.add(pos)
        if part1 is None:
            part1 = count
        count += 1
        stack.pop()
        continue

    for np in [pos+1j, pos+1j-1, pos+1j+1]:
        if np not in occupied:
            stack.append(np)
            break
    else:
        occupied.add(pos)
        count += 1
        stack.pop()

print(f"Part 1: {part1}")
print(f"Part 2: {count}")