import sys

with open(sys.argv[1]) as f:
    blocks = f.read().split("\n\n")
    registers = [int(line.split()[-1]) for line in blocks[0].splitlines()]
    program = list(map(int, blocks[1].split()[-1].split(",")))

def run(a: int, b: int = 0, c: int = 0) -> list[int]:
    regs = [a, b, c]
    combo = lambda o: o if o <= 3 else regs[o - 4]
    ip, out = 0, []
    while ip < len(program) - 1:
        op, x = program[ip], program[ip + 1]
        if   op == 0: regs[0] >>= combo(x)
        elif op == 1: regs[1] ^= x
        elif op == 2: regs[1] = combo(x) % 8
        elif op == 3 and regs[0]:
            ip = x
            continue
        elif op == 4: regs[1] ^= regs[2]
        elif op == 5: out.append(combo(x) % 8)
        elif op == 6: regs[1] = regs[0] >> combo(x)
        elif op == 7: regs[2] = regs[0] >> combo(x)
        ip += 2
    return out

def find_a(a: int, i: int) -> int | None:
    if i < 0:
        return a
    for d in range(8):
        n = a * 8 + d
        if run(n) == program[i:] and (result := find_a(n, i - 1)) is not None:
            return result
    return None

print(f"Part 1: {','.join(map(str, run(*registers)))}")
print(f"Part 2: {find_a(0, len(program)-1)}")