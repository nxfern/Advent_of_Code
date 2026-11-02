import sys

with open(sys.argv[1]) as f:
    navi = [(l[0], int(l[1:])) for l in f.read().splitlines()]

CARD: dict[str, complex] = {"N": 1j, "S": -1j, "E": 1, "W": -1}
TURN: dict[str, complex] = {"L": 1j, "R": -1j}
d, wp, part1, part2 = 1, complex(10, 1), 0, 0
for op, n in navi:
    if op in CARD:
        part1 += CARD[op] * n
        wp += CARD[op] * n
    elif op in TURN:
        d *= pow(TURN[op], n // 90)
        wp *= pow(TURN[op], n // 90)
    else:
        part1 += d * n
        part2 += wp * n

print(f"Part 1: {int(abs(part1.real) + abs(part1.imag))}")
print(f"Part 2: {int(abs(part2.real) + abs(part2.imag))}")