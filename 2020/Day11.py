import sys

seats: set[complex] = set()
rows = cols = 0
with open(sys.argv[1]) as f:
    for r, row in enumerate(f.read().splitlines()):
        for c, ch in enumerate(row):
            if ch != ".":
                seats.add(complex(c, r))
            rows = max(rows, r+1)
            cols = max(cols, c+1)

def in_bounds(p: complex) -> bool:
    return 0 <= p.imag < rows and 0 <= p.real < cols

def get_neighbors(los: bool) -> dict[complex, list[complex]]:
    neighbors: dict[complex, list[complex]] = {}
    for p in seats:
        nbrs: list[complex] = []
        for d in [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]:
            np = p + d
            while in_bounds(np):
                if np in seats:
                    nbrs.append(np)
                    break
                if not los:
                    break
                np += d

        neighbors[p] = nbrs
    return neighbors

def simulate(neighbors: dict[complex, list[complex]], tolerance: int) -> int:
    occupied: set[complex] = set()
    while True:
        new_occupied: set[complex] = set()
        for p in seats:
            count = sum(n in occupied for n in neighbors[p])
            if p not in occupied:
                if count == 0:
                    new_occupied.add(p)
            else:
                if count < tolerance:
                    new_occupied.add(p)

        if new_occupied == occupied:
            return len(occupied)
        occupied = new_occupied

neighbors_p1 = get_neighbors(los=False)
print(f"Part 1: {simulate(neighbors_p1, tolerance=4)}")

neighbors_p2 = get_neighbors(los=True)
print(f"Part 2: {simulate(neighbors_p2, tolerance=5)}")