import sys
from intcode import Computer
from collections import defaultdict

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def painting(start_color: int) -> defaultdict[tuple[int, int], int]:
    robot = Computer(data)
    grid: defaultdict[tuple[int, int], int] = defaultdict(int)
    x, y, dx, dy = 0, 0, 0, 1
    grid[(x, y)] = start_color
    while not robot.halted:
        color = grid[(x, y)]
        paint = robot.run(color, feedback=True)
        turn = robot.run([], feedback=True)
        if paint is None or turn is None:
            break
        grid[(x, y)] = paint
        (dx, dy) = (-dy, dx) if turn == 0 else (dy, -dx)
        x += dx
        y += dy
    return grid

print(f"Part 1: {len(painting(0))}")

directions = painting(1)
min_x, min_y = 1000, 1000   # large numbers
max_x, max_y = 0, 0         # small numbers
for x, y in directions.keys():
    min_x, max_x = min(min_x, x), max(max_x, x)
    min_y, max_y = min(min_y, y), max(max_y, y)
for y in range(max_y, min_y - 1, -1):
    print(''.join('#' if directions[(x, y)] == 1 else '.' for x in range(min_x, max_x + 1)))