import sys
from collections import Counter, defaultdict

with open(sys.argv[1]) as f:
    stones = Counter(f.read().split())

def blink(stones: defaultdict[str, int] | Counter[str], times: int = 75) -> tuple[int, int]:
    p1 = 0
    for b in range(times):
        if b == 25:
            p1 = sum(stones.values())
        new: defaultdict[str, int] = defaultdict(int)
        for stone, num in stones.items():
            if stone == "0":
                new["1"] += num
            elif len(stone) % 2 == 0:
                mid = len(stone) // 2
                new[stone[:mid]] += num
                new[stone[mid:].lstrip("0") or "0"] += num
            else:
                new[str(int(stone) * 2024)] += num
        stones = new
    return p1, sum(stones.values())

part1, part2 = blink(stones)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")