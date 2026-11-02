import sys

with open(sys.argv[1]) as f:
    data = f.read()

width = len(data)
mask = (1 << width) - 1
row = int(data.translate(str.maketrans(".^", "01"))[::-1], 2)
part1 = part2 = bin(row).count("1")

for k in range(399_999):
    row = ((row << 1) ^ (row >> 1)) & mask
    traps = bin(row).count("1")
    part2 += traps
    if k < 39:
        part1 += traps

safe1 = (40 * width) - part1
safe2 = (400_000 * width) - part2

print(f"Part 1: {safe1}")
print(f"Part 2: {safe2}")