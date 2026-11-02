import sys

with open(sys.argv[1]) as f:
    groups = [list(map(set, g.splitlines())) for g in f.read().split("\n\n")]

print(f"Part 1: {sum(len(set.union(*g)) for g in groups)}")
print(f"Part 2: {sum(len(set.intersection(*g)) for g in groups)}")