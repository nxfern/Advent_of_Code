import sys

with open(sys.argv[1]) as f:
    instructions = f.read().splitlines()

keypad1 = [[str(i + j*3) for i in range(1, 4)] for j in range(3)]
keypad2 = [[None, None, "1", None, None],
           [None, "2", "3", "4", None],
           ['5', "6", "7", "8", "9"],
           [None, "A", "B", "C", None],
           [None, None, "D", None, None]]
d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
r1 = c1 = 1
r2, c2 = 2, 0
part1 = part2 = ""
for line in instructions:
    for m in line:
        nr1, nc1 = [a + b for a, b, in zip((r1, c1), d[m])]
        nr2, nc2 = [a + b for a, b, in zip((r2, c2), d[m])]
        (r1, c1) = (nr1, nc1) if 0 <= nr1 < len(keypad1) and 0 <= nc1 < len(keypad1[0]) else (r1, c1)
        (r2, c2) = (nr2, nc2) if 0 <= nr2 < len(keypad2) and 0 <= nc2 < len(keypad2[0]) and keypad2[nr2][nc2] is not None else (r2, c2)
    part1 += keypad1[r1][c1]
    part2 += keypad2[r2][c2]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")