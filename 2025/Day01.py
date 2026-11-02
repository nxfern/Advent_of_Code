import sys

ROT = {"L": -1, "R": 1}
with open(sys.argv[1]) as f:
    turns = [(l[0], int(l[1:])) for l in f.read().splitlines()]

pos, part1, part2 = 50, 0, 0
for t, n in turns:
    part2 += (pos + n) // 100 if t == "R" else ((100 - pos) % 100 + n) // 100
    pos = (pos + ROT[t] * n) % 100
    part1 += pos == 0

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")