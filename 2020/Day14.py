import sys
import re

memory1: dict[int, int] = {}
memory2: dict[int, int] = {}
mask = "X" * 36
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            a1, v = [int(n) for n in re.findall(r"\d+", line)]
            or_mask  = int(mask.replace("X", "0"), 2)
            and_mask = int(mask.replace("X", "1"), 2)
            memory1[a1] = (v | or_mask) & and_mask

            a2 = a1 | or_mask
            floating = [i for i, b in enumerate(reversed(mask)) if b == "X"]
            for c in range(1 << len(floating)):
                for b, p in enumerate(floating):
                    a2 = a2 | (1 << p) if c & (1 << b) else a2 & ~(1 << p)
                memory2[a2] = v

print(f"Part 1: {sum(memory1.values())}")
print(f"Part 2: {sum(memory2.values())}")