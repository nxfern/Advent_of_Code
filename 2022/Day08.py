import sys

with open(sys.argv[1]) as f:
    FOREST = [list(map(int, row)) for row in f.read().splitlines()]
    ROWS, COLS = len(FOREST), len(FOREST[0])

def rays(r, c):
    left = FOREST[r][:c][::-1]
    right = FOREST[r][c+1:]
    up = [FOREST[i][c] for i in range(r-1, -1, -1)]
    down = [FOREST[i][c] for i in range(r+1, ROWS)]
    return left, right, up, down

def viewing_distance(cur, ray):
    count = 0
    for tree in ray:
        count += 1
        if tree >= cur:
            break
    return count

part1 = part2 = 0
for r in range(ROWS):
    for c in range(COLS):
        cur = FOREST[r][c]
        distances = [viewing_distance(cur, ray) for ray in rays(r, c)]

        if any(d == len(ray) for d, ray in zip(distances, rays(r, c))):
            part1 += 1

        score = distances[0] * distances[1] * distances[2] * distances[3]
        part2 = max(part2, score)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")