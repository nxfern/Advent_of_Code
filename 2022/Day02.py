import sys

with open(sys.argv[1]) as f:
    rounds = [line.split() for line in f.read().splitlines()]

P1 = {"A": "X", "B": "Y", "C": "Z", "X": "C", "Y": "A", "Z": "B"}
VAL = {"X": 1, "Y": 2, "Z": 3}
P2 = {"X": "Z", "Y": "X", "Z": "Y"}

part1 = part2 = 0
for elf, you in rounds:
    part1 += VAL[you]
    if P1[you] == elf:
        part1 += 6
    elif you == P1[elf]:
        part1 += 3

    if you == "X":
        part2 += VAL[P2[P1[elf]]]
    elif you == "Y":
        part2 += VAL[P1[elf]] + 3
    else:
        part2 += VAL[P2[P2[P1[elf]]]] + 6

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")