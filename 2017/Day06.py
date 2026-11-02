import sys

with open(sys.argv[1]) as f:
    banks = list(map(int, f.read().split()))

states: dict[tuple[int, ...], int] = {}
steps = 0
while True:
    state = tuple(banks)
    if state in states:
        break
    states[state] = steps
    i = banks.index(max(banks))
    blocks = banks[i]
    banks[i] = 0
    for j in range(1, blocks + 1):
        banks[(i + j) % len(banks)] += 1
    steps += 1

print(f"Part 1: {steps}")
print(f"Part 2: {steps - states[state]}")