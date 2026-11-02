import sys

with open(sys.argv[1]) as f:
    seq = list(map(int, f.readlines()))

print(f"Part 1: {sum(seq)}")

part2 = i = 0
seen: set[int] = {part2}
while True:
    part2 += seq[i % len(seq)]
    if part2 in seen:
        break
    seen.add(part2)
    i += 1

print(f"Part 2: {part2}")