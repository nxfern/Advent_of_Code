import sys
import re
from collections import deque
from math import prod

class Monkey:
    def __init__(self, items: list[int], op: list[str], test: int, t: int, f: int) -> None:
        self.items = deque(items)
        self.inspections: int = 0
        self._op = op
        self.test = test
        self._cond: tuple[int, int] = (f, t)

    def __operation(self, item: int) -> int:
        op, v = self._op
        v = int(v) if v.isdigit() else item
        return item + v if op == "+" else item * v

    def throw(self, item: int, mod: int) -> tuple[int, int]:
        level = self.__operation(item)
        bored = level % mod if mod > 0 else level // 3
        res = bored % self.test == 0
        return self._cond[res], bored

p1_monkeys: list[Monkey] = []
p2_monkeys: list[Monkey] = []
with open(sys.argv[1]) as f:
    for block in f.read().split("\n\n"):
        lines = block.splitlines()
        items = list(map(int, re.findall(r"\d+", lines[1])))
        op = lines[2].split()[-2:]
        test = int(lines[3].split()[-1])
        t = int(lines[4].split()[-1])
        f = int(lines[5].split()[-1])
        p1_monkeys.append(Monkey(items=items, op=op, test=test, t=t, f=f))
        p2_monkeys.append(Monkey(items=items, op=op, test=test, t=t, f=f))

def rounds(monkeys: list[Monkey], n: int, mod: int = 0) -> int:
    for _ in range(n):
        for monkey in monkeys:
            while monkey.items:
                i, level = monkey.throw(monkey.items.popleft(), mod)
                monkeys[i].items.append(level)
                monkey.inspections += 1
    return prod(sorted([m.inspections for m in monkeys], reverse=True)[:2])

mod = prod(m.test for m in p2_monkeys)
print(f"Part 1: {rounds(p1_monkeys, 20)}")
print(f"Part 2: {rounds(p2_monkeys, 10_000, mod)}")