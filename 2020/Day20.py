import sys
from collections import defaultdict
from math import prod

class Tile:
    def __init__(self, tile_id: int, data: list[str]) -> None:
        self.id = tile_id
        self.data = data

    def rotate(self) -> "Tile":
        rotated = [''.join(row) for row in zip(*self.data[::-1])]
        return Tile(self.id, rotated)

    def flip(self) -> "Tile":
        flipped = [row[::-1] for row in self.data]
        return Tile(self.id, flipped)

    def all_orientations(self) -> list["Tile"]:
        variants: list["Tile"] = []
        t = self
        for _ in range(4):
            variants.append(t)
            variants.append(t.flip())
            t = t.rotate()

        seen: dict[tuple[str, ...], "Tile"] = {}
        for v in variants:
            key = tuple(v.data)
            if key not in seen:
                seen[key] = v
        return list(seen.values())

    def edges(self) -> list[str]:
        top = self.data[0]
        bottom = self.data[-1]
        left = ''.join(row[0] for row in self.data)
        right = ''.join(row[-1] for row in self.data)
        return [top, right, bottom, left]

def parse_tiles(blocks: list[str]) -> dict[int, Tile]:
    tiles: dict[int, "Tile"] = {}
    for block in blocks:
        lines = block.splitlines()
        tid = int(lines[0].split()[1][:-1])
        tiles[tid] = Tile(tid, lines[1:])
    return tiles

def find_corners(tiles: dict[int, Tile]) -> tuple[list[int], dict[int, set[int]]]:
    edge_map = defaultdict(list)
    for tid, tile in tiles.items():
        for e in tile.edges():
            edge_map[e].append(tid)
            edge_map[e[::-1]].append(tid)
    neighbors = defaultdict(set)
    for e, tids in edge_map.items():
        if len(tids) == 2:
            a,b = tids
            neighbors[a].add(b)
            neighbors[b].add(a)
    corners = [tid for tid, neigh in neighbors.items() if len(neigh)==2]
    return corners, neighbors

def assemble_image(tiles: dict[int, Tile], neighbors: dict[int, set[int]]) -> list[list[Tile]]:
    N = int(len(tiles)**0.5)
    corners, _ = find_corners(tiles)
    start = tiles[corners[0]]

    # orient so matching edges on right and bottom
    grid: list[list[Tile]] = []
    for orient in start.all_orientations():
        right, bottom = orient.edges()[1], orient.edges()[2]
        if sum(1 for e in edge_map_lookup(tiles, right) if e!=orient.id)==1 \
           and sum(1 for e in edge_map_lookup(tiles, bottom) if e!=orient.id)==1:
            grid = [[orient]]
            break

    # fill first row
    placed = {grid[0][0].id}
    for x in range(1, N):
        left_tile = grid[0][x-1]
        needed = left_tile.edges()[1]
        for tid in neighbors[left_tile.id]:
            if tid in placed: continue
            for orient in tiles[tid].all_orientations():
                if orient.edges()[3] == needed:
                    grid[0].append(orient)
                    placed.add(tid)
                    break
            else:
                continue
            break

    # fill rest rows
    for y in range(1, N):
        grid.append([])
        for x in range(N):
            above = grid[y-1][x]
            needed = above.edges()[2]
            for tid in neighbors[above.id]:
                if tid in placed: continue
                for orient in tiles[tid].all_orientations():
                    if orient.edges()[0] == needed:
                        grid[y].append(orient)
                        placed.add(tid)
                        break
                else:
                    continue
                break
    return grid

def edge_map_lookup(tiles: dict[int, Tile], edge: str) -> list[int]:
    # returns tile ids having that edge or its reverse
    res = []
    for t in tiles.values():
        if edge in t.edges() or edge[::-1] in t.edges():
            res.append(t.id)
    return res

def build_full_image(grid: list[list[Tile]]) -> list[str]:
    rows = []
    for tile_row in grid:
        inner_rows = ['']*(len(tile_row[0].data)-2)
        for tile in tile_row:
            for i, row in enumerate(tile.data[1:-1]):
                inner_rows[i] += row[1:-1]
        rows.extend(inner_rows)
    return rows

SEA_MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

monster_offsets = [(dy, dx)
    for dy, row in enumerate(SEA_MONSTER)
    for dx, ch in enumerate(row) if ch == '#'
]

def count_monsters(img):
    count = 0
    h, w = len(img), len(img[0])
    for y in range(h - len(SEA_MONSTER) + 1):
        for x in range(w - len(SEA_MONSTER[0]) + 1):
            if all(img[y+dy][x+dx] == '#' for dy,dx in monster_offsets):
                count += 1
    return count

def water_roughness(full_img):
    total_hash = sum(row.count('#') for row in full_img)
    for orient in Tile(0, full_img).all_orientations():
        c = count_monsters(orient.data)
        if c:
            return total_hash - c * len(monster_offsets)
    return None

with open(sys.argv[1]) as f:
    puzzle = f.read().split("\n\n")

TILES = parse_tiles(puzzle)
CORNERS, NEIGHBORS = find_corners(TILES)

# Part 1
print(f"Part 1: {prod(CORNERS)}")

# Part 2
grid = assemble_image(TILES, NEIGHBORS)
full = build_full_image(grid=grid)
print(f"Part 2: {water_roughness(full)}")