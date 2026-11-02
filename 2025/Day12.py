import sys, re

with open(sys.argv[1]) as f:
    *sizes, spaces = f.read().split("\n\n")
    gifts = {int(k.strip(":")): "".join(v).count("#") for block in sizes for k, *v in [block.splitlines()]}
    regions = [(int(h) * int(w), list(map(int, q))) for line in spaces.splitlines() for h, w, *q in [re.findall(r"\d+", line)]]

print(f"Answer: {sum(sum(n * gifts[i] for i, n in enumerate(reqs)) < area * .85 for area, reqs in regions)}")   # .85 tested on example