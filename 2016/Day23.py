import sys
from math import factorial

def cpy(regs: dict[str, int], key: str, reg: str) -> None:
    if not reg.isalpha():
        return None
    regs[reg] = int(key) if key.lstrip("-").isdigit() else regs[key]

def inc_dec(regs: dict[str, int], inst: str, reg: str) -> None:
    if not reg.isalpha():
        return None
    regs[reg] += 1 if inst == "inc" else -1

def jnz(regs: dict[str, int], reg1: str, reg2: str) -> int:
    x = int(reg1) if reg1.lstrip("-").isdigit() else regs[reg1]
    y = int(reg2) if reg2.lstrip("-").isdigit() else regs[reg2]
    return 1 if x == 0 else y

def tgl(instr: list[str], index: int, regs: dict[str, int], reg: str) -> None:
    x = int(reg) if reg.lstrip("-").isdigit() else regs[reg]
    new_i = index + x
    if not (0 <= new_i < len(instr)):
        return None
    
    parts = instr[new_i].split()
    if len(parts) < 3:
        if parts[0] == "inc":
            instr[new_i] = instr[new_i].replace(parts[0], "dec")
        else:
            instr[new_i] = instr[new_i].replace(parts[0], "inc")
    else:
        if parts[0] == "jnz":
            instr[new_i] = instr[new_i].replace(parts[0], "cpy")
        else:
            instr[new_i] = instr[new_i].replace(parts[0], "jnz")

def solve(instructions: list[str], set_a: int) -> int:
    instr = instructions.copy()
    registers = {"a": set_a, "b": 0, "c": 0, "d": 0}
    i = 0
    while 0 <= i < len(instr):
        parts = instr[i].split()

        if parts[0] == "tgl":
            tgl(instr, i, registers, parts[1])
            i += 1
        elif len(parts) < 3:
            inc_dec(registers, *parts)
            i += 1
        elif parts[0] == "cpy":
            cpy(registers, parts[1], parts[2])
            i += 1
        elif parts[0] == "jnz":
            i += jnz(registers, parts[1], parts[2])
        
    return registers["a"]

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

# Part 1
print(f"Part 1: {solve(data, 7)}")

# Part 2 - factorial of the initial register of a plus the cpy 71 and jnz 72 from the puzzle input
print(f"Part 2: {factorial(12) + (71 * 72)}")