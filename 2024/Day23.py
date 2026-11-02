import sys
from collections import defaultdict
from collections.abc import Iterator

network: defaultdict[str, set[str]] = defaultdict(set)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        a, b = line.split("-")
        network[a].add(b)
        network[b].add(a)

part1 = 0
for c1, conns in network.items():
    for c2 in conns:
        if c2 <= c1:
            continue
        for c3 in conns & network[c2]:
            part1 += c3 > c2 and "t" in (c1[0], c2[0], c3[0])

print(f"Part 1: {part1}")

def parties(net: dict[str, set[str]], r: set[str], p: set[str], x: set[str]) -> Iterator[set[str]]:
    if not p and not x:
        yield r
        return
    pivot = max(p | x, key=lambda v: len(net[v] & p))
    for v in p - net[pivot]:
        yield from parties(net, r | {v}, p & net[v], x & net[v])
        p = p - {v}
        x = x | {v}

part2 = max(parties(network, set(), set(network), set()), key=len)
print(f"Part 2: {",".join(sorted(part2))}")