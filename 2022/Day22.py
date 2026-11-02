import sys, re
from math import isqrt

Faces = dict[tuple[int, int], dict[str, tuple[int, int, int]]]
Normal = dict[tuple[int, int, int], tuple[int, int]]

with open(sys.argv[1]) as f:
    grid_text, path_text = f.read().split("\n\n")
    lines = grid_text.splitlines()
    width = max(len(l) for l in lines)
    grid: dict[tuple[int, int], str] = {}
    for r, line in enumerate(lines):
        line = line.ljust(width)
        for c, ch in enumerate(line):
            if ch in ".#":
                grid[(r, c)] = ch
    reg: list[str] = re.findall(r"\d+|[LR]", path_text.strip())
    path = [int(p) if p.isdigit() else p for p in reg]

DR = {0: 0, 1: 1, 2: 0, 3: -1}   # E, S, W, N
DC = {0: 1, 1: 0, 2: -1, 3: 0}

def neg(v: tuple[int, int, int]) -> tuple[int, int, int]:
    return (-v[0], -v[1], -v[2])

def part1(grid: dict[tuple[int, int], str], path: list[int | str]) -> int:
    min_c, max_c, min_r, max_r = {}, {}, {}, {}
    for (r, c) in grid:
        min_c[r] = min(min_c.get(r, c), c); max_c[r] = max(max_c.get(r, c), c)
        min_r[c] = min(min_r.get(c, r), r); max_r[c] = max(max_r.get(c, r), r)

    row = min(r for r, c in grid if r == 0) and 0
    col = min(c for (r, c) in grid if r == 0)
    d = 0
    for step in path:
        if step == 'R':
            d = (d + 1) % 4
        elif step == 'L':
            d = (d - 1) % 4
        elif isinstance(step, int):
            for _ in range(step):
                dr, dc = DR[d], DC[d]
                nr, nc = row + dr, col + dc
                if (nr, nc) not in grid:
                    if dr == 0:
                        nc = min_c[row] if dc == 1 else max_c[row]
                    else:
                        nr = min_r[col] if dr == 1 else max_r[col]
                if grid[(nr, nc)] == '#':
                    break
                row, col = nr, nc
    return 1000 * (row + 1) + 4 * (col + 1) + d

def build_cube(grid: dict[tuple[int, int], str], L: int) -> tuple[Faces, Normal]:
    faces: Faces = {}
    face_blocks = {(r // L, c // L) for (r, c) in grid}
    start = min(face_blocks)
    faces[start] = {'n': (0, 0, 1), 'r': (1, 0, 0), 'd': (0, 1, 0)}

    stack = [start]
    seen = {start}
    while stack:
        fb = stack.pop()
        n, r, d = faces[fb]['n'], faces[fb]['r'], faces[fb]['d']
        fr, fc = fb
        for dirn, (nfb, trans) in {
            'E': ((fr, fc + 1), lambda n, r, d: (r, neg(n), d)),
            'W': ((fr, fc - 1), lambda n, r, d: (neg(r), n, d)),
            'S': ((fr + 1, fc), lambda n, r, d: (d, r, neg(n))),
            'N': ((fr - 1, fc), lambda n, r, d: (neg(d), r, n)),
        }.items():
            if nfb in face_blocks and nfb not in seen:
                nn, nr_, nd = trans(n, r, d)
                faces[nfb] = {'n': nn, 'r': nr_, 'd': nd}
                seen.add(nfb)
                stack.append(nfb)

    normal_to_face: Normal = {f['n']: fb for fb, f in faces.items()}
    return faces, normal_to_face

def cross_edge(faces: Faces, normal_to_face: Normal, fb: tuple[int, int], L: int, local_u: int, local_v: int, dirIdx: int) -> tuple[int, int, int]:
    f = faces[fb]
    n, r, d = f['n'], f['r'], f['d']
    facing3d = {0: r, 1: d, 2: neg(r), 3: neg(d)}[dirIdx]
    dest_fb = normal_to_face[facing3d]
    g = faces[dest_fb]
    n2, r2, d2 = g['n'], g['r'], g['d']
    new_facing3d = neg(n)

    if new_facing3d == r2:
        new_dir, perp_new = 0, d2
    elif new_facing3d == neg(r2):
        new_dir, perp_new = 2, d2
    elif new_facing3d == d2:
        new_dir, perp_new = 1, r2
    else:
        new_dir, perp_new = 3, r2
        
    if dirIdx in (0, 2):
        perp_old, val = d, local_v
    else:
        perp_old, val = r, local_u

    new_val = val if perp_old == perp_new else (L - 1 - val)

    if new_dir == 0:
        nu, nv = 0, new_val
    elif new_dir == 2:
        nu, nv = L - 1, new_val
    elif new_dir == 1:
        nu, nv = new_val, 0
    else:
        nu, nv = new_val, L - 1

    new_row = dest_fb[0] * L + nv
    new_col = dest_fb[1] * L + nu
    return new_row, new_col, new_dir

def part2(grid: dict[tuple[int, int], str], path: list[int | str]) -> int:
    L = isqrt(len(grid) // 6)
    faces, normal_to_face = build_cube(grid, L)

    start_fb = min(faces)
    col = min(c for (r, c) in grid if r == start_fb[0] * L)
    row = start_fb[0] * L
    d = 0

    for step in path:
        if step == 'R':
            d = (d + 1) % 4
        elif step == 'L':
            d = (d - 1) % 4
        elif isinstance(step, int):
            for _ in range(step):
                fb = (row // L, col // L)
                local_u, local_v = col % L, row % L
                dr, dc = DR[d], DC[d]
                nu, nv = local_u + dc, local_v + dr
                if 0 <= nu < L and 0 <= nv < L:
                    nr, nc, nd = fb[0] * L + nv, fb[1] * L + nu, d
                else:
                    nr, nc, nd = cross_edge(faces, normal_to_face, fb, L, local_u, local_v, d)
                if grid[(nr, nc)] == '#':
                    break
                row, col, d = nr, nc, nd
    return 1000 * (row + 1) + 4 * (col + 1) + d

print("Part 1:", part1(grid, path))
print("Part 2:", part2(grid, path))