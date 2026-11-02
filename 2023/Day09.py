import sys

with open(sys.argv[1]) as f:
    readings = [list(map(int, line.split())) for line in f.read().splitlines()]

part1 = part2 = 0
for forwards in readings:
    backwards = forwards[::-1]
    while any(n != 0 for n in forwards):
        part1 += forwards[-1]
        part2 += backwards[-1]
        forwards = [b - a for a, b in zip(forwards, forwards[1:])]
        backwards = [b - a for a, b in zip(backwards, backwards[1:])]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")