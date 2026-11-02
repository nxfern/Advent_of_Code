import sys

def spin(s: list[str], n: int, *args) -> list[str]:
    return s[-n:] + s[:-n]

def exchange(s: list[str], i: int, j: int) -> list[str]:
    s[i], s[j] = s[j], s[i]
    return s

def partner(s: list[str], a: str, b: str) -> list[str]:
    i, j = s.index(a), s.index(b)
    return exchange(s, i, j)

moves = {"s": spin, "x": exchange, "p": partner}
DANCE: list[tuple[str, int | str, int | str]] = []
with open(sys.argv[1]) as f:
    for d in f.read().split(","):
        if d[0] == "p":
            m, (i, j) = d[0], d[1:].split("/")
        else:
            m, (i, j) = d[0], (list(map(int, d[1:].split("/"))) + [0])[:2]
        DANCE.append((m, i, j))

seq = [chr(i) for i in range(97, 113)]
seen = dict()
states = []
part1 = part2 = ""
for s in range(1_000_000_000):
    state = "".join(seq)
    if s == 1:
        part1 = state
    if state in seen:
        cycle_start = seen[state]
        cycle_length = s - cycle_start
        part2 = states[cycle_start + (1_000_000_000 - cycle_start) % cycle_length]
        break

    seen[state] = s
    states.append(state)
    for m, i, j in DANCE:
        seq = moves[m](seq, i, j)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")