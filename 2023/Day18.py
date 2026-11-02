import sys

DIRS: dict[str, complex] = {
    "U": -1j, "D": 1j, "L": -1, "R": 1,
    "0": 1, "1": 1j, "2": -1, "3": -1j
}
plans: list[tuple[str, int, str]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        c, n, h = line.split()
        plans.append((c, int(n), h.strip("#()")))

def shoelace(vertices: list[complex]) -> int:
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i].real, vertices[i].imag
        x2, y2 = vertices[(i+1)%n].real, vertices[(i+1)%n].imag
        area += x1 * y2 - x2 * y1
    return int(abs(area) / 2)

p1 = p2 = perim1 = perim2 = 0
points1: list[complex] = [p1]
points2: list[complex] = [p2]
for c, n, h in plans:
    perim1 += n
    p1 += DIRS[c] * n
    points1.append(p1)
    p2 += DIRS[h[5]] * int(h[:5], 16)
    points2.append(p2)
    perim2 += int(h[:5], 16)

print(f"Part 1: {shoelace(points1) + perim1 // 2 + 1}") # Pick's theorem
print(f"Part 2: {shoelace(points2) + perim2 // 2 + 1}")