import sys

letters: dict[str, set[complex]] = {"X": set(), "M": set(), "A": set(), "S": set()}
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            letters[ch].add(complex(c, r))

part1 = part2 = 0
for p in letters["X"]:
    for d in [1, 1+1j, 1-1j, -1, -1+1j, -1-1j, 1j, -1j]:
        np = p + d
        for l in "MAS":
            if np not in letters[l]:
                break
            np += d
        else:
            part1 += 1

for p in letters["A"]:
    part2 += all((p - d in letters["M"] and p + d in letters["S"])
                 or (p - d in letters["S"] and p + d in letters["M"])
                 for d in (1+1j, 1-1j))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")