import sys
from collections import defaultdict

DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
ALL = tuple(DIRS.values())

def solve(grid: list[str], slippery: bool) -> int:
    H, W = len(grid), len(grid[0])
    start = (0, grid[0].index("."))
    end = (H - 1, grid[-1].index("."))

    def neighbors(p: tuple[int, int]) -> list[tuple[int, int]]:
        r, c = p
        if slippery and grid[r][c] in DIRS:
            dr, dc = DIRS[grid[r][c]]
            return [(r + dr, c + dc)]
        return [(r + dr, c + dc) for dr, dc in ALL
                if 0 <= r + dr < H and 0 <= c + dc < W and grid[r + dr][c + dc] != "#"]
    
    nodes = set()
    for r in range(H):
        for c in range(W):
            if grid[r][c] == "#":
                continue

            p = (r, c)
            degree = len(neighbors(p))
            if p in (start, end) or degree != 2:
                nodes.add(p)

    graph = defaultdict(list)
    for node in nodes:
        for nxt in neighbors(node):
            prev, cur = node, nxt
            dist = 1
            while cur not in nodes:
                options = [p for p in neighbors(cur) if p != prev]
                if not options:
                    break

                prev, cur = cur, options[0]
                dist += 1

            if cur in nodes:
                graph[node].append((cur, dist))

    def dfs(node: tuple[int, int], seen: set[tuple[int, int]], distance: int, best: int) -> int:
        if node == end:
            return max(best, distance)

        for nxt, weight in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                best = dfs(nxt, seen, distance + weight, best)
                seen.remove(nxt)
                
        return best

    return dfs(start, {start}, 0, 0)

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()

print(f"Part 1: {solve(grid, slippery=True)}")
print(f"Part 2: {solve(grid, slippery=False)}")