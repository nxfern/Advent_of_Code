import sys, heapq
from collections import defaultdict

walls: set[tuple[int, int]] = set()
start = end = (0, 0)
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            if ch == "#":
                walls.add((r, c))
            elif ch == "S":
                start = (r, c)
            elif ch == "E":
                end = (r, c)

start_state = (start, (0, 1))  # facing east
dist = {start_state: 0}
preds = defaultdict(list)
heap = [(0, start_state)]
best = None
end_states = []

while heap:
    score, state = heapq.heappop(heap)
    if score > dist[state]:
        continue  # stale heap entry
    if best is not None and score > best:
        break  # everything left is worse than the best path

    pos, d = state
    if pos == end:
        best = score
        end_states.append(state)

    r, c = pos
    dr, dc = d
    moves = [
        (score + 1, ((r + dr, c + dc), d)),
        (score + 1000, (pos, (dc, -dr))),
        (score + 1000, (pos, (-dc, dr))),
    ]
    for cost, nxt in moves:
        if nxt[0] in walls:
            continue
        old = dist.get(nxt)
        if old is None or cost < old:
            dist[nxt] = cost
            preds[nxt] = [state]  # strictly better: replace predecessors
            heapq.heappush(heap, (cost, nxt))
        elif cost == old:
            preds[nxt].append(state)  # tie: keep this predecessor too

seen = set(end_states)
stack = list(end_states)
while stack:
    state = stack.pop()
    for p in preds[state]:
        if p not in seen:
            seen.add(p)
            stack.append(p)

print(f"Part 1: {best}")
print(f"Part 2: {len({pos for pos, _ in seen})}")