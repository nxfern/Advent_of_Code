import sys
import re
from hashlib import md5
from collections import defaultdict

def find_repeat(seq: str, n: int) -> str | None:
    m = re.search(rf'(.)\1{{{n-1}}}', seq)
    return m.group(1) if m else None

def check_quintuplet(c: str | None, triplets: dict, keys: int) -> tuple[int, int | None]:
    part = None
    if c:
        for idx in triplets.pop(c, []):
            keys += 1
            if keys == 64:
                part = idx
    return keys, part

def expire_triplets(triplets: dict[str, list[int]], i: int) -> defaultdict[str, list[int]]:
    return defaultdict(list, {c: [idx for idx in idxs if i < idx + 1000]
                for c, idxs in triplets.items() if any(i < idx + 1000 for idx in idxs)})

with open(sys.argv[1]) as f:
    SALT = f.read().strip()

i = p1_keys = p2_keys = 0
part1 = part2 = None
p1_triplets: dict[str, list[int]] = defaultdict(list)
p2_triplets: dict[str, list[int]] = defaultdict(list)
while True:
    hashed = md5((SALT + str(i)).encode()).hexdigest()
    p2_hashed = hashed
    for _ in range(2016):
        p2_hashed = md5(p2_hashed.encode()).hexdigest()

    if p1_keys < 64:
        p1_keys, part1 = check_quintuplet(find_repeat(hashed, 5), p1_triplets, p1_keys)
    if p2_keys < 64:
        p2_keys, part2 = check_quintuplet(find_repeat(p2_hashed, 5), p2_triplets, p2_keys)

    if part1 is not None and part2 is not None:
        break

    if (c := find_repeat(hashed, 3)):
        p1_triplets[c].append(i)
    if (c := find_repeat(p2_hashed, 3)):
        p2_triplets[c].append(i)

    i += 1
    p1_triplets = expire_triplets(p1_triplets, i)
    p2_triplets = expire_triplets(p2_triplets, i)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")