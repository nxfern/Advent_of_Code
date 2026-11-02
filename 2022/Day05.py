import sys
import re

with open(sys.argv[1]) as f:
    blocks = f.read().split("\n\n")
    
    cols: dict[int, list[str]] = {}
    for line in blocks[0].split('\n')[:-1]:
        for m in re.finditer(r'\[(.)\]', line):
            col = m.start() // 4    # each column is 4 chars wide: "[X] "
            cols.setdefault(col, []).append(m.group(1))
    p1_stacks = [list(reversed(cols[c])) for c in sorted(cols)]
    p2_stacks = [s[:] for s in p1_stacks]

    moves: list[tuple[int, int, int]] = []
    for line in blocks[1].splitlines():
        n, i, j = map(int, re.findall(r"\d+", line))
        moves.append((n, i-1, j-1)) # match 0 indexing

for n, i, j in moves:
    p1_stacks[j].extend(p1_stacks[i][-n:][::-1])
    p1_stacks[i] = p1_stacks[i][:len(p1_stacks[i])-n]
    p2_stacks[j].extend(p2_stacks[i][-n:])
    p2_stacks[i] = p2_stacks[i][:len(p2_stacks[i])-n]

print(f"Part 1: {"".join(s[-1] for s in p1_stacks)}")
print(f"Part 2: {"".join(s[-1] for s in p2_stacks)}")