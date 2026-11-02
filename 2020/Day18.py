import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

def tokenize(expr: str) -> list[str]:
    return [ch for ch in expr if ch != ' ']

def parse(tokens: list[str], pos: int, p2: bool = False) -> tuple[int, int]:
    val, pos = parse_add(tokens, pos, p2)
    while pos < len(tokens) and tokens[pos] in ('*', '+'):
        op = tokens[pos]
        if op == '+' and p2:
            break
        right, pos = parse_add(tokens, pos + 1, p2)
        val = val + right if op == '+' else val * right
    return val, pos

def parse_add(tokens: list[str], pos: int, p2: bool = False) -> tuple[int, int]:
    val, pos = parse_atom(tokens, pos, p2)
    while p2 and pos < len(tokens) and tokens[pos] == '+':
        right, pos = parse_atom(tokens, pos + 1, p2)
        val += right
    return val, pos

def parse_atom(tokens: list[str], pos: int, p2: bool = False) -> tuple[int, int]:
    if tokens[pos] == '(':
        val, pos = parse(tokens, pos + 1, p2)
        assert tokens[pos] == ')'
        return val, pos + 1
    else:
        return int(tokens[pos]), pos + 1

print(f"Part 1: {sum(parse(tokenize(line), 0)[0] for line in lines)}")
print(f"Part 2: {sum(parse(tokenize(line), 0, p2=True)[0] for line in lines)}")