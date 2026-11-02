import sys
import re
from collections import Counter

rooms: list[tuple[str, int, str]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        encryption, sid, checksum = re.findall(r"^([a-z-]+)-(\d+)\[([a-z]+)\]$", line)[0]
        rooms.append((encryption, int(sid), checksum))

part1 = part2 = 0
for (encryption, sid, checksum) in rooms:
    top_5 = "".join(p[0] for p in sorted(Counter(encryption.replace("-", "")).items(), key=lambda t: (-t[1], t[0]))[:5])
    if top_5 == checksum:
        part1 += sid
        shift = sid % 26
        if part2 == 0:
            decrypted = "".join(" " if ch == "-" else chr((ord(ch) - ord('a') + shift) % 26 + ord('a')) for ch in encryption)
            if "northpole" in decrypted:
                part2 = sid

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")