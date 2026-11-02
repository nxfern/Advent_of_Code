import sys
from itertools import combinations
from math import prod

def sort_packages(weights: list[int], groups: int) -> int:
    target = sum(weights) // groups
    for size in range(1, len(weights)):
        valid_groups = []
        for combo in combinations(weights, size):
            if sum(combo) == target:
                valid_groups.append(combo)

        if valid_groups:
            return min(prod(group) for group in valid_groups)
    return -1

with open(sys.argv[1]) as f:
    puzzle = list(map(int, f.read().splitlines()))

# Part 1
part1 = sort_packages(puzzle, groups=3)
print(f"Part 1: {part1}")

# Part 2
part2 = sort_packages(puzzle, groups=4)
print(f"Part 2: {part2}")