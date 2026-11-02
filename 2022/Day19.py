import sys
import re
from math import ceil, prod

def parse_blueprint(line: str) -> list[tuple[int, int, int]]:
    nums = list(map(int, re.findall(r"\d+", line)))
    return [(nums[1], 0, 0),        # ore robot: ore, clay, obsidian
            (nums[2], 0, 0),        # clay robot
            (nums[3], nums[4], 0),  # obsidian robot
            (nums[5], 0, nums[6])]  # geode robot

with open(sys.argv[1]) as f:
    blueprints = list(map(parse_blueprint, f.read().splitlines()))

def max_geodes(costs: list[tuple[int, int, int]], total_time: int) -> int:
    max_needed = [max(c[i] for c in costs) for i in range(3)]
    max_needed.append(10_000_000)  # no cap on geode robots
    best = 0

    def dfs(t, resources, robots):
        nonlocal best
        ub = resources[3] + robots[3] * t + t * (t - 1) // 2
        if ub <= best:
            return
        
        best = max(best, resources[3] + robots[3] * t)
        if t == 0:
            return

        for r in (3, 2, 1, 0):
            if robots[r] >= max_needed[r]:
                continue

            cost = costs[r]
            if any(cost[i] > 0 and robots[i] == 0 for i in range(3)):
                continue

            wait = 0
            for i in range(3):
                if cost[i] > resources[i]:
                    wait = max(wait, ceil((cost[i] - resources[i]) / robots[i]))

            new_t = t - wait - 1
            if new_t <= 0:
                continue

            new_resources = list(resources)
            new_robots = list(robots)
            for i in range(3):
                new_resources[i] += robots[i] * (wait + 1) - cost[i]
                new_resources[i] = min(new_resources[i], max_needed[i] * new_t)  # cap excess

            new_resources[3] += robots[3] * (wait + 1)
            new_robots[r] += 1
            dfs(new_t, tuple(new_resources), tuple(new_robots))

    dfs(total_time, (0, 0, 0, 0), (1, 0, 0, 0))
    return best

print(f"Part 1: {sum(i * max_geodes(c, 24) for i, c in enumerate(blueprints, 1))}")
print(f"Part 2: {prod(max_geodes(c, 32) for c in blueprints[:3])}")