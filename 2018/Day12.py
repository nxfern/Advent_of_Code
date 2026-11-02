import sys

with open(sys.argv[1]) as f:
    START, lines = f.read().split("\n\n")
    START = START.split()[2]
    rules: dict[str, str] = {}
    for line in lines.splitlines():
        pattern, _, result = line.split()
        if result == "#":
            rules[pattern] = result

generations = 50_000_000_000
pots = {i for i, c in enumerate(START) if c == "#"}
part1 = part2 = 0
for gen in range(generations):
    if gen == 20:
        part1 = sum(pots)

    lo, hi = min(pots), max(pots)
    next_pots = {
        i for i in range(lo - 2, hi + 3)
        if "".join("#" if j in pots else "." for j in range(i - 2, i + 3)) in rules
    }

    shift = min(next_pots) - min(pots)
    if {p - min(next_pots) for p in next_pots} == {p - min(pots) for p in pots}:
        remaining = generations - gen - 1
        part2 = sum(p + shift * remaining for p in next_pots)
        break
    pots = next_pots

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")