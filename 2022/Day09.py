import sys

DIRS = {"U": -1j, "D": 1j, "L": -1, "R": 1}
with open(sys.argv[1]) as f:
    motions = [(DIRS[d], int(n)) for line in f.read().splitlines() for d, n in [line.split()]]

def sign(n: float) -> int:
    return (n > 0) - (n < 0)

def move(head: complex, tail: complex) -> complex:
    diff = head - tail
    if max(abs(diff.real), abs(diff.imag)) > 1:
        return sign(diff.real) + sign(diff.imag) * 1j
    return 0j

rope = [0j] * 10
part1 = {rope[0]}
part2 = {rope[0]}
for d, n in motions:
    for _ in range(n):
        rope[0] += d
        i = 1
        while i < len(rope) and (m := move(rope[i-1], rope[i])) != 0:
            rope[i] += m
            i += 1
        part2.add(rope[-1])
        part1.add(rope[1])

print(f"Part 1: {len(part1)}")
print(f"Part 2: {len(part2)}")