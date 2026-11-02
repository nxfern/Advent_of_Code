import sys
import re

with open(sys.argv[1]) as f:
    a, b = map(int, re.findall(r"\d+", f.read()))

part1 = 0
part2: dict[str, list[int]] = {"a": [], "b": []}
for _ in range(40_000_000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    a_bit, b_bit = a & 0xFFFF, b & 0xFFFF
    part1 += a_bit == b_bit
    if len(part2["a"]) < 5_000_000 and a % 4 == 0:
        part2["a"].append(a_bit)
    if len(part2["b"]) < 5_000_000 and b % 8 == 0:
        part2["b"].append(b_bit)

print(f"Part 1: {part1}")
print(f"Part 2: {sum(a == b for a, b in zip(part2["a"], part2["b"]))}")