import sys
from collections import Counter

left: list[int] = []
right: list[int] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

counts = Counter(right)
print(f"Part 1: {sum(abs(a-b) for a, b in zip(sorted(left), sorted(right)))}")
print(f"Part 2: {sum(n * counts[n] for n in left)}")