import sys
from heapq import heappop, heappush

with open(sys.argv[1]) as f:
    cave = [list(map(int, line)) for line in f.read().splitlines()]

def get_risk(mult: int) -> int:
    rows, cols = len(cave), len(cave[0])
    heap = [(0, 0, 0)] # risk, r, c
    seen: set[tuple[int, int]] = {(0, 0)}
    
    while heap:
        risk, r, c = heappop(heap)
        if (r, c) == (rows * mult -1, cols * mult -1):
            return risk

        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < rows * mult and 0 <= nc < cols * mult and (nr, nc) not in seen:
                inc = (cave[nr % rows][nc % cols] + nr // rows + nc // cols - 1) % 9 + 1
                heappush(heap, (risk + inc, nr, nc))
                seen.add((nr, nc))
    return -1   # answer not found

print(f"Part 1: {get_risk(mult=1)}")
print(f"Part 2: {get_risk(mult=5)}")