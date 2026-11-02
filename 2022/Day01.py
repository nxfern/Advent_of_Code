import sys

with open(sys.argv[1]) as f:
    elves = sorted([sum(map(int, block.splitlines())) for block in f.read().split("\n\n")], reverse=True)

print(f"Part 1: {elves[0]}")
print(f"Part 2: {sum(elves[:3])}")