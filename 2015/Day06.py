import sys
import numpy as np

with open(sys.argv[1]) as f:
    instructions = f.read().splitlines()

part1 = np.zeros((1000, 1000), dtype=bool)
part2 = np.zeros((1000, 1000), dtype=int)
for line in instructions:
    parts = line.split()
    if line.startswith("toggle"):
        op = parts[0]
        x1, y1 = map(int, parts[1].split(","))
    else:
        op = parts[1]
        x1, y1 = map(int, parts[2].split(","))
    x2, y2 = map(int, parts[-1].split(","))

    if op == "toggle":
        part1[x1:x2+1, y1:y2+1] ^= True
        part2[x1:x2+1, y1:y2+1] += 2
    elif op == "on":
        part1[x1:x2+1, y1:y2+1] = True
        part2[x1:x2+1, y1:y2+1] += 1
    else:
        part1[x1:x2+1, y1:y2+1] = False
        part2[x1:x2+1, y1:y2+1] = np.maximum(part2[x1: x2+1, y1: y2+1] - 1, 0)

print(f"Part 1: {part1.sum()}")
print(f"Part 2: {part2.sum()}")