import sys

with open(sys.argv[1]) as f:
    instructions = f.read().splitlines()

OPS = {
    "hlf": lambda r: r // 2,
    "tpl": lambda r: r * 3,
    "inc": lambda r: r + 1
}

def debug(reg_a: int) -> int:
    regs: dict[str, int] = {"a": reg_a, "b": 0}
    i = 0
    while 0 <= i < len(instructions):
        parts = instructions[i].split()
        if parts[0] == "jmp":
            i += int(parts[1])
            continue
        elif parts[0] == "jie":
            if regs[parts[1].strip(",")] % 2 == 0:
                i += int(parts[2])
                continue
        elif parts[0] == "jio":
            if regs[parts[1].strip(",")] == 1:
                i += int(parts[2])
                continue
        else:
            regs[parts[1]] = OPS[parts[0]](regs[parts[1]])
        i += 1
    return regs["b"]

print(f"Part 1: {debug(reg_a=0)}")
print(f"Part 2: {debug(reg_a=1)}")