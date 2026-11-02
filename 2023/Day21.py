import sys
from collections import deque
from itertools import product

def count_grid(r: int, c: int, s: int) -> int:
    queue = deque([(r, c, s)])
    seen = set()
    count = 0
    while queue:
        r, c, s = queue.popleft()

        if (r, c) in seen or s < 0:
            continue
        seen.add((r, c))
        if s % 2 == 0:
            count += 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] != "#":
                queue.append((nr, nc, s - 1))
    return count

with open(sys.argv[1]) as f:
    grid = f.read().splitlines()

size = len(grid)
assert size == len(grid[0])
assert all(c != "#" for c in grid[size // 2])
assert all(c != "#" for c in list(zip(*grid))[size // 2])

(start, ) = [(r, c) for r, c in product(range(size), repeat=2) if grid[r][c] == "S"]    # find start
print(f"Part 1: {count_grid(*start, s=64)}")

# Part 2
steps = 26501365
radius = steps // size

right_corner = count_grid(size // 2, 0, steps - (size // 2 + 1) - ((radius - 1) * size))
left_corner = count_grid(size // 2, size - 1, steps - (size // 2 + 1) - ((radius - 1) * size))
top_corner = count_grid(size - 1, size // 2, steps - (size // 2 + 1) - ((radius - 1) * size))
bottom_corner = count_grid(0, size // 2, steps - (size // 2 + 1) - ((radius - 1) * size))

odd_block = count_grid(0, 0, 2 * size + 11)
even_block = count_grid(0, 0, 2 * size + 10)

edge_top_right_out = count_grid(size - 1, 0, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))
edge_top_left_out = count_grid(size - 1, size - 1, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))
edge_bottom_right_out = count_grid(0, 0, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))
edge_bottom_left_out = count_grid(0, size - 1, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))

edge_top_right_in = count_grid(size - 1, 0, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))
edge_top_left_in = count_grid(size - 1, size - 1, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))
edge_bottom_right_in = count_grid(0, 0, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))
edge_bottom_left_in = count_grid(0, size - 1, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))

part2 = right_corner + left_corner + top_corner + bottom_corner
part2 += odd_block * pow(radius - 1, 2)
part2 += even_block * pow(radius, 2)
part2 += (edge_top_left_out + edge_bottom_left_out + edge_bottom_right_out + edge_top_right_out) * radius
part2 += (edge_top_left_in + edge_bottom_left_in + edge_bottom_right_in + edge_top_right_in) * (radius - 1)

print(f"Part 2: {part2}")