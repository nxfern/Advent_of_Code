import sys
from itertools import combinations
from math import prod

def repair(expenses: list[int], n: int) -> int:
    for c in combinations(expenses, n):
        if sum(c) == 2020:
            return prod(c)
    return -1

with open(sys.argv[1]) as f:
    expenses = list(map(int, f.readlines()))

print(f"Part 1: {repair(expenses, 2)}")
print(f"Part 2: {repair(expenses, 3)}")