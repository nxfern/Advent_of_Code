import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

part1 = part2 = 0
for line in lines:
    p1 = True
    vowels = repeat = pair_repeat = mid_repeat = 0
    for i, ch in enumerate(line):
        if ch in "aeiou":
            vowels += 1
        if i > 0:
            pair = line[i-1:i+1]
            if p1 and pair in ["ab", "cd", "pq", "xy"]:
                p1 = False
            if ch == line[i-1]:
                repeat += 1
            if pair in line[i+1:]:
                pair_repeat += 1
        if i > 1 and line[i-2] == ch:
            mid_repeat += 1

    if p1 and vowels >= 3 and repeat >= 1:
        part1 += 1
    if pair_repeat >= 1 and mid_repeat >= 1:
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")