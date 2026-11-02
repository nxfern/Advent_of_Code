import sys

with open(sys.argv[1]) as f:
    directions = [(s[0], int(s[1:])) for s in f.read().split(", ")]

trans: dict[str, complex] = {"L": 1j, "R": -1j}
part1, facing, part2 = 0, 1j, 0
visited: set[complex] = {part1}
for d, n in directions:
    facing *= trans[d]
    if part2 == 0:
        for _ in range(n):
            part1 += facing
            if part2 == 0 and part1 in visited:
                part2 = part1
            visited.add(part1)
    else:
        part1 += facing * n

print(f"Part 1: {int(abs(part1.real) + abs(part1.imag))}")
print(f"Part 2: {int(abs(part2.real) + abs(part2.imag))}")