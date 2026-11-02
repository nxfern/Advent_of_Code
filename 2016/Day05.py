import sys
from hashlib import md5

with open(sys.argv[1]) as f:
    door_id = f.read().strip()

part1 = ""
part2: list[str | None] = [None] * 8
i = 0
while None in part2 or len(part1) < 8:
    hashed = md5((door_id + str(i)).encode()).hexdigest()
    if hashed.startswith("00000"):
        pos = hashed[5]
        if len(part1) < 8:
            part1 += pos
        if pos.isdigit() and int(pos) < 8 and part2[int(pos)] is None:
            part2[int(pos)] = hashed[6]
    i += 1

print(f"Part 1: {part1}")
print(f"Part 2: {''.join(j for j in part2 if j is not None)}")