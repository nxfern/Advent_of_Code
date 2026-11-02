import sys
from typing import Iterator

def process(seq: Iterator[int]) -> tuple[int, int]:
    n_child = next(seq)
    n_data = next(seq)
    children = [process(seq) for _ in range(n_child)]
    metadata = [next(seq) for _ in range(n_data)]
    part1 = sum(c[0] for c in children) + sum(metadata)
    part2 = sum(metadata) if n_child == 0 else sum(children[i-1][1] for i in metadata if 1 <= i <= n_child)
    return part1, part2

with open(sys.argv[1]) as f:
    file = iter(map(int, f.read().split()))

part1, part2 = process(file)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")