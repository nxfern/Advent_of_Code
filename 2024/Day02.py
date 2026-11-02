import sys, operator

OPS = {">": operator.gt, "<": operator.lt}
with open(sys.argv[1]) as f:
    levels = [tuple(map(int, line.split())) for line in f.read().splitlines()]

def safe(seq: tuple[int, ...]) -> bool:
    if seq[0] == seq[1]:
        return False
    op = ">" if seq[0] > seq[1] else "<"
    return all(OPS[op](a, b) and 1 <= abs(a-b) <= 3 for a, b in zip(seq, seq[1:]))

part1 = part2 = 0
for level in levels:
    if safe(level):
        part1 += 1
        part2 += 1
    else:
        for i in range(len(level)):
            damp = level[:i] + level[i+1:]
            if safe(damp):
                part2 += 1
                break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")