import sys

with open(sys.argv[1]) as f:
    firewall: dict[int, int] = {d: r for line in f.read().splitlines() for d, r in [map(int, line.split(": "))]}

delay = part1 = part2 = 0
while True:
    if delay == 0:
        part1 = sum(i * r for i, r in firewall.items() if (i) % (2 * (r-1)) == 0)
        
    caught = any((i + delay) % (2 * (r - 1)) == 0 for i, r in firewall.items())
    if not caught:
        part2 = delay
        break
    delay += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")