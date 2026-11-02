import sys
import re
from math import prod

with open(sys.argv[1]) as f:
    ingredients = [list(map(int, re.findall(r"-?\d+", line))) for line in f.read().splitlines()]

part1 = part2 = 0
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            d = 100 - a - b - c
            totals = [0, 0, 0, 0]
            calories = 0
            for ing, amt in zip(ingredients, [a, b, c, d]):
                for i in range(4):
                    totals[i] += ing[i] * amt
                calories += ing[-1] * amt
            totals = [max(0, t) for t in totals]
            score = prod(totals)
            part1 = max(part1, score)
            if calories == 500:
                part2 = max(part2, score)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")