import sys, re

machines: list[list[int]] = []
with open(sys.argv[1]) as f:
    for block in f.read().split("\n\n"):
        temp: list[int] = []
        for line in block.splitlines():
            temp.extend(list(map(int, re.findall(r"\d+", line))))
        machines.append(temp)

def buttons(Ax: int, Ay: int, Bx: int, By: int, Px: int, Py: int, p2: bool) -> int:
    Px += 10_000_000_000_000 if p2 else 0
    Py += 10_000_000_000_000 if p2 else 0
    if (D := Ax*By - Ay*Bx) == 0:
        return 0
    
    x = Px*By - Py*Bx
    y = Ax*Py - Ay*Px
    aq, ar = divmod(x, D)
    bq, br = divmod(y, D)
    return aq*3 + bq if ar + br == 0 else 0

print(f"Part 1: {sum(buttons(*m, p2=False) for m in machines)}")
print(f"Part 1: {sum(buttons(*m, p2=True) for m in machines)}")