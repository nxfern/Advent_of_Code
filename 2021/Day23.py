import sys
from heapq import heappop, heappush

State = tuple[tuple[str, ...], tuple[tuple[str, ...], ...]]

LETTERS = "ABCD"
COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOM_COL = [2, 4, 6, 8]
HALLWAY_STOPS = [0, 1, 3, 5, 7, 9, 10]

def parse(lines: list[str], p2: bool) -> State:
    extra = ["DCBA", "DBAC"]
    room_lines = [lines[2]] + extra + [lines[-2]] if p2 else lines[2:-1]
    rooms: list[list[str]] = [[] for _ in range(4)]
    for line in room_lines:
        letters = [ch for ch in line if ch.isalpha()]
        for i, ch in enumerate(letters):
            rooms[i].append(ch)

    rooms_tuple = tuple(tuple(reversed(r)) for r in rooms)
    hallway = tuple(["."] * 11)
    return hallway, rooms_tuple

def clear_path(hallway: tuple[str, ...], c1: int, c2: int) -> bool:
    lo, hi = sorted((c1, c2))
    return all(hallway[c] == "." for c in range(lo, hi + 1) if c != c1)

def is_done(state: State, room_depth: int) -> bool:
    _, rooms = state
    return all(len(room) == room_depth and all(c == LETTERS[i] for c in room)
               for i, room in enumerate(rooms))

def neighbors(state: State, room_depth: int):
    hallway, rooms = state
    for i, room in enumerate(rooms):
        if not room or all(c == LETTERS[i] for c in room):
            continue  # empty or already settled: nothing useful to move
        ch = room[-1]
        col = ROOM_COL[i]
        steps_out = room_depth - len(room) + 1
        for target in HALLWAY_STOPS:
            if hallway[target] != "." or not clear_path(hallway, col, target):
                continue
            steps = steps_out + abs(target - col)
            new_hallway = list(hallway)
            new_hallway[target] = ch
            new_rooms = list(rooms)
            new_rooms[i] = room[:-1]

            yield (tuple(new_hallway), tuple(new_rooms)), steps * COST[ch]

    # Hallway -> Room
    for pos, ch in enumerate(hallway):
        if ch == ".":
            continue

        i = LETTERS.index(ch)
        room = rooms[i]
        col = ROOM_COL[i]

        if len(room) == room_depth or any(c != ch for c in room):
            continue  # full, or contains a foreign amphipod

        if not clear_path(hallway, pos, col):
            continue

        steps_in = room_depth - len(room)
        steps = abs(col - pos) + steps_in
        new_hallway = list(hallway)
        new_hallway[pos] = "."
        new_rooms = list(rooms)
        new_rooms[i] = room + (ch,)

        yield (tuple(new_hallway), tuple(new_rooms)), steps * COST[ch]

def solve(lines: list[str], depth: int, p2: bool = False) -> int:
    start = parse(lines, p2)
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        cost, state = heappop(pq)

        if is_done(state, depth):
            return cost
        
        if cost > dist.get(state, float("inf")):
            continue

        for nstate, move_cost in neighbors(state, depth):
            ncost = cost + move_cost
            if ncost < dist.get(nstate, float("inf")):
                dist[nstate] = ncost
                heappush(pq, (ncost, nstate))

    raise RuntimeError("no solution found")

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

print(f"Part 1: {solve(lines, 2)}")
print(f"Part 2: {solve(lines, 4, p2=True)}")