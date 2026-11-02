import sys
import random

with open(sys.argv[1]) as f:
    lines, molecule = f.read().split("\n\n")
    rules: list[tuple[str, str]] = []
    for line in lines.splitlines():
        k, v = line.split(" => ")
        rules.append((k, v))

# Part 1
calibration: set[str] = set()
for (k, v) in rules:
    i = 0
    while i < len(molecule):
        front, back = molecule[:i], molecule[i:]
        if k not in back:
            break
        calibration.add(front + back.replace(k, v, 1))
        i += 1

print(f"Part 1: {len(calibration)}")

# Part 2
while True:
    deconstruction = molecule.strip()
    part2 = 0
    while deconstruction != "e":
        for (k, v) in rules:
            if v in deconstruction:
                deconstruction = deconstruction.replace(v, k, 1)
                part2 += 1
                break
        else:
            random.shuffle(rules)
            break
    else:
        break

print(f"Part 2: {part2}")