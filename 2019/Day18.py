import sys
from collections import deque

def patch_grid(grid: dict, pos: tuple[int,int]) -> list[tuple[int,int]]:
    x, y = pos
    for dx, dy in [(0,0),(0,-1),(1,0),(0,1),(-1,0)]:
        grid[(x+dx, y+dy)] = "#"
    new_entrances = []
    for dx, dy in [(-1,-1),(1,-1),(1,1),(-1,1)]:
        grid[(x+dx, y+dy)] = "@"
        new_entrances.append((x+dx, y+dy))
    return new_entrances

def bfs_from(
    start: tuple[int,int],
    grid: dict[tuple[int,int], str],
    keys: dict[str, tuple[int,int]]
) -> dict[str, tuple[int, frozenset[str]]]:
    """BFS from start; returns {key: (distance, doors_needed)} for all reachable keys."""
    reachable: dict[str, tuple[int, frozenset[str]]] = {}
    visited: set[tuple[int,int]] = {start}
    queue: deque[tuple[tuple[int,int], int, frozenset[str]]] = deque([(start, 0, frozenset())])

    while queue:
        pos, dist, doors_needed = queue.popleft()
        x, y = pos
        for nx, ny in [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]:
            npos = (nx, ny)
            if npos in visited or grid.get(npos, "#") == "#":
                continue
            visited.add(npos)
            cell = grid[npos]
            new_doors = doors_needed | {cell.lower()} if cell.isupper() else doors_needed
            if cell.islower():
                reachable[cell] = (dist + 1, new_doors)
            queue.append((npos, dist + 1, new_doors))

    return reachable

def build_graph(
    grid: dict,
    keys: dict[str, tuple[int,int]],
    entrances: list[tuple[int,int]]
) -> dict[str, dict[str, tuple[int, frozenset[str]]]]:
    graph: dict[str, dict[str, tuple[int, frozenset[str]]]] = {}
    for i, pos in enumerate(entrances):
        graph[f"@{i}"] = bfs_from(pos, grid, keys)
    for key, pos in keys.items():
        graph[key] = bfs_from(pos, grid, keys)
    return graph

def find_keys(
    graph: dict[str, dict[str, tuple[int, frozenset[str]]]],
    positions: tuple[str, ...],
    found: frozenset[str],
    all_keys: frozenset[str],
    cache: dict
) -> int:
    if found == all_keys:
        return 0

    cache_key = (positions, found)
    if cache_key in cache:
        return cache[cache_key]

    best = sys.maxsize
    for i, bot in enumerate(positions):
        for key, (steps, doors_needed) in graph[bot].items():
            if key in found:
                continue
            if not doors_needed.issubset(found):
                continue
            new_positions = positions[:i] + (key,) + positions[i+1:]
            result = steps + find_keys(graph, new_positions, found | {key}, all_keys, cache)
            if result < best:
                best = result

    cache[cache_key] = best
    return best


grid: dict[tuple[int,int], str] = {}
keys: dict[str, tuple[int,int]] = {}
entrances: list[tuple[int,int]] = []
with open(sys.argv[1]) as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, cell in enumerate(row):
            grid[(x, y)] = cell
            if cell == "@":         entrances.append((x, y))
            elif cell.islower():    keys[cell] = (x, y)

all_keys = frozenset(keys)

# Part 1
graph1 = build_graph(grid, keys, entrances)
starts1 = tuple(f"@{i}" for i in range(len(entrances)))
part1 = find_keys(graph1, starts1, frozenset(), all_keys, {})
print(f"Part 1: {part1}")

# Part 2
grid2 = dict(grid)
new_entrances = patch_grid(grid2, entrances[0])
graph2 = build_graph(grid2, keys, new_entrances)
starts2 = tuple(f"@{i}" for i in range(len(new_entrances)))
part2 = find_keys(graph2, starts2, frozenset(), all_keys, {})
print(f"Part 2: {part2}")