import sys

WIDTH = 7
PART1_ROCKS = 2022
PART2_ROCKS = 1_000_000_000_000
ROCKS: list[list[tuple[int, int]]] = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

def can_place(shape: list[tuple[int, int]], x: int, y: int, occupied: set[tuple[int, int]]) -> bool:
    for dx, dy in shape:
        cx, cy = x + dx, y + dy
        if cx < 0 or cx >= WIDTH or cy < 1:
            return False
        if (cx, cy) in occupied:
            return False
    return True

with open(sys.argv[1]) as f:
    jets = f.read().strip()

n_jets = len(jets)
heights = [0] * WIDTH   # highest filled row in each column (0 = floor)
occupied: set[tuple[int, int]] = set()
top = jet_i = rock_i = extra_height = 0
seen: dict[tuple[int, int, tuple[int, ...]], tuple[int, int]] = {}  # (rock_type, jet_i % n_jets, profile) -> (rock_i, top)
cycles_applied = False

part1 = 0
while rock_i < PART2_ROCKS:
    shape = ROCKS[rock_i % 5]
    x, y = 2, top + 4

    while True:
        push = jets[jet_i % n_jets]
        jet_i += 1
        nx = x + (1 if push == '>' else -1)
        if can_place(shape, nx, y, occupied):
            x = nx
        if can_place(shape, x, y - 1, occupied):
            y -= 1
        else:
            break

    for dx, dy in shape:
        cx, cy = x + dx, y + dy
        occupied.add((cx, cy))
        if cy > heights[cx]:
            heights[cx] = cy
    top = max(heights)
    rock_i += 1

    if rock_i == PART1_ROCKS:
        part1 = top

    if not cycles_applied and rock_i > PART1_ROCKS:
        profile = tuple(top - h for h in heights)
        key = (rock_i % 5, jet_i % n_jets, profile)
        if key in seen:
            prev_rock_i, prev_top = seen[key]
            cycle_len = rock_i - prev_rock_i
            cycle_height = top - prev_top
            remaining = PART2_ROCKS - rock_i
            n_cycles = remaining // cycle_len
            extra_height = n_cycles * cycle_height
            rock_i += n_cycles * cycle_len
            cycles_applied = True   # only fast-forward once
        else:
            seen[key] = (rock_i, top)

print(f"Part 1: {part1}")
print(f"Part 2: {top + extra_height}")