import sys

regs = {chr(n): 0 for n in range(97, 105)}  # a through h
with open(sys.argv[1]) as f:
    lines = [l.split() for l in f.read().splitlines()]

def get_value(val: str) -> int:
    try:
        return int(val)
    except ValueError:
        return regs[val]

OPS = {
    "set": lambda x, y: get_value(y),
    "sub": lambda x, y: regs[x] - get_value(y),
    "mul": lambda x, y: regs[x] * get_value(y)
}
    
i = part1 = 0
while 0 <= i < len(lines):
    op, x, y = lines[i]
    part1 += op == "mul"
    if op == "jnz":
        if get_value(x) != 0:
            i += get_value(y)
            continue
    else:
        regs[x] = OPS[op](x, y)
    i += 1

print(f"Part 1: {part1}")

# Part 2 requires reverse engineering the puzzle input
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            return False
    return True

b, c, step = 109_900, 126_900, 17
print(f"Part 2: {sum(not is_prime(n) for n in range(b, c+1, step))}")