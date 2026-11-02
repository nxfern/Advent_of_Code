import sys
from collections import deque
from itertools import cycle

Coord = tuple[int, int]
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def simulate_battle(grid: list[list[str]], elf_attack: int = 3) -> tuple[int, int]:
    units: dict[Coord, list] = {
        (y, x): [c, 200]
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c in "EG"
    }
    turns: dict[Coord, cycle] = {pos: cycle([-1j, 1, 1j]) for pos in units}

    def find_next_move(pos: Coord, kind: str) -> Coord | None:
        queue: deque[tuple[Coord, Coord | None]] = deque([(pos, None)])
        visited = {pos}
        while queue:
            cur, first = queue.popleft()
            for dy, dx in DIRS:
                nb = (cur[0] + dy, cur[1] + dx)
                if nb in visited or grid[nb[0]][nb[1]] == "#":
                    continue
                if nb in units:
                    if units[nb][0] != kind:
                        return first or cur
                    continue
                visited.add(nb)
                queue.append((nb, first or nb))
        return None

    rounds = 0
    while True:
        for pos in sorted(units):
            if pos not in units:
                continue
            kind, hp = units[pos]

            kinds = {u[0] for u in units.values()}
            if len(kinds) == 1:
                return rounds * sum(u[1] for u in units.values()), \
                       sum(1 for u in units.values() if u[0] == "E")

            # Move
            adj = [(pos[0]+dy, pos[1]+dx) for dy, dx in DIRS]
            if not any(nb in units and units[nb][0] != kind for nb in adj):
                nxt = find_next_move(pos, kind)
                if nxt:
                    units[nxt] = units.pop(pos)
                    turns[nxt] = turns.pop(pos)
                    pos = nxt
                    adj = [(pos[0]+dy, pos[1]+dx) for dy, dx in DIRS]

            # Attack
            enemies = [(pos[0]+dy, pos[1]+dx) for dy, dx in DIRS
                       if (pos[0]+dy, pos[1]+dx) in units
                       and units[(pos[0]+dy, pos[1]+dx)][0] != kind]
            if enemies:
                target = min(enemies, key=lambda p: (units[p][1], p))
                dmg = elf_attack if kind == "E" else 3
                units[target][1] -= dmg
                if units[target][1] <= 0:
                    del units[target]
                    del turns[target]

        rounds += 1

with open(sys.argv[1]) as f:
    grid = [list(row) for row in f.read().splitlines()]

initial_elves = sum(row.count("E") for row in grid)
outcome, _ = simulate_battle(grid)
print(f"Part 1: {outcome}")

for atk in range(4, 200):
    outcome, surviving = simulate_battle(grid, atk)
    if surviving == initial_elves:
        print(f"Part 2: {outcome}")
        break