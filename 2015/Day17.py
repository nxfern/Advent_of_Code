import sys
from itertools import combinations
from collections import defaultdict

with open(sys.argv[1]) as f:
    sizes = list(map(int, f.read().splitlines()))

target = int(sys.argv[2])
n = len(sizes)
combs: defaultdict[int, int] = defaultdict(int)
for r in range(2, n):
    for c in combinations(sizes, r):
        if sum(c) == target:
            combs[r] += 1

print(f"Part 1: {sum(combs.values())}")
print(f"Part 2: {combs[min(combs)]}")