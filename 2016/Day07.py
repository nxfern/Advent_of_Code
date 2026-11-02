import sys
import re

def is_abba(s: str) -> bool:
    return any(s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2] for i in range(len(s)-3))

def find_abas(s: str) -> list[str]:
    results: list[str] = []
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i] == s[i+2]:
            results.append(s[i:i+2])
    return results

def has_bab(hyp_segments: list[str], ab_pairs: list[str]) -> bool:
    return any(h[i] == h[i+2] and h[i] == ab[1] and h[i+1] == ab[0]
               for ab in ab_pairs
               for h in hyp_segments
               for i in range(len(h) - 2))

ips: list[tuple[list[str], list[str]]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        results = re.split(r"[\[\]]", line)
        ips.append((results[::2], results[1::2]))

part1 = part2 = 0
for (sup, hyp) in ips:
    part1 += any(is_abba(s) for s in sup) and not any(is_abba(h) for h in hyp)
    part2 += has_bab(hyp, [ab for s in sup for ab in find_abas(s)])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")