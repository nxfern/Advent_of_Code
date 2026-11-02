import sys

code: list[tuple[str, int]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        op, n = line.split()
        code.append((op, int(n)))

def execute(code: list[tuple[str, int]]) -> tuple[bool, int]:
    accumulator = i = 0
    executed: set[int] = set()
    while 0 <= i < len(code):
        if i in executed:
            return False, accumulator
        executed.add(i)
        op, arg = code[i]
        if op == "jmp":
            i += arg
            continue
        if op == "acc":
            accumulator += arg
        i += 1
    return True, accumulator

print(f"Part 1: {execute(code)[1]}")

flip: dict[str, str] = {"nop": "jmp", "jmp": "nop"}
changes: list[int] = [i for i, (o, n) in enumerate(code) if o in ["nop", "jmp"] and (o, n) != ("nop", 0)]
part2 = 0
while changes:
    i = changes.pop()
    updated_code = code.copy()
    updated_code[i] = flip[updated_code[i][0]], updated_code[i][1]
    fixed, accumulator = execute(updated_code)
    if fixed:
        part2 = accumulator

print(f"Part 2: {part2}")