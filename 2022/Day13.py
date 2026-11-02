import sys
from ast import literal_eval
from functools import cmp_to_key

with open(sys.argv[1]) as f:
    blocks = [[literal_eval(line) for line in block.splitlines()] for block in f.read().split("\n\n")]

def compare(left: list | int, right: list | int) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 1 if left > right else 0

    left = [left] if isinstance(left, int) else left
    right = [right] if isinstance(right, int) else right
    for l, r in zip(left, right):
        if (res := compare(l, r)) != 0:
            return res

    return -1 if len(left) < len(right) else 1 if len(left) > len(right) else 0

print(f"Part 1: {sum(i for i, (l, r) in enumerate(blocks, 1) if compare(l, r) < 0)}")

packets = sorted([p for pair in blocks for p in pair] + [[[2]], [[6]]], key=cmp_to_key(compare))
positions = {str(p): i for i, p in enumerate(packets, 1)}
print(f"Part 2: {positions["[[2]]"] * positions["[[6]]"]}")