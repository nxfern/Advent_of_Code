import sys

with open(sys.argv[1]) as f:
    report = list(map(int, f.readlines()))

print(f"Part 1: {sum(a < b for a, b in zip(report, report[1:]))}")
print(f"Part 1: {sum(a < b for a, b in zip(report, report[3:]))}")