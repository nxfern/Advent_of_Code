import sys
from collections import defaultdict, deque

regs: defaultdict[str, int] = defaultdict(int)
with open(sys.argv[1]) as f:
    instructions = [tuple((line.split()+[""])[:3]) for line in f.read().splitlines()]

def get_val(r: defaultdict[str, int], v: str) -> int:
        try:
            return int(v)
        except ValueError:
            return r[v]

OPS = {
    "set": lambda r, x, y: get_val(r, y),
    "add": lambda r, x, y: r[x] + get_val(r, y),
    "mul": lambda r, x, y: r[x] * get_val(r, y),
    "mod": lambda r, x, y: r[x] % get_val(r, y),
}

i = last = part1 = 0
while 0 <= i < len(instructions):
    op, x, y = instructions[i]
    if op == "jgz":
        i += get_val(regs, y) if get_val(regs, x) > 0 else 1
        continue
    elif op == "snd":
        last = get_val(regs, x)
    elif op == "rcv":
        if get_val(regs, x) != 0:
            part1 = last
            break
    else:
        regs[x] = OPS[op](regs, x, y)
    i += 1

print(f"Part 1: {part1}")

class Program:
    def __init__(self, pid: int, instructions):
        self.regs = defaultdict(int)
        self.regs["p"] = pid
        self.instructions = instructions
        self.i = 0
        self.queue: deque[int] = deque()
        self.waiting = False
        self.send_count = 0

    def step(self, other: "Program") -> bool:
        """Execute one instruction. Returns False if blocked or finished."""
        if not (0 <= self.i < len(self.instructions)):
            return False
        op, x, y = self.instructions[self.i]
        if op == "rcv":
            if not self.queue:
                self.waiting = True
                return False
            self.waiting = False
            self.regs[x] = self.queue.popleft()
        elif op == "snd":
            other.queue.append(get_val(self.regs, x))
            self.send_count += 1
        elif op == "jgz":
            self.i += get_val(self.regs, y) - 1 if get_val(self.regs, x) > 0 else 0
        else:
            self.regs[x] = OPS[op](self.regs, x, y)
        self.i += 1
        return True

p0 = Program(0, instructions)
p1 = Program(1, instructions)

while True:
    ran0 = p0.step(p1)
    ran1 = p1.step(p0)
    if not ran0 and not ran1:
        break  # both blocked or terminated

print(f"Part 2: {p1.send_count}")