import sys

with open(sys.argv[1]) as f:
    nums = list(map(int, f.read().split(",")))

def solve(nums: list[int]) -> tuple[int, int]:  # local vs global vals for large loops
    seen = [0] * 30_000_000
    for i, n in enumerate(nums[:-1], 1):
        seen[n] = i
    last = nums[-1]
    p1 = 0
    for t in range(len(nums), 30_000_000):
        if t == 2020:
            p1 = last
        p = seen[last]
        seen[last] = t
        last = t - p if p else 0
    return p1, last

part1, part2 = solve(nums)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")