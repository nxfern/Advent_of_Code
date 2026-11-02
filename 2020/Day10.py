import sys

with open(sys.argv[1]) as f:
    adapters = sorted(map(int, f.readlines()))
    adapters = [0] + adapters + [adapters[-1] + 3]

single = triple = 0
ways: dict[int, int] = {0: 1}
for a, b in zip(adapters, adapters[1:]):
    single += b-a == 1
    triple += b-a == 3
    ways[b] = sum(ways.get(b-i, 0) for i in range(1, 4))

print(f"Part 1: {single * triple}")
print(f"Part 2: {ways[adapters[-1]]}")