import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def arcade(val: int|None = None) -> dict[tuple[int, int], int]:
    prog = Computer(data)
    prog.mem[0] = val if val is not None else prog.mem[0]
    grid: dict[tuple[int, int], int] = {}
    paddle = ball = 0
    while not prog.halted:
        joystick = (ball > paddle) - (ball < paddle)
        x = prog.run([joystick], feedback=True)
        y = prog.run([], feedback=True)
        t = prog.run([], feedback=True)
        if x is None or y is None or t is None:
            break
        paddle = x if t == 3 else paddle
        ball = x if t == 4 else ball
        grid[(x, y)] = t
    return grid

print(f"Part 1: {list(arcade().values()).count(2)}")
print(f"Part 2: {arcade(2)[(-1, 0)]}")