import sys
from itertools import cycle

reindeer: dict[str, tuple[int, int, int]] = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = line.split()
        reindeer[parts[0]] = int(parts[3]), int(parts[6]), int(parts[-2])

states = {name: cycle([v] * t + [0] * r) for name, (v, t, r) in reindeer.items()}
positions: dict[str, int] = {n: 0 for n in reindeer}
scores: dict[str, int] = {n: 0 for n in reindeer}

limit = int(sys.argv[2])    # 1000 for ex 2503 for puzzle input
part1 = 0
for _ in range(limit):
    for name, gen in states.items():
        positions[name] += next(gen)
    best = max(positions.values())
    part1 = max(part1, best)
    for name, d in positions.items():
        if d == best:
            scores[name] += 1
part2 = max(scores.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")