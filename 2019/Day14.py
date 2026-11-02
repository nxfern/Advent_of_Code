import sys
from math import ceil

recipes: dict[str, tuple[int, list[tuple[int, str]]]] = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        ingredients, result = line.split(" => ")
        amt, name = int(result.split()[0]), result.split()[1]
        ingredients = [(int(n), c) for ing in ingredients.split(", ") for n, c in [ing.split()]]
        recipes[name] = (amt, ingredients)

def dfs_ore(chem: str, req: int, surplus: dict[str, int]) -> int:
    if chem == "ORE":
        return req
    
    if (available := surplus.get(chem, 0)) >= req:
        surplus[chem] = available - req
        return 0
    
    req -= available
    surplus[chem] = 0
    amount, ingredients = recipes[chem]
    times = ceil(req / amount)
    surplus[chem] = times * amount - req

    total_ore = 0
    for amt, ing in ingredients:
        total_ore += dfs_ore(ing, amt * times, surplus)
    return total_ore

print(f"Part 1: {dfs_ore("FUEL", 1, {})}")

TARGET = 1_000_000_000_000
lo, hi = 1, TARGET
while lo < hi:
    mid = (lo + hi + 1) // 2
    if dfs_ore("FUEL", mid, {}) <= TARGET:
        lo = mid
    else:
        hi = mid - 1

print(f"Part 2: {lo}")