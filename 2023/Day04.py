import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

L = len(lines)
copies = [1] * L
part1 = part2 = 0
for i, line in enumerate(lines):
    _, nums = line.split(":", 1)
    w, o = nums.split("|")
    if (m := len(set(w.split()) & set(o.split()))):
        part1 += 1 << (m - 1)   # pow(2, m - 1)
        c = copies[i]
        for j in range(i + 1, min(i + 1 + m, L)):
            copies[j] += c

    part2 += copies[i]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")