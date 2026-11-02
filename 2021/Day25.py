import sys
import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    grid = np.array([list(row) for row in lines])
    east = grid == ">"
    south = grid == "v"

def step(east: np.ndarray, south: np.ndarray) -> tuple[np.ndarray, np.ndarray, bool]:
    empty = ~(east | south)    # --- move east herd ---
    can_move_e = east & np.roll(empty, -1, axis=1)      # target cell (r, c+1) is free
    new_east = (east & ~can_move_e) | np.roll(can_move_e, 1, axis=1)

    empty2 = ~(new_east | south)    # --- move south herd (against updated east, old south) ---
    can_move_s = south & np.roll(empty2, -1, axis=0)    # target cell (r+1, c) is free
    new_south = (south & ~can_move_s) | np.roll(can_move_s, 1, axis=0)

    moved = bool(can_move_e.any() or can_move_s.any())
    return new_east, new_south, moved

steps, moved = 0, True
while moved:
    east, south, moved = step(east, south)
    steps += 1

print(f"Answer: {steps}")