import sys
from collections import defaultdict

CARD = (-1j, 1j, -1, 1)
DIRS = [1j, -1+1j, 1+1j, -1j, 1-1j, -1-1j, 1, -1]
DIR_SEQ = {-1j: (-1-1j, 1-1j),
        1j: (-1+1j, 1+1j),
        -1: (-1+1j, -1-1j),
        1: (1+1j, 1-1j)}

def box(elves: set[complex]) -> int:
    xs, ys = [int(e.real) for e in elves], [int(e.imag) for e in elves]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)

with open(sys.argv[1]) as f:
    elves = {complex(c, r)
             for r, row in enumerate(f.read().splitlines())
             for c, ch in enumerate(row) if ch == "#"}

r = 0   # round counter
while True:
    proposed: defaultdict[complex, list[complex]] = defaultdict(list)
    new_elves: set[complex] = set()
    for elf in elves:
        if all(elf + d not in elves for d in DIRS):
            new_elves.add(elf)
            continue

        for i in range(4):
            d1 = CARD[(r+i)%4]
            d2, d3 = DIR_SEQ[d1]
            if all(elf + d not in elves for d in [d1, d2, d3]):
                proposed[elf + d1].append(elf)
                break
        else:   # elf has at least one elf in each direction
            new_elves.add(elf)

    for move, dudes in proposed.items():
        if len(dudes) > 1:
            for dude in dudes:
                new_elves.add(dude)
        else:
            new_elves.add(move)

    if r == 10:
        print(f"Part 1: {box(elves)}")

    r += 1
    if new_elves == elves:
        print(f"Part 2: {r}")
        break

    elves = new_elves