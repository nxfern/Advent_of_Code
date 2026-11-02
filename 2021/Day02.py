import sys

with open(sys.argv[1]) as f:
    course = [(d[0], int(n)) for line in f.read().splitlines() for d, n in [line.split()]]

x = y1 = y2 = 0
for d, n in course:
    if d == "f":
        x += n
        y2 += y1 * n
    else:
        y1 += n if d == "d" else -n

print(f"Part 1: {x * y1}")
print(f"Part 2: {x * y2}")