import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    passphrases = f.read().splitlines()

part1 = part2 = 0
for phrase in passphrases:
    combs = list(combinations(phrase.split(), 2))
    if any(a == b for a, b in combs):
        continue
    part1 += 1
    if any(sorted(a) == sorted(b) for a, b in combs):
        continue
    part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")