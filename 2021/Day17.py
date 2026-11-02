import sys
import re
from math import ceil, sqrt

with open(sys.argv[1]) as f:
    nums = list(map(int, re.findall(r"-?\d+", f.read())))
    XRNG, YRNG = nums[:2], nums[2:]

vxmin, vxmax = ceil((-1 + sqrt(1 + 8 * XRNG[0])) / 2), XRNG[1]
vymin, vymax = YRNG[0], abs(YRNG[0]) - 1

print(f"Part 1: {vymax * abs(YRNG[0]) // 2}")

def is_hit(vx: int, vy: int) -> bool:
    x = y = 0
    while True:
        x += vx
        y += vy
        vx = max(0, vx-1)
        vy -= 1
        if XRNG[0] <= x <= XRNG[1] and YRNG[0] <= y <= YRNG[1]:
            return True
        elif x > XRNG[1] or y < YRNG[0]:
            return False

print(f"Part 2: {sum(is_hit(vx, vy) for vx in range(vxmin, vxmax+1) for vy in range(vymin, vymax+1))}")