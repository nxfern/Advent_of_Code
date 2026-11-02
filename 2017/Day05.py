import sys

with open(sys.argv[1]) as f:
    jumps = list(map(int, f.read().splitlines()))

def get_steps(jumps: list[int], p2: bool = False) -> int:
    i = offset = steps = 0
    while 0 <= i < len(jumps):
        offset = jumps[i]
        jumps[i] += -1 if p2 and offset >= 3 else 1
        i += offset
        steps += 1
    return steps

print(f"Part 1: {get_steps(jumps.copy())}")
print(f"Part 2: {get_steps(jumps.copy(), p2=True)}")