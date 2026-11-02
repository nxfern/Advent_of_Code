import sys
from math import prod

COLORS = {"red": 12, "green": 13, "blue": 14}
part1 = part2 = 0
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

for line in lines:
    game, pulls = line.split(": ")
    game = int(game.split()[1])
    totals = {"red": 0, "green": 0, "blue": 0}
    pulls = [p.split(", ") for p in pulls.split("; ")]
    for pull in pulls:
        for p in pull:
            n, c = p.split()
            totals[c] = max(totals[c], int(n))

    part2 += prod(totals.values())
    if all(totals[c] <= COLORS[c] for c in COLORS):
        part1 += game

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")