import sys

with open(sys.argv[1]) as f:
    options, targets = f.read().split("\n\n")
    options = set(options.split(", "))
    targets = targets.splitlines()

max_len = max(map(len, options))
def combs(target: str) -> int:
    n = len(target)
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(n):
        if ways[i] == 0:
            continue
        for j in range(i + 1, min(i + max_len, n) + 1):
            if target[i:j] in options:
                ways[j] += ways[i]
    return ways[n]

combinations = [combs(t) for t in targets]
print(f"Part 1: {sum(c > 0 for c in combinations)}")
print(f"Part 2: {sum(combinations)}")