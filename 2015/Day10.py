import sys

def look_and_say(seq: str, steps: int) -> int:
    for _ in range(steps):
        last = seq[0]
        count = 1
        result = []
        for digit in seq[1:]:
            if digit == last:
                count += 1
                continue
            result.extend([str(count), last])
            last = digit
            count = 1
        result.extend([str(count), last])
        seq = "".join(result)
    return len(seq)

with open(sys.argv[1]) as f:
    puzzle = f.read().strip()

# Part 1
part1 = look_and_say(puzzle, steps=40)
print(f"Part 1: {part1}")

# Part 2
part2 = look_and_say(puzzle, steps=50)
print(f"Part 2: {part2}")