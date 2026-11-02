import sys

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIR_IDX = {d: i for i, d in enumerate(DIRS)}

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()

def step(grid: list[str], rows: int, cols: int, r: int, c: int, dr: int, dc: int) -> list[tuple[int, int, int, int]]:
    r, c = r + dr, c + dc
    if not (0 <= r < rows and 0 <= c < cols):
        return []
    nxt = [(0, 0)]
    match grid[r][c]:
        case "/": nxt = [(-dc, -dr)]
        case "\\": nxt = [(dc, dr)]
        case "|": nxt = [(dr, dc)] if dc == 0 else [(1, 0), (-1, 0)]
        case "-": nxt = [(dr, dc)] if dr == 0 else [(0, 1), (0, -1)]
        case ".": nxt = [(dr, dc)]
    return [(r, c, ndr, ndc) for ndr, ndc in nxt]

def energized(r, c, dr, dc):
    m = 0
    for nr, nc, ndr, ndc in step(grid, rows, cols, r, c, dr, dc):
        m |= mask[node(nr, nc, DIR_IDX[(ndr, ndc)])]
    return bin(m).count("1")

rows, cols = len(grid), len(grid[0])
n = rows * cols * 4
node = lambda r, c, d: (r * cols + c) * 4 + d
adj = [[node(nr, nc, DIR_IDX[(ndr, ndc)])
            for nr, nc, ndr, ndc in step(grid, rows, cols, r, c, dr, dc)]
        for r in range(rows) for c in range(cols) for dr, dc in DIRS]

index, low, on_stack, mask = [-1] * n, [0] * n, [False] * n, [0] * n
tstack, counter = [], 0
for s in range(n):
    if index[s] != -1:
        continue
    work = [(s, iter(adj[s]))]
    index[s] = low[s] = counter; counter += 1
    tstack.append(s); on_stack[s] = True

    while work:
        v, it = work[-1]
        for w in it:
            if index[w] == -1:
                index[w] = low[w] = counter; counter += 1
                tstack.append(w); on_stack[w] = True
                work.append((w, iter(adj[w])))
                break
            elif on_stack[w]:
                low[v] = min(low[v], index[w])
        else:
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp, m = [], 0
                while True:
                    w = tstack.pop(); on_stack[w] = False
                    comp.append(w); m |= 1 << (w // 4)
                    if w == v:
                        break
                for u in comp:
                    for w in adj[u]:
                        m |= mask[w]
                for u in comp:
                    mask[u] = m

starts = ([(r, -1, 0, 1) for r in range(rows)] + [(r, cols, 0, -1) for r in range(rows)]
            + [(-1, c, 1, 0) for c in range(cols)] + [(rows, c, -1, 0) for c in range(cols)])

print(f"Part 1: {energized(0, -1, 0, 1)}")
print(f"Part 2: {max(energized(*s) for s in starts)}")