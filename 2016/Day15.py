import sys
import re
from math import prod

def crt(rem: list[int], mod: list[int]) -> int: # Chinese Remainder Theorem
    M = prod(mod)
    x = 0
    for r, m in zip(rem, mod):
        Mi = M // m
        x += r * Mi * pow(Mi, -1, m)
    return x % M

remainders: list[int] = []
moduli: list[int] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        disc, length, t, pos = map(int, re.findall(r"\d+", line))
        remainders.append(-(disc + pos) % length)
        moduli.append(length)

print(f"Part 1: {crt(remainders, moduli)}")

# Adding another disc per part 2 instructions
remainders.append(-(len(remainders)+ 1 + 0) % 11)
moduli.append(11)
print(f"Part 2: {crt(remainders, moduli )}")