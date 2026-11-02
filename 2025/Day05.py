import sys

with open(sys.argv[1]) as f:
    ranges, ingredients = f.read().split("\n\n")
    ranges = sorted(list(map(int, l.split("-"))) for l in ranges.splitlines())
    merged = [list(ranges[0])]
    for lo, hi in ranges[1:]:
        last = merged[-1]
        if lo <= last[1] + 1:
            last[1] = max(last[1], hi)
        else:
            merged.append([lo, hi])
    ingredients = list(map(int, ingredients.splitlines()))

print(f"Part 1: {sum(any(lo <= i <= hi for lo, hi in merged) for i in ingredients)}")
print(f"Part 2: {sum(hi+1 - lo for lo, hi in merged)}")