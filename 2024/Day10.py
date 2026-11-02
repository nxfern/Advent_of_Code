import sys

topo: list[list[int]] = []
stack: list[tuple[int, int, tuple[int, int]]] = []
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        temp: list[int] = []
        for c, d in enumerate(row):
            n = int(d)
            temp.append(n)
            if n == 0:
                stack.append((r, c, (r, c)))
        topo.append(temp)

rows, cols = len(topo), len(topo[0])
score: set[tuple[int, int, tuple[int, int]]] = set()
rating = 0
while stack:
    r, c, start = stack.pop()
    if topo[r][c] == 9:
        score.add((r, c, start))
        rating += 1
        continue

    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if 0 <= nr < rows and 0 <= nc < cols and topo[nr][nc] == topo[r][c] + 1:
            stack.append((nr, nc, start))

print(f"Part 1: {len(score)}")
print(f"Part 2: {rating}")