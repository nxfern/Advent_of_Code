import sys
from collections import deque

def spinlock(s: int) -> int:
    buffer = deque([0])
    for i in range(1, 2018):
        buffer.rotate(-s)
        buffer.append(i)
    return buffer[0]

with open(sys.argv[1]) as f:
    steps = int(f.read())

# Part 1
part1 = spinlock(steps)
print(f"Part 1: {part1}")

# Part 2
def after_zero(s: int) -> int:
    pos, val = 0, -1
    for i in range(1, 50_000_000):
        pos = (pos + s) % i + 1
        if pos == 1:
            val = i
    return val

part2 = after_zero(steps)
print(f"Part 2: {part2}")