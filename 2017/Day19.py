import sys

paths: dict[complex, str] = {}
pos, d = 0, 1j                          # starting direction = down
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        if r == 0:
            pos = complex(row.index("|"), r)
        for c, ch in enumerate(row):
            if ch != " ":
                paths[complex(c, r)] = ch

part1, part2 = "", 0
while pos in paths:
    if paths[pos] == "+":
        for nd in [d * 1j, d * -1j]:    # [right turn, left turn]
            if pos + nd in paths:
                d = nd
                break
    elif paths[pos].isalpha():
            part1 += paths[pos]
    pos += d
    part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")