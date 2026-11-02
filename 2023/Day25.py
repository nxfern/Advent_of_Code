import sys
from collections import defaultdict, deque

adjacencies: defaultdict[str, set[str]] = defaultdict(set)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        key, nodes = line.split(": ")
        for node in nodes.split():
            adjacencies[key].add(node)
            adjacencies[node].add(key)

def max_flow_capped(source: str, sink: str, limit: int) -> tuple[int, dict[tuple[str, str], int]]:
    cap: defaultdict[tuple[str, str], int] = defaultdict(int)
    for u in adjacencies:
        for v in adjacencies[u]:
            cap[(u, v)] = 1  # unit capacity, undirected

    flow = 0
    while flow <= limit:
        parent: dict[str, str] = {source: ""}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            if u == sink:
                break
            for v in adjacencies[u]:
                if v not in parent and cap[(u, v)] > 0:
                    parent[v] = u
                    queue.append(v)
        if sink not in parent:
            break
        v = sink
        while parent[v] != "":
            u = parent[v]
            cap[(u, v)] -= 1
            cap[(v, u)] += 1
            v = u
        flow += 1
    return flow, cap

capped: dict[tuple[str, str], int] = {}
source = next(iter(adjacencies))
for sink in adjacencies:
    if sink == source:
        continue
    flow, capped = max_flow_capped(source, sink, 4)
    if flow == 3:
        break

visited = {source}
queue = deque([source])
while queue:
    u = queue.popleft()
    for v in adjacencies[u]:
        if v not in visited and capped[(u, v)] > 0:
            visited.add(v)
            queue.append(v)

total = len(adjacencies)
print(f"Answer: {len(visited) * (total - len(visited))}")