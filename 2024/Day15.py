import sys

with open(sys.argv[1]) as f:
    top, moves = f.read().split("\n\n")
    moves = moves.replace("\n", "")

def part1(top: str, moves: str) -> int:
    W = top.index("\n")
    g = bytearray(top.replace("\n", ""), "ascii")
    pos = g.index(b"@")
    g[pos] = 46  # '.', the robot is tracked by index, not drawn
    delta = {"^": -W, "v": W, "<": -1, ">": 1}

    WALL, BOX = 35, 79
    for m in moves:
        d = delta[m]
        n = pos + d
        p = n
        while g[p] == BOX:
            p += d
        if g[p] == WALL:
            continue
        if p != n:  # push the chain: only the two ends change
            g[p] = BOX
            g[n] = 46
        pos = n

    return sum(100 * (i // W) + i % W for i, ch in enumerate(g) if ch == BOX)

def part2(top: str, moves: str) -> int:
    W = 2 * top.index("\n")
    wide = top.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    g = bytearray(wide.replace("\n", ""), "ascii")
    pos = g.index(b"@")
    g[pos] = 46
    delta = {"^": -W, "v": W, "<": -1, ">": 1}

    WALL, LEFT = 35, 91  # '#', '['
    for m in moves:
        d = delta[m]
        n = pos + d
        c = g[n]

        if c == 46:  # fast path: empty cell
            pos = n
            continue
        if c == WALL:
            continue

        if d == 1 or d == -1:
            p = n
            while g[p] in (91, 93):
                p += d
            if g[p] == WALL:
                continue
            if d == 1:
                g[n + 1 : p + 1] = g[n:p]
            else:
                g[p:n] = g[p + 1 : n + 1]
            g[n] = 46
            pos = n
            continue
        
        order = []
        seen = set()
        frontier = [n]
        ok = True
        while frontier and ok:
            nxt = []
            for cell in frontier:
                ch = g[cell]
                if ch == 46:
                    continue
                if ch == WALL:
                    ok = False
                    break
                left = cell if ch == LEFT else cell - 1
                if left in seen:
                    continue
                seen.add(left)
                order.append(left)
                nxt.append(left + d)
                nxt.append(left + d + 1)
            frontier = nxt
        if not ok:
            continue

        for left in reversed(order):  # farthest layer first, so nothing is overwritten
            g[left + d] = 91
            g[left + d + 1] = 93
            g[left] = 46
            g[left + 1] = 46
        pos = n

    return sum(100 * (i // W) + i % W for i, ch in enumerate(g) if ch == LEFT)

print(f"Part 1: {part1(top, moves)}")
print(f"Part 2: {part2(top, moves)}")