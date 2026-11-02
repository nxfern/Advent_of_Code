import sys
import re

sensors: list[tuple[int, int, int, int, int]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        d = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, bx, by, d))

def part1(sensors: list[tuple[int, int, int, int, int]], row: int = 2_000_000) -> int:
    intervals = []
    beacons_on_row = set()
    for sx, sy, bx, by, d in sensors:
        if by == row:
            beacons_on_row.add(bx)
        remaining = d - abs(sy - row)
        if remaining >= 0:
            intervals.append((sx - remaining, sx + remaining))

    intervals.sort()
    merged = []
    for lo, hi in intervals:
        if merged and lo <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))

    covered = sum(hi - lo + 1 for lo, hi in merged)
    for bx in beacons_on_row:
        if any(lo <= bx <= hi for lo, hi in merged):
            covered -= 1
    return covered

def part2(sensors: list[tuple[int, int, int, int, int]], bound: int =4_000_000) -> int:
    pos_lines: set[int] = set()
    neg_lines: set[int] = set()
    for sx, sy, bx, by, d in sensors:
        r = d + 1
        pos_lines.add(sx - sy + r)
        pos_lines.add(sx - sy - r)
        neg_lines.add(sx + sy + r)
        neg_lines.add(sx + sy - r)

    def covered_by_any(x: int, y: int) -> int:
        return any(abs(x - sx) + abs(y - sy) <= d for sx, sy, *_ , d in sensors)

    for c1 in pos_lines:
        for c2 in neg_lines:
            if (c1 + c2) % 2 != 0:
                continue
            x = (c1 + c2) // 2
            y = (c2 - c1) // 2
            if 0 <= x <= bound and 0 <= y <= bound and not covered_by_any(x, y):
                return x * 4_000_000 + y
    return -1

print("Part 1:", part1(sensors))
print("Part 2:", part2(sensors))