import sys
from functools import cache
from collections import Counter

nodes: dict[str, int] = {}
children: set[str] = set()
tree: dict[str, list[str]] = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = line.split(" -> ")
        node, weight = parts[0].split()
        nodes[node] = int(weight[1:-1])
        if len(parts) > 1:
            kids = parts[1].split(", ")
            children.update(kids)
            tree[node] = kids
        else:
            tree[node] = []

@cache
def total_weight(node: str) -> int:
    return nodes[node] + sum(total_weight(c) for c in tree[node])

def find_fix(node: str, expected: int) -> int:
    child_weights = [(c, total_weight(c)) for c in tree[node]]
    counts = Counter(w for _, w in child_weights)
    if len(counts) == 1:
        return expected - (total_weight(node) - nodes[node])
    
    odd_weight  = next(w for w, c in counts.items() if c == 1) 
    good_weight = next(w for w, c in counts.items() if c > 1) 
    odd_node    = next(n for n, w in child_weights if w == odd_weight)
    return find_fix(odd_node, good_weight)

root = (nodes.keys() - children).pop()
print(f"Part 1: {root}")
print(f"Part 2: {find_fix(root, total_weight(root))}")