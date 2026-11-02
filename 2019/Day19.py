import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def tractor(data: list[int], x: int, y: int) -> bool:
    prog = Computer(data)
    return prog.run(inputs=[x, y]) == 1

print(f"Part 1: {sum(tractor(data, x, y) for x in range(50) for y in range(50))}")

x, y = 0, 99
while True:
    while not tractor(data, x, y):  # checks if x is within beam
        x += 1
    if tractor(data, x+99, y-99):   # check if top right corner is within beam
        break
    y += 1                          # shift y down to try again

print(f"Part 2: {x * 10_000 + (y - 99)}")