import sys

with open(sys.argv[1]) as f:
    puzzle = f.read()

move = {"(": 1, ")": -1}
part1 = part2 = 0
for i, p in enumerate(puzzle, 1):
    part1 += move[p]
    if part2 == 0 and part1 == -1:
        part2 = i

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")