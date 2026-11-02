import sys

with open(sys.argv[1]) as f:
    p1, p2 = f.read().split("\n\n")
    p1 = list(map(int, p1.splitlines()[1:]))
    p2 = list(map(int, p2.splitlines()[1:]))

def combat(p1: list[int], p2: list[int], recursive: bool = False) -> tuple[bool, list[int]]:
    d1, d2 = p1.copy(), p2.copy()
    seen: set[tuple[int, ...]] = set()
    while d1 and d2:
        state = tuple(d1)
        if recursive and state in seen:
            return True, d1
        seen.add(state)

        c1, c2 = d1.pop(0), d2.pop(0)
        if recursive and c1 <= len(d1) and c2 <= len(d2):
            winner, _ = combat(d1[:c1], d2[:c2], recursive=True)
        else:
            winner = c1 > c2
        if winner:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])
    return len(d1) > len(d2), d1 if d1 else d2

print(f"Part 1: {sum(i*c for i, c in enumerate(combat(p1, p2)[1][::-1], 1))}")
print(f"Part 1: {sum(i*c for i, c in enumerate(combat(p1, p2, recursive=True)[1][::-1], 1))}")