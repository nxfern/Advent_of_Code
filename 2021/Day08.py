import sys

with open(sys.argv[1]) as f:
    lines = [([frozenset(p) for p in pat], [frozenset(o) for o in out])
             for line in f.read().splitlines() for pat, out in [map(str.split, line.split(" | "))]]

UNIQUE: dict[int, int] = {2: 1, 3: 7, 4: 4, 7: 8}
part1 = part2 = 0
for pat, out in lines:
    part1 += sum(len(o) in UNIQUE for o in out)

    one = next(p for p in pat if len(p) == 2)
    four = next(p for p in pat if len(p) == 4)
    six = next(p for p in pat if len(p) == 6 and not one <= p)
    mapping: dict[frozenset[str], str] = {}
    for p in pat:
        l = len(p)
        if l in UNIQUE:
            mapping[p] = str(UNIQUE[l])
        elif l == 6:
            if four <= p:
                mapping[p] = "9"
            elif one <= p:
                mapping[p] = "0"
            else:
                mapping[p] = "6"
        elif l == 5:
            if one <= p:
                mapping[p] = "3"
            elif p <= six:
                mapping[p] = "5"
            else:
                mapping[p] = "2"
    part2 += int("".join(mapping[o] for o in out))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")