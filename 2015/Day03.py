import sys

with open(sys.argv[1]) as f:
    directions = f.read()

move = {"^": -1j, "v": 1j, ">": 1, "<": -1}
pos1 = santa = robo = 0j
part1: set[complex] = {pos1}
part2: set[complex] = {pos1}
for i, d in enumerate(directions):
    m = move[d]
    pos1 += m
    part1.add(pos1)

    if i % 2 == 0:
        santa += m
        part2.add(santa)
    else:
        robo += m
        part2.add(robo)

print(f"Part 1: {len(part1)}")
print(f"Part 2: {len(part2)}")