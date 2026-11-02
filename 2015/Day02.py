import sys

with open(sys.argv[1]) as f:
    presents = [list(map(int, line.split("x"))) for line in f.readlines()]

part1 = part2 = 0
for (l, w, h) in presents:
    s1, s2, s3 = l*w, l*h, w*h
    part1 += 2 * (s1 + s2 + s3) + min(s1, s2, s3)
    part2 += (l + w + h - max(l, w, h)) * 2 + l * w * h

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")