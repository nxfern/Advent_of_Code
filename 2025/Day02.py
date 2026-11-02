import sys

with open(sys.argv[1]) as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

def mobius(n):
    res, d = 1, 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return 0
            res = -res
        d += 1
    return -res if n > 1 else res

part1 = part2 = 0
for lo, hi in ranges:
    for L in range(len(str(lo)), len(str(hi)) + 1):
        a = max(lo, 10 ** (L - 1))
        b = min(hi, 10 ** L - 1)
        if a > b:
            continue
        for p in range(1, L):
            if L % p:
                continue
            mu = mobius(L // p)
            if mu == 0 and not (L == 2 * p):
                continue
            R = (10 ** L - 1) // (10 ** p - 1)
            s_lo = max(-(-a // R), 10 ** (p - 1))   # ceil(a / R)
            s_hi = min(b // R, 10 ** p - 1)
            if s_lo > s_hi:
                continue
            total = R * (s_lo + s_hi) * (s_hi - s_lo + 1) // 2
            if L == 2 * p:
                part1 += total          # exactly two repeats
            if mu:
                part2 -= mu * total     # inclusion-exclusion over periods

print("Part 1:", part1)
print("Part 2:", part2)