import sys

with open(sys.argv[1]) as f:
    PROGRAM: dict[str, list[str]] = {}
    for line in f.read().splitlines():
        parts = line.split()
        target = parts[-1]
        src = parts[:-2]  # drop the '->' and target
        PROGRAM[target] = src

BITWISE = {
    "AND": lambda a, b: (a & b) & 0xFFFF,
    "OR": lambda a, b: (a | b) & 0xFFFF,
    "NOT": lambda a: (~a) & 0xFFFF,
    "LSHIFT": lambda a, b: (a << b) & 0xFFFF,
    "RSHIFT": lambda a, b: (a >> b) & 0xFFFF,
}

def run(wire: str, memo: dict[str, int]) -> int:
    if wire in memo:
        return memo[wire]
    try:
        return int(wire)
    except ValueError:
        pass

    src = PROGRAM[wire]
    if len(src) == 1:
        result = run(src[0], memo)
    elif len(src) == 2:
        result = BITWISE[src[0]](run(src[1], memo))
    else:
        result = BITWISE[src[1]](run(src[0], memo), run(src[2], memo))
    
    memo[wire] = result
    return result

part1 = run("a", {})
part2 = run("a", {"b": part1})

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")