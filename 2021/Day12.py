import sys
from collections import defaultdict

paths: defaultdict[str, list[str]] = defaultdict(list)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        a, b = line.split("-")
        paths[a].append(b)
        paths[b].append(a)

visited: defaultdict[str, int] = defaultdict(int)
part1 = part2 = 0

def dfs(pos: str, once: bool) -> None:
    global part1, part2
    if pos == "end":
        part1 += once
        part2 += 1
        return
    for neighbor in paths[pos]:
        if neighbor == "start":
            continue
        new_once = once
        if neighbor.islower() and visited[neighbor]:
            if new_once:
                new_once = False
            else:
                continue
        visited[neighbor] += 1
        dfs(neighbor, new_once)
        visited[neighbor] -= 1  # backtrack

visited["start"] = 1
dfs("start", True)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")