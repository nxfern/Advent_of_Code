import sys
import re
from collections import deque, defaultdict

with open(sys.argv[1]) as f:
    queue = deque(f.read().splitlines())

bots: defaultdict[int, list[int]] = defaultdict(list)
bins: defaultdict[int, list[int]] = defaultdict(list)
part1 = -1
while queue:
    line = queue.popleft()
    if line.startswith("value"):
        v, b = map(int, re.findall(r"\d+", line))
        bots[b].append(v)
    else:
        g, v1, v2 = map(int, re.findall(r"\d+", line))
        if len(bots[g]) < 2:
            queue.append(line)
            continue
        lo, hi = sorted(bots[g])
        bots[g].clear()
        if "low to bot" in line:
            bots[v1].append(lo)
        else:
            bins[v1].append(lo)
        if "high to bot" in line:
            bots[v2].append(hi)
        else:
            bins[v2].append(hi)
    
    if part1 == -1:
        for bot, chips in bots.items():
            if sorted(chips) == [17, 61]:
                part1 = bot
                break

print(f"Part 1: {part1}")
print(f"Part 2: {bins[0][0] * bins[1][0] * bins[2][0]}")