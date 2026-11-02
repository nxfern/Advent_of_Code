import sys
from intcode import Computer

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def boost(val: int) -> int:
    prog = Computer(data)
    out = None
    while not prog.halted:
        result = prog.run([val] if out is None else [])
        if result is not None:  out = result
    return out if out else -1   # -1 indicates failure

print(f"Part 1: {boost(1)}")
print(f"Part 2: {boost(2)}")