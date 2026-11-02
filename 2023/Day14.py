import sys

State = tuple[tuple[str, ...], ...]

def tilt(grid: list[list[str]], direction: str) -> list[list[str]]:
    rows, cols = len(grid), len(grid[0])
    if direction in ("N", "S"):
        for c in range(cols):
            col = [grid[r][c] for r in range(rows)]
            parts = "".join(col).split("#")
            new_col = []
            for part in parts:
                rocks = part.count("O")
                dots = len(part) - rocks
                if direction == "N":
                    new_col.append("O" * rocks + "." * dots)
                else:  # "S"
                    new_col.append("." * dots + "O" * rocks)
            rebuilt = "#".join(new_col)
            for r in range(rows):
                grid[r][c] = rebuilt[r]

    else:  # "W" or "E"
        for r in range(rows):
            row = "".join(grid[r])
            parts = row.split("#")
            new_row = []
            for part in parts:
                rocks = part.count("O")
                dots = len(part) - rocks
                if direction == "W":
                    new_row.append("O" * rocks + "." * dots)
                else:  # "E"
                    new_row.append("." * dots + "O" * rocks)
            rebuilt = "#".join(new_row)
            grid[r] = list(rebuilt)

    return grid

def only_north(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]
    grid = tilt(grid, "N")
    return sum(i * row.count("O") for i, row in enumerate(reversed(grid), 1))
    
def total_load(data: str, cycles: int) -> int:
    
    def grid_state(matrix: list[list[str]]) -> State:
        return tuple(tuple(row) for row in matrix)
    
    grid = [list(row) for row in data.splitlines()]
    states: dict[State, int] = {}
    history: list[State] = []
    for cycle in range(1, cycles+1):
        for t in ["N", "W", "S", "E"]:
            grid = tilt(grid, t)
        
        state = grid_state(grid)
        if state in states:
            start = states[state]
            length = cycle - start
            end = start + ((cycles - start - 1) % length)
            final_grid = history[end]
            return sum(i * row.count("O") for i, row in enumerate(reversed(final_grid), 1))

        states[state] = cycle
        history.append(state)

    return -1   # Loop not found

with open(sys.argv[1]) as f:
    puzzle = f.read()

print(f"Part 1: {only_north(puzzle)}")
print(f"Part 2: {total_load(puzzle, cycles=1_000_000_000)}")