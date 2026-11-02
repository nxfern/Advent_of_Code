import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    bios = list(map(int, f.read().split(",")))

print(f"Part 1: {Computer(bios).run(1)}")
print(f"Part 2: {Computer(bios).run(5)}")