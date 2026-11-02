import sys

def cpy(regs: dict[str, int], key: str, reg: str) -> None:
    regs[reg] = int(key) if key.isdigit() else regs[key]

def inc_dec(regs: dict[str, int], inst: str, reg: str) -> None:
    regs[reg] += 1 if inst == "inc" else -1

def solve(instructions: list[str], set_c: int = 0) -> int:
    registers = {"a": 0, "b": 2, "c": set_c, "d": 0}
    
    i = 0
    while 0 <= i < len(instructions):
        parts = instructions[i].split()

        if len(parts) < 3:
            inc_dec(registers, *parts)
            i += 1
        elif parts[0] == "cpy":
            cpy(registers, parts[1], parts[2])
            i += 1
        else:
            x = int(parts[1]) if parts[1].isdigit() else registers[parts[1]]
            i += 1 if x == 0 else int(parts[2])
    
    return registers["a"]

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

# Part 1
part1 = solve(data)
print(f"Part 1: {part1}")

# Part 2
part2 = solve(data, set_c=1)
print(f"Part 2: {part2}")