import sys

with open(sys.argv[1]) as f:
    pos = sorted(map(int, f.read().split(",")))

def fuel(target: int) -> int:
    return sum(d * (d + 1) // 2 for p in pos if (d := abs(p - target)))

n = len(pos)
med = (pos[n//2] + pos[(n//2)+1]) // 2
mean = sum(pos) / n
print(f"Part 1: {sum(abs(c - med) for c in pos)}")
print(f"Part 2: {min(fuel(c) for c in [int(mean), int(mean) + 1])}")