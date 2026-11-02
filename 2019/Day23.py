import sys
from intcode import Computer
from collections import deque

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))

def cat6(data: list[int], nat: bool = False) -> int:
    progs = [Computer(data[:]) for _ in range(50)]
    queues: list[deque[int]] = [deque([i]) for i in range(50)]
    outputs: list[list[int]] = [[] for _ in range(50)]
    nat_packet: tuple[int, int] | None = None
    last_nat: int | None = None

    while True:
        idle = True
        for i in range(50):
            inputs = list(queues[i]) or [-1]
            queues[i].clear()

            for inp in inputs:
                if (result := progs[i].run(inputs=inp, feedback=True)) is not None:
                    outputs[i].append(result)
                    idle = False

            if len(outputs[i]) >= 3:
                dest, x, y = outputs[i][:3]
                outputs[i] = outputs[i][3:]
                idle = False
                if dest == 255:
                    if not nat:
                        return y
                    nat_packet = (x, y)
                else:
                    queues[dest].extend([x, y])

        if nat and idle and nat_packet is not None:
            x, y = nat_packet
            if y == last_nat:
                return y
            last_nat = y
            queues[0].extend([x, y])

print(f"Part 1: {cat6(data)}")
print(f"Part 2: {cat6(data, nat=True)}")