import sys
from collections import defaultdict, deque
import re

rules: defaultdict[str, list[tuple[str, int]]] = defaultdict(list)
child_map: defaultdict[str, list[str]] = defaultdict(list)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parent, children = re.sub(r" bags?|\.", "", line).split(" contain ")
        for ele in children.split(", "):
            if not ele.startswith("no"):
                n, *words = ele.split()
                child = " ".join(words)
                rules[parent].append((child, int(n)))
                child_map[child].append(parent)

queue1: deque[str] = deque(["shiny gold"])
seen: set[str] = set()
while queue1:
    child = queue1.popleft()
    for parent in child_map[child]:
        if parent in seen:
            continue
        seen.add(parent)
        queue1.append(parent)

print(f"Part 1: {len(seen)}")

queue2: deque[tuple[str, int]] = deque([*rules["shiny gold"]])
part2 = 0
while queue2:
    bag, amount = queue2.popleft()
    part2 += amount
    for child, n in rules[bag]:
        queue2.append((child, amount*n))

print(f"Part 2: {part2}")