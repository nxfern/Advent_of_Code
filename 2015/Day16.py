import sys

MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

sues: list[dict[str, int]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = [p.strip(":,") for p in line.split()][2:]
        sues.append({k: int(v) for k, v in zip(*[iter(parts)]*2)})

part1 = part2 = None
for i, sue in enumerate(sues, 1):
    if not part1 and all(MFCSAM.get(k) == v for k, v in sue.items()):
        part1 = i

    if not part2:
        for k, v in sue.items():
            amt = MFCSAM[k]
            if k in ["cats", "trees"]:
                if v <= amt:
                    break
            elif k in ["pomeranians", "goldfish"]:
                if v >= amt:
                    break
            elif amt != v:
                break
        else:
            part2 = i
            
    if part1 and part2:
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")