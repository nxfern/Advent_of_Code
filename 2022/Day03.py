import sys

with open(sys.argv[1]) as f:
    rucksacks = f.read().splitlines()

PRIORITY = {l: i for i, l in enumerate(map(chr, list(range(97, 123)) + list(range(65, 91))), 1)}

part1 = 0
for r in rucksacks:
    m = len(r) // 2
    compartment = next(iter(set(r[:m]) & set(r[m:])))
    part1 += PRIORITY[compartment]

print(f"Part 1: {part1}")

part2 = 0
for i in range(0, len(rucksacks), 3):
    badge = next(iter(set.intersection(*map(set, rucksacks[i:i+3]))))
    part2 += PRIORITY[badge]

print(f"Part 2: {part2}")