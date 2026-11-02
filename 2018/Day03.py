import sys
import re
import numpy as np

fabric = np.zeros((1000, 1000), dtype=np.int64)
rectangles: list[tuple[int, int, int, int, int]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        r_id, x, y, w, h = list(map(int, re.findall(r"\d+", line)))
        rectangles.append((r_id, x, y, w, h))
        fabric[y:y+h, x:x+w] += 1

print(f"Part 1: {np.sum(fabric >= 2)}")

for r_id, x, y, w, h in rectangles:
    if np.all(fabric[y:y+h, x:x+w] == 1):
        print(f"Part 2: {r_id}")
        break