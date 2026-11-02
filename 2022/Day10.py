import sys

with open(sys.argv[1]) as f:
    program: list[str | int] = [l if l == "noop" else int(l.split()[-1]) for l in f.read().splitlines()]

cycle = part1 = 0
x = 1
signals = [20+i for i in range(0, 201, 40)]
part2: list[str] = []
for v in program:
    cycles = 1 if isinstance(v, str) else 2
    for _ in range(cycles):
        cycle += 1
        if cycle in signals:
            part1 += cycle * x

        col = (cycle - 1) % 40
        part2.append("#" if abs(col - x) <= 1 else ".")
        
    if isinstance(v, int):
        x += v

print(f"Part 1: {part1}")
for i in range(0, len(part2), 40):
    print("".join(part2[i:i+40]))