import sys, re
from collections import defaultdict, deque

with open(sys.argv[1]) as f:
    bricks = sorted([tuple(map(int, re.findall(r"\d+", line))) for line in f.read().splitlines()], key=lambda b: b[2])

def overlaps(b1: tuple[int, ...], b2: tuple[int, ...]) -> bool:
    return max(b1[0], b2[0]) <= min(b1[3], b2[3]) and max(b1[1], b2[1]) <= min(b1[4], b2[4])

settled: list[tuple[int, ...]] = []
parents: defaultdict[int, set[int]] = defaultdict(set)
children: defaultdict[int, set[int]] = defaultdict(set)
for i, brick in enumerate(bricks):
    x1, y1, z1, x2, y2, z2 = brick
    height = z2 - z1
    max_top = 0
    resting_on: list[int] = []
    for j, s in enumerate(settled):
        if overlaps(brick, s):
            s_top = s[5]
            if s_top > max_top:
                max_top = s_top
                resting_on = [j]
            elif s_top == max_top:
                resting_on.append(j)
    nz1 = max_top + 1
    nz2 = nz1 + height
    settled.append((x1, y1, nz1, x2, y2, nz2))
    for k in resting_on:
        parents[k].add(i)
        children[i].add(k)

part2 = 0
L = len(bricks)
support_count = {i: len(children[i]) for i in range(L)}
for k in range(L):
    rem = dict(support_count)
    queue = deque([k])
    fallen: set[int] = set()
    while queue:
        cur = queue.popleft()
        fallen.add(cur)
        for j in parents[cur]:
            rem[j] -= 1
            if rem[j] == 0:
                queue.append(j)
    part2 += len(fallen) - 1

print(f"Part 1: {sum(all(len(children[i]) > 1 for i in parents[k]) for k in range(L))}")
print(f"Part 2: {part2}")