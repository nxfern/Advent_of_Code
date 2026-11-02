import sys

with open(sys.argv[1]) as f:
    seq = list(map(int, list(f.read())))

part1 = part2 = 0
length, mid = len(seq), len(seq) // 2
for i, n in enumerate(seq):
    part1 += n if n == seq[(i+1)%length] else 0
    part2 += n if n == seq[(i+mid)%length] else 0

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")