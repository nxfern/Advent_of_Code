import sys
from math import lcm

network: dict[str, tuple[str, str]] = {}
with open(sys.argv[1]) as f:
    raw_moves, lines = f.read().split("\n\n")
    moves = tuple(map(int, list(raw_moves.translate(str.maketrans("LR", "01")))))
    for line in lines.splitlines():
        node, neighbors = line.split(" = ")
        n1, n2 = neighbors.strip("()").split(", ")
        network[node] = (n1, n2)

L = len(moves)
def navigate(pos: str, cond: str) -> int:
    steps = 0
    while not pos.endswith(cond):
        pos = network[pos][moves[steps%L]]
        steps += 1
    return steps

print(f"Part 1: {navigate("AAA", "ZZZ")}")
print(f"Part 2: {lcm(*[navigate(n, "Z") for n in network.keys() if n.endswith("A")])}")