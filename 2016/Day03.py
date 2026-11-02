import sys

def is_triangle(triangle: list[int]) -> bool:
    a, b, c = sorted(triangle)
    return a + b > c

with open(sys.argv[1]) as f:
    triangles = [list(map(int, line.split())) for line in f.read().splitlines()]

part1 = part2 = 0
for i in range(0, len(triangles), 3):
    group = triangles[i:i+3]
    for j in range(3):
        part1 += is_triangle(group[j])
        part2 += is_triangle([group[0][j], group[1][j], group[2][j]])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")