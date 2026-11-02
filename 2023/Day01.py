import sys

WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def word_at(line: str, i: int) -> str | None:
    for idx, w in enumerate(WORDS, start=1):
        if line.startswith(w, i):
            return str(idx)
    return None

part1 = part2 = 0
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

for line in lines:
    d_first = d_last = ""
    w_first = w_last = ""
    l, r = 0, len(line) - 1

    while not (d_first and d_last and w_first and w_last):
        if l < len(line):
            if not d_first and line[l].isdigit():
                d_first = line[l]
            if not w_first:
                if line[l].isdigit():
                    w_first = line[l]
                elif (w := word_at(line, l)):
                    w_first = w

        if r >= 0:
            if not d_last and line[r].isdigit():
                d_last = line[r]
            if not w_last:
                if line[r].isdigit():
                    w_last = line[r]
                elif (w := word_at(line, r)):
                    w_last = w

        l += 1
        r -= 1
        
        if l >= len(line) and r < 0:
            break

    part1 += int(d_first + d_last)
    part2 += int(w_first + w_last)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")