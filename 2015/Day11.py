import sys

with open(sys.argv[1]) as f:
    puzzle = f.read().strip()

def increment(pword: str) -> str:
    s = list(pword)
    i = len(s) - 1
    while i >= 0:
        if s[i] == "z":
            s[i] = "a"
            i -= 1
            continue
        s[i] = chr(ord(s[i]) + 1)
        if s[i] in "iol":
            s[i] = chr(ord(s[i]) + 1)
            s[i+1:] = ["a"] * (len(s) - i - 1)

        return "".join(s)
    return "".join(s)

new = puzzle
pairs = [chr(x)*2 for x in range(97, 123) if chr(x) not in "iol"]
triplets = [chr(x)+chr(x+1)+chr(x+2) for x in range(97, 121) if not any(chr(x+y) in "iol" for y in range(3))]
part1 = part2 = None
while not (part1 and part2):
    if (
        any(t in new for t in triplets) and
        sum(1 for p in pairs if p in new) >= 2
    ):
        if part1 is None:
            part1 = new
        else:
            part2 = new
    new = increment(new)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")