import sys
from hashlib import md5

with open(sys.argv[1]) as f:
    secret = f.read()

part1 = part2 = None
i = 1
while True:
    hashed = md5((secret + str(i)).encode()).hexdigest()
    if not part1 and all(ch == "0" for ch in hashed[:5]):
        part1 = i
    if part1 and all(ch == "0" for ch in hashed[:6]):
        part2 = i
        break
    i += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")