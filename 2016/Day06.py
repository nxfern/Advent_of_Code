import sys
from collections import Counter

with open(sys.argv[1]) as f:
    transposed = list(map(Counter, zip(*f.read().splitlines())))

print(f"Part 1: {"".join(line.most_common()[0][0] for line in transposed)}")
print(f"Part 2: {"".join(line.most_common()[-1][0] for line in transposed)}")