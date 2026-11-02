import sys

allergens: dict[str, set[str]] = {}
all_ings: list[str] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        ings, algns = line.split(" (contains ")
        ings = ings.split()
        all_ings.extend(ings)
        for a in algns.strip(")").split(", "):
            if a in allergens:
                allergens[a] &= set(ings)
            else:
                allergens[a] = set(ings)

print(f"Part 1: {len([i for i in all_ings if i not in set.union(*allergens.values())])}")

resolved: dict[str, str] = {}
while allergens:
    for a, ings in allergens.items():
        if len(ings) == 1:
            ing = next(iter(ings))
            resolved[a] = ing
            del allergens[a]
            for o in allergens.values():
                o.discard(ing)
            break

print(f"Part 2: {','.join(resolved[a] for a in sorted(resolved.keys()))}")