import sys

with open(sys.argv[1]) as f:
    passes = [int(line.translate(str.maketrans("FBLR", "0101")), 2)
        for line in f.read().splitlines()]

print(f"Part 1: {max(passes)}")
print(f"Part 2: {sum(range(min(passes), max(passes)+1)) - sum(passes)}")