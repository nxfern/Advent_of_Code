import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

width = len(lines[0])
counts = [0] * width
counts[lines[0].index('S')] = 1
splits = escaped = 0

for row in lines[1:]:
    new = [0] * width
    for c, n in enumerate(counts):
        if n == 0:
            continue
        if row[c] == '^':
            splits += 1
            if c > 0:
                new[c - 1] += n
            else:
                escaped += n
            if c < width - 1:
                new[c + 1] += n
            else:
                escaped += n
        else:
            new[c] += n
    counts = new

print(f"Part 1: {splits}")
print(f"Part 2: {sum(counts) + escaped}")