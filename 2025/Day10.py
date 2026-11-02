import sys, re
from functools import cache
from itertools import combinations

def solve(diagram: str, btns: list[tuple[int, ...]], joltage: tuple[int, ...]) -> tuple[int, int]:
    n = len(joltage)
    patterns: dict[int, list[tuple[tuple[int, ...], int]]] = {}
    for k in range(len(btns) + 1):
        for combo in combinations(btns, k):
            eff = [0] * n
            for b in combo:
                for i in b:
                    eff[i] += 1
            mask = 0
            for i, e in enumerate(eff):
                mask |= (e & 1) << i
            patterns.setdefault(mask, []).append((tuple(eff), k))

    target = sum(1 << i for i, ch in enumerate(diagram) if ch == "#")
    p1 = patterns[target][0][1]

    @cache
    def f(j: tuple[int, ...]) -> float:
        if not any(j):
            return 0
        mask = 0
        for i, v in enumerate(j):
            mask |= (v & 1) << i
        best = float("inf")
        for eff, k in patterns.get(mask, ()):
            if all(v >= e for v, e in zip(j, eff)):
                best = min(best, k + 2 * f(tuple((v - e) >> 1 for v, e in zip(j, eff))))
        return best

    return p1, int(f(joltage))

part1 = part2 = 0
with open(sys.argv[1]) as fh:
    for line in fh.read().splitlines():
        c, *but, jolt = line.split()
        btns = [tuple(map(int, re.findall(r"\d+", b))) for b in but]
        joltage = tuple(map(int, re.findall(r"\d+", jolt)))
        a, b = solve(c[1:-1], btns, joltage)
        part1 += a
        part2 += b

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")