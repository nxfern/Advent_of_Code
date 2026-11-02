import sys
from itertools import cycle

class Cart:
    def __init__(self, pos: complex, d: complex) -> None:
        self.pos = pos
        self.d = d
        self.turn = cycle([-1j, 1, 1j])
        self.alive = True

dirs = {"<": -1+0j, ">": 1+0j, "^": -1j, "v": 1j}
tracks: dict[complex, str] = {}
carts: list[Cart] = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, char in enumerate(line):
            if char in dirs:
                carts.append(Cart(complex(x, y), dirs[char]))
            elif char in "\\/+":
                tracks[complex(x, y)] = char

part1 = None
while len(carts) > 1:
    carts.sort(key=lambda c: (c.pos.imag, c.pos.real))
    positions = {c.pos: c for c in carts}
    for c in carts:
        if not c.alive:
            continue
        del positions[c.pos]
        c.pos += c.d

        if (track := tracks.get(c.pos)):
            if track == "+":
                c.d *= next(c.turn)
            elif track == "/":
                c.d = complex(-c.d.imag, -c.d.real)
            else:
                c.d = complex(c.d.imag, c.d.real)

        if c.pos in positions:
            if part1 is None:
                part1 = int(c.pos.real), int(c.pos.imag)
            positions[c.pos].alive = False
            c.alive = False
        else:
            positions[c.pos] = c
    carts = [c for c in carts if c.alive]

print(f"Part 1: {part1}")
print(f"Part 2: {int(carts[0].pos.real), int(carts[0].pos.imag)}")