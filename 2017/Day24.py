import sys
from collections import defaultdict

ports: list[tuple[int, int]] = []
index: defaultdict[int, list[int]] = defaultdict(list)
with open(sys.argv[1]) as f:
    for i, line in enumerate(f.read().splitlines()):
        l, r = map(int, line.split("/"))
        ports.append((l, r))
        index[l].append(i)
        index[r].append(i)

def dfs(curr: int, used: set[int], length: int, strength: int) -> tuple[int, tuple[int,int]]:
    best_p1 = strength
    best_p2 = (length, strength)
    for i in index[curr]:
        if i not in used:
            l, r = ports[i]
            nc = r if l == curr else l
            used.add(i)
            p1, p2 = dfs(nc, used, length + 1, strength + l + r)
            best_p1 = max(best_p1, p1)
            best_p2 = max(best_p2, p2)
            used.remove(i)
    return best_p1, best_p2

part1, (_, part2) = dfs(0, set(), 0, 0)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")