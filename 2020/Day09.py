import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    seq = list(map(int, f.readlines()))

part1 = 0
for i in range(25, len(seq)):
    if not any(sum(c) == seq[i] for c in combinations(seq[i-25:i], 2)):
        part1 = seq[i]
        break

print(f"Part 1: {part1}")

def get_sum(i: int) -> int|None:
    total = 0
    for j in range(i, len(seq)):
        total += seq[j]
        if total > part1:
            return
        if total == part1 and len(seq[i:j+1]) >= 2:
            return min(seq[i:j+1]) + max(seq[i:j+1])

i, part2 = 0, None
while i < len(seq) and (part2 := get_sum(i)) is None:
    i += 1

print(f"Part 2: {part2}")