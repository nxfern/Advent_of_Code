import sys
import json
from typing import Any

def sum_numbers(obj: Any, p2: bool=False) -> int:
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(sum_numbers(x, p2) for x in obj)
    elif isinstance(obj, dict):
        if p2 and "red" in obj.values():
            return 0
        return sum(sum_numbers(v, p2) for v in obj.values())
    else:
        return 0

with open(sys.argv[1]) as f:
    puzzle = json.load(f)

# Part 1
part1 = sum_numbers(puzzle)
print(f"Part 1: {part1}")

# Part 2
part2 = sum_numbers(puzzle, p2=True)
print(f"Part 2: {part2}")