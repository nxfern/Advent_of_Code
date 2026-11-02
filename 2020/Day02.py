import sys

passwords: list[tuple[int, int, str, str]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = line.split()
        lo, hi = map(int, parts[0].split("-"))
        passwords.append((lo, hi, parts[1][0], parts[2]))

print(f"Part 1: {sum(lo <= p.count(l) <= hi for lo, hi, l, p in passwords)}")
print(f"Part 2: {sum((p[lo-1] == l) ^ (p[hi-1] == l) for lo, hi, l, p in passwords)}")