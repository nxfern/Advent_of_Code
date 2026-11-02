import sys
import re

with open(sys.argv[1]) as f:
    assignments = [tuple(map(int, re.findall(r"\d+", line))) for line in f.read().splitlines()]

part1 = part2 = 0
for lo1, hi1, lo2, hi2 in assignments:
    part1 += (lo1 <= lo2 and hi1 >= hi2) or (lo2 <= lo1 and hi2 >= hi1)
    part2 += lo1 <= hi2 and lo2 <= hi1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")