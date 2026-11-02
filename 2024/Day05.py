import sys
from collections import defaultdict
from functools import cmp_to_key

rules: defaultdict[int, set[int]] = defaultdict(set)
with open(sys.argv[1]) as f:
    blocks = f.read().split("\n\n")
    for line in blocks[0].splitlines():
        k, v = map(int, line.split("|"))
        rules[k].add(v)
    prints = [list(map(int, l.split(","))) for l in blocks[1].splitlines()]

def cmp(a, b):
    if b in rules[a]:
        return -1
    if a in rules[b]:
        return 1
    return 0

part1 = part2 = 0
for p in prints:
    l = len(p)
    if all(set(p[i+1:]).issubset(rules[n]) for i, n in enumerate(p)):
        part1 += p[l//2]
    else:
        part2 += sorted(p, key=cmp_to_key(cmp))[l//2]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")