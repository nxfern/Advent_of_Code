import sys
from functools import cache

NUMPAD = ["789", "456", "123", " 0A"]
DPAD = [" ^A", "<v>"]

def build_moves(layout: list[str]) -> dict[tuple[str, str], tuple[str, ...]]:
    pos = {ch: (r, c) for r, row in enumerate(layout) for c, ch in enumerate(row) if ch != " "}
    gap = next((r, c) for r, row in enumerate(layout) for c, ch in enumerate(row) if ch == " ")
    moves: dict[tuple[str, str], tuple[str, ...]] = {}
    for a, (r1, c1) in pos.items():
        for b, (r2, c2) in pos.items():
            v = ("v" if r2 > r1 else "^") * abs(r2 - r1)
            h = (">" if c2 > c1 else "<") * abs(c2 - c1)
            opts = set()
            if (r1, c2) != gap:   # horizontal first, corner at (r1, c2)
                opts.add(h + v + "A")
            if (r2, c1) != gap:   # vertical first, corner at (r2, c1)
                opts.add(v + h + "A")
            moves[(a, b)] = tuple(opts)
    return moves

NUM_MOVES = build_moves(NUMPAD)
DIR_MOVES = build_moves(DPAD)

@cache
def cost(seq: str, depth: int) -> int:
    if depth == 0:
        return len(seq)
    return sum(min(cost(opt, depth - 1) for opt in DIR_MOVES[(a, b)]) for a, b in zip("A" + seq, seq))

def complexity_length(code: str, robots: int) -> int:
    return sum(min(cost(opt, robots) for opt in NUM_MOVES[(a, b)]) for a, b in zip("A" + code, code))

with open(sys.argv[1]) as f:
    codes = [line for line in f.read().splitlines() if line.strip()]

print(f"Part 1: {sum(int(c[:-1]) * complexity_length(c, 2) for c in codes)}")
print(f"Part 2: {sum(int(c[:-1]) * complexity_length(c, 25) for c in codes)}")