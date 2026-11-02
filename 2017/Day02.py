import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    spreadsheet = [sorted(map(int, line.split())) for line in f.read().splitlines()]

part1 = part2 = 0
for sheet in spreadsheet:
    part1 += sheet[-1] - sheet[0]
    for (lo, hi) in combinations(sheet, 2):
        if hi % lo == 0:
            part2 += hi // lo
            break
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")