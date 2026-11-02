import sys
from intcode import Computer
from itertools import permutations

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def amp(perm: tuple[int, int, int, int, int], feedback: bool=False) -> int:
    prog = Computer(data)
    best = 0
    for phases in permutations(perm):
        amps = [Computer(list(prog.mem.values())) for _ in range(5)]
        signal = 0
        inputs = [[phase] for phase in phases]
        inputs[0].append(signal)
        while not amps[4].halted:
            for i, amp in enumerate(amps):
                if (out := amp.run(inputs[i], feedback)) is not None:
                    inputs[(i+1) % 5].append(out)
                    signal = out
        best = max(best, signal)
    return best

print(f"Part 1: {amp((0, 1, 2, 3, 4))}")
print(f"Part 2: {amp((5, 6, 7, 8, 9), feedback=True)}")