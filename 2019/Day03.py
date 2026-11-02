import sys

with open(sys.argv[1]) as f:
    moves = [[(m[0], int(m[1:])) for m in line.split(",")] for line in f.read().splitlines()]

DIRS: dict[str, complex] = {"U": -1j, "D": 1j, "L": -1, "R": 1}
wires: list[dict[complex, int]] = []
for line in moves:
    pos, steps, temp = 0, 0, {}
    for d, n in line:
        for _ in range(n):
            steps += 1
            pos += DIRS[d]
            temp[pos] = steps
    wires.append(temp)

intersections: set[complex] = wires[0].keys() & wires[1].keys()
print(f"Part 1: {int(min(abs(c.real) + abs(c.imag) for c in intersections))}")
print(f"Part 2: {min(wires[0][i] + wires[1][i] for i in intersections)}")