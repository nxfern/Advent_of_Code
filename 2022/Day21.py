import sys
import operator

monkeys = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        name, rest = line.split(":")
        parts = rest.split()
        monkeys[name] = int(parts[0]) if len(parts) == 1 else tuple(parts)

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
def resolve(name):
    value = monkeys[name]
    if isinstance(value, int):
        return value
    left, op, right = value
    return OPS[op](resolve(left), resolve(right))

def contains_humn(name):
    if name == "humn":
        return True
    value = monkeys[name]
    if isinstance(value, int):
        return False
    left, _, right = value
    return contains_humn(left) or contains_humn(right)

def solve(name, target):
    if name == "humn":
        return target
    left, op, right = monkeys[name]
    if contains_humn(left):
        r = resolve(right)
        if      op == "+": next_target = target - r
        elif    op == "-": next_target = target + r
        elif    op == "*": next_target = target // r
        else: next_target = target * r
        return solve(left, next_target)
    else:
        l = resolve(left)
        if      op == "+": next_target = target - l
        elif    op == "-": next_target = l - target
        elif    op == "*": next_target = target // l
        else: next_target = l // target
        return solve(right, next_target)

print(f"Part 1: {resolve('root')}")

left, _, right = monkeys["root"]
if contains_humn(left):
    print(f"Part 2: {solve(left, resolve(right))}")
else:
    print(f"Part 2: {solve(right, resolve(left))}")