import sys
from collections import Counter

with open(sys.argv[1]) as f:
    lo, hi = map(int, f.read().split("-"))
    
part1 = part2 = 0
for n in range(lo, hi+1):
    digits = str(n)
    if any(b < a for a, b in zip(digits, digits[1:])):
        continue
    counts = Counter(digits).values()
    if any(v >= 2 for v in counts):
        part1 += 1
    if any(v == 2 for v in counts):
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")