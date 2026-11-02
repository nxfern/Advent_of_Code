import sys
from functools import cache
from heapq import heappop, heappush

if len(sys.argv) != 3:
    sys.exit("Incorrect usage, please follow this format: python script.py <input_file> <buffer_size>")

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    DEPTH = int(lines[0].split()[1])
    TARGET = tuple(map(int, lines[1].split()[1].split(",")))
BUFFER = int(sys.argv[2])

@cache
def get_geo(x: int, y: int) -> int:
    if (x, y) == (0, 0) or (x, y) == TARGET:
        return 0
    elif x == 0:
        return y * 48271
    elif y == 0:
        return x * 16807
    else:
        return get_erosion(x-1, y) * get_erosion(x, y-1)
    
@cache
def get_erosion(x: int, y: int) -> int:
    return (get_geo(x, y) + DEPTH) % 20183

@cache
def get_region(x: int, y: int) -> int:
    return get_erosion(x, y) % 3

# Part 1
part1 = 0
for x in range(TARGET[0] + 1):
    for y in range(TARGET[1] + 1):
        part1 += get_region(x, y)

print(f"Part 1: {part1}")

# Part 2
TOOLS = {0: ["gear", "torch"], 1: ["gear", "none"], 2: ["torch", "none"]}
heap = [(0, 0, 0, "torch")] # time, x, y, tool
seen: dict[tuple[int, int, str], int] = {}

part2 = -1
while heap:
    time, x, y, tool = heappop(heap)
    if (x, y) == TARGET and tool == "torch":
        part2 = time
        break

    if (x, y, tool) in seen and seen[(x, y, tool)] <= time:
        continue

    seen[(x, y, tool)] = time

    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if not (0 <= nx <= TARGET[0] + BUFFER and 0 <= ny <= TARGET[1] + BUFFER):
            continue
        if tool in TOOLS[get_region(nx, ny)]:
            heappush(heap, (time+1, nx, ny, tool))
    
    for t in TOOLS[get_region(x, y)]:
        if t != tool:
            heappush(heap, (time+7, x, y, t))

print(f"Part 2: {part2}")