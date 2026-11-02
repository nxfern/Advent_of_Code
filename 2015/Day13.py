import sys
from collections import defaultdict
from itertools import permutations

def get_happiness(people: defaultdict[str, dict[str, int]]) -> int:
    result, n_people = 0, len(people)
    for order in permutations(people.keys()):
        total = 0
        for i in range(n_people):
            left, right = order[i], order[(i+1) % n_people]
            if left == "me" or right == "me":
                continue
            total += people[left][right] + people[right][left]
        result = max(result, total)
    return result

happiness: defaultdict[str, dict[str, int]] = defaultdict(dict)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = line.split()
        happiness[parts[0]][parts[-1].strip(".")] = int(parts[3]) * (1 if parts[2] == "gain" else -1)

# Part 1
part1 = get_happiness(happiness)
print(f"Part 1: {part1}")

# Part 2 - adding myself
happiness["me"] = {}
part2 = get_happiness(happiness)
print(f"Part 2: {part2}")