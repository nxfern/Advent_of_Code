import sys
import re

with open(sys.argv[1]) as f:
    a, b = map(int, re.findall(r"\d+", f.read())[:2])   # first two numbers found

constant = a * b
target = 0
while target <= constant:
    target = (target << 2) | 2

print(f"Part 1: {target - constant}")