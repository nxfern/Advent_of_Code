import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def get_outputs(data: list[int], mem0: int = 1, inputs: list[int]|None = None) -> list[int]:
    prog = Computer(data)
    prog.mem[0] = mem0
    inputs = [] if inputs is None else inputs
    outputs: list[int] = []
    while not prog.halted:
        out = prog.run(inputs, feedback=True)
        if out is not None:
            outputs.append(out)

    return outputs

def is_scaffold(grid: list[str], r: int, c: int) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == "#"

grid = "".join(chr(o) for o in get_outputs(data)).splitlines()
part1 = 0
(y, x) = (dy, dx) = (0, 0)
DIRS: dict[str, tuple[int, int]] = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
for r in range(1, len(grid)-1):
    for c in range(1, len(grid[0])-1):
        if (ch := grid[r][c]) in DIRS:
            y, x = r, c
            dy, dx = DIRS[ch]
        if ch != "#":
            continue
        if all(is_scaffold(grid, ny, nx) for ny, nx in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]):
            part1 += r * c
print(f"Part 1: {part1}")

path: list[str] = []
while True:
    for turn, (ndy, ndx) in [("L", (-dx, dy)), ("R", (dx, -dy))]:
        if is_scaffold(grid, y+ndy, x+ndx):
            dy, dx = ndy, ndx
            steps = 0
            while is_scaffold(grid, y+dy, x+dx):
                y, x = y+dy, x+dx
                steps += 1
            path.append(turn + "," + str(steps))
            break
    else:
        break
# print(path)   # print statement used to display path and manually figure out pattern

A = path[0:4]
B = path[4:7]
C = path[11:15]
pattern = ["A", "B", "A", "C", "A", "B", "C", "B", "C", "B"]
inputs: list[int] = ([ord(c) for c in ",".join(pattern) + "\n"] +
                     [ord(c) for c in ",".join(A) + "\n"]       +
                     [ord(c) for c in ",".join(B) + "\n"]       +
                     [ord(c) for c in ",".join(C) + "\n"]       +
                     [ord("n"), ord("\n")]                      )

print(f"Part 2: {get_outputs(data, mem0=2, inputs=inputs)[-1]}")