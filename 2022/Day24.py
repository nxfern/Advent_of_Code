import sys
from math import lcm
from typing import Callable

walls: set[tuple[int, int]] = set()
blizzards: dict[str, set[tuple[int, int]]] = {
    "^": set(), "v": set(), "<": set(), ">": set()
}
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    rows, cols = len(lines) - 2, len(lines[0]) - 2
    start, goal = (-1, lines[0].index(".") - 1), (rows, lines[-1].index(".") - 1)
    for r, row in enumerate(lines, start=-1):
        for c, ch in enumerate(row, start=-1):
            if ch in blizzards:
                blizzards[ch].add((r, c))
            elif ch == "#":
                walls.add((r, c))

MOVES = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
DIRS: dict[str, Callable[[int, int, int], tuple[int, int]]] = {
    "^": lambda r, c, t: ((r - t) % rows, c),
    "v": lambda r, c, t: ((r + t) % rows, c),
    "<": lambda r, c, t: (r, (c - t) % cols),
    ">": lambda r, c, t: (r, (c + t) % cols),
}

period = lcm(rows, cols)
occupied_cache: dict[int, set[tuple[int, int]]] = {}
def occupied(t: int) -> set[tuple[int, int]]:
    t %= period
    if t not in occupied_cache:
        occ = set()
        for d, storms in blizzards.items():
            for sr, sc in storms:
                occ.add(DIRS[d](sr, sc, t))
        occupied_cache[t] = occ
    return occupied_cache[t]

def in_bounds(r: int, c: int) -> bool:
    return (r, c) in (start, goal) or (0 <= r < rows and 0 <= c < cols)

def shortest_path(start: tuple[int, int], goal: tuple[int, int], t0: int) -> int:
    frontier = {start}
    t = t0
    while goal not in frontier:
        t += 1
        occ = occupied(t)
        frontier = {
            (r + dr, c + dc)
            for r, c in frontier
            for dr, dc in MOVES
            if in_bounds(r + dr, c + dc)
            and (r + dr, c + dc) not in walls
            and (r + dr, c + dc) not in occ
        }
    return t

leg1 = shortest_path(start, goal, 0)
leg2 = shortest_path(goal, start, leg1)
leg3 = shortest_path(start, goal, leg2)

print(f"Part 1: {leg1}")
print(f"Part 2: {leg3}")