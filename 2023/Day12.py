import sys
from functools import cache

@cache
def count(pattern: str, groups: tuple[int, ...]) -> int:
    total = 0
    if len(pattern) == 0:
        if len(groups) == 0:
            return 1
        return 0
    
    if len(groups) == 0:
        if "#" in pattern:
            return 0
        return 1

    if len(pattern) < sum(groups) + len(groups) - 1:
        return 0

    if pattern[0] in ".?":
        total += count(pattern[1:], groups)

    n = groups[0]
    if (pattern[0] in "#?" and
        "." not in pattern[:n] and
        (len(pattern) == n or pattern[n] in ".?")):
        total += count(pattern[n+1:], groups[1:])
    
    return total

springs: list[tuple[str, tuple[int, ...]]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        arr, broken = line.split()
        springs.append((arr, tuple(map(int, broken.split(",")))))

print(f"Part 1: {sum(count(*s) for s in springs)}")
print(f"Part 2: {sum(count('?'.join([p]*5), g*5) for p, g in springs)}")