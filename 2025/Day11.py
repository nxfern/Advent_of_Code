import sys
from functools import cache

with open(sys.argv[1]) as f:
    conns = {k[:-1]: v for line in f.read().splitlines() for k, *v in [line.split()]}

@cache
def racks(node: str, reqs: frozenset[str] = frozenset()) -> int:
    reqs = reqs - {node}
    if node == "out":
        return 0 if reqs else 1
    return sum(racks(nxt, reqs) for nxt in conns[node])

print(f"Part 1: {racks("you")}")
print(f"Part 2: {racks("svr", frozenset(["dac", "fft"]))}")