import sys

with open(sys.argv[1]) as f:
    stream = iter(f.read())

opened = garbage = part1 = part2 = 0
for ch in stream:
    if ch == "!":
        next(stream)
        continue
    if garbage > 0:
        part2 += 1
        if ch == ">":
            part2 -= 1
            garbage -= 1
    elif ch == "}":
        part1 += opened
        opened -= 1
    elif ch == "<":
        garbage += 1
    elif ch == "{":
        opened += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")