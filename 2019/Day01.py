import sys

def get_fuel(m: int) -> int:
    return m // 3 - 2

with open(sys.argv[1]) as f:
    masses = list(map(int, f.readlines()))

part1 = part2 = 0
for m in masses:
    fuel = get_fuel(m)
    part1 += fuel
    part2 += fuel
    while (fuel := get_fuel(fuel)) > 0:
        part2 += fuel

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")