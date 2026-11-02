import sys
import re
from math import prod

fields: dict[str, tuple[int, int, int, int]] = {}
with open(sys.argv[1]) as f:
    ranges, ticket, nearby = f.read().split("\n\n")
    for line in ranges.splitlines():
        k, rngs = line.split(": ")
        a, b, c, d = map(int, re.findall(r"\d+", rngs))
        fields[k] = a, b, c, d
    ticket = list(map(int, ticket.splitlines()[1].split(",")))
    others = [list(map(int, line.split(","))) for line in nearby.splitlines()[1:]]

part1 = 0
valid: list[list[int]] = []
for o in others:
    for n in o:
        if not any(lo1 <= n <= hi1 or lo2<= n <= hi2 for lo1, hi1, lo2, hi2 in fields.values()):
            part1 += n
            break
    else:
        valid.append(o)

print(f"Part 1: {part1}")

possible: dict[str, set[int]] = {}
for k, (lo1, hi1, lo2, hi2) in fields.items():
    possible[k] = {
        i for i in range(len(valid[0]))
        if all(lo1 <= v[i] <= hi1 or lo2 <= v[i] <= hi2 for v in valid)
    }

assigned: dict[str, int] = {}
while possible:
    sole = {k: next(iter(v)) for k, v in possible.items() if len(v) == 1}
    for k, col in sole.items():
        assigned[k] = col
        del possible[k]
        for s in possible.values():
            s.discard(col)

print(f"Part 2: {prod(ticket[c] for k, c in assigned.items() if k.startswith("departure"))}")