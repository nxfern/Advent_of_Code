import sys
import numpy as np

target = int(sys.argv[1])
limit = target // 30

part1 = np.zeros(limit + 1, dtype=np.int64)
part2 = np.zeros(limit + 1, dtype=np.int64)
for elf in range(1, limit + 1):
    part1[elf::elf] += elf * 10
    part2[elf::elf][:50] += elf * 11

print(f"Part 1: {np.argmax(part1 >= target)}")
print(f"Part 2: {np.argmax(part2 >= target)}")