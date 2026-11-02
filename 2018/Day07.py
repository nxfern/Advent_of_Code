import sys
from collections import defaultdict

parents: defaultdict[str, set[str]] = defaultdict(set)
dependents: defaultdict[str, set[str]] = defaultdict(set)
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        prereq, step = line[5], line[36]
        parents[step].add(prereq)
        dependents[prereq].add(step)

base_time, time, n_workers = 60, 0, 5
in_progress: dict[str, int] = {}

all_steps = set(parents) | set(dependents)
available = sorted(s for s in all_steps if not parents[s])
result: list[str] = []

while available or in_progress:

    while available and len(in_progress) < n_workers:
        step = available.pop(0)
        in_progress[step] = time + base_time + (ord(step) - ord("A") + 1)

    time = min(in_progress.values())
    for step in sorted(k for k, v in in_progress.items() if v == time):
        result.append(step)
        del in_progress[step]

        for dep in dependents[step]:
            parents[dep].discard(step)
            if not parents[dep]:
                available.append(dep)

        available.sort()

print(f"Part 1: {"".join(result)}")
print(f"Part 2: {time}")