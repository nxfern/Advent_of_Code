import re
import sys

sys.setrecursionlimit(3000)

def simulate(clay: set[tuple[int, int]]) -> tuple[int, int]:
    min_y = min(y for _, y in clay)
    max_y = max(y for _, y in clay)
    water: dict[tuple[int, int], str] = {}

    def blocked(x: int, y: int) -> bool:
        return (x, y) in clay or water.get((x, y)) == '~'

    def flow(x: int, y: int) -> None:
        if y > max_y:
            return  # out of bounds — water falls off the bottom

        if (x, y) in water:
            return  # already visited this cell

        water[(x, y)] = '|'  # mark as flowing
        if not blocked(x, y + 1):
            flow(x, y + 1)

        if blocked(x, y + 1):
            fill(x, y)

    def fill(x: int, y: int) -> bool:
        leftx = x
        while not blocked(leftx - 1, y):
            leftx -= 1
            water[(leftx, y)] = '|'
            if not blocked(leftx, y + 1):
                flow(leftx, y + 1)
                if not blocked(leftx, y + 1):
                    break   # water fell off this side — row is open on the left

        rightx = x
        while not blocked(rightx + 1, y):
            rightx += 1
            water[(rightx, y)] = '|'
            if not blocked(rightx, y + 1):
                flow(rightx, y + 1)
                if not blocked(rightx, y + 1):
                    break   # water fell off this side — row is open on the right

        left_bounded = blocked(leftx - 1, y)
        right_bounded = blocked(rightx + 1, y)

        if left_bounded and right_bounded:
            for cx in range(leftx, rightx + 1):
                water[(cx, y)] = '~'
            return True
        return False

    flow(500, 0)

    part1, part2 = 0, 0
    for (_, y), v in water.items():
        if min_y <= y <= max_y:
            part1 += 1
            if v == "~":
                part2 += 1

    return part1, part2

with open(sys.argv[1]) as f:
    clay: set[tuple[int, int]] = set()
    for line in f.read().splitlines():
        nums = list(map(int, re.findall(r'\d+', line)))
        if line.startswith('x'):
            x, y1, y2 = nums
            for y in range(y1, y2 + 1):
                clay.add((x, y))
        else:
            y, x1, x2 = nums
            for x in range(x1, x2 + 1):
                clay.add((x, y))

part1, part2 = simulate(clay)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")