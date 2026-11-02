import sys

with open(sys.argv[1]) as f:
    ips = sorted((int(lo), int(hi)) for line in f.read().splitlines() for lo, hi in [line.split("-")])

MIN_IP, MAX_IP = 0, 4_294_967_295

blacklist: list[tuple[int, int]] = []
whitelist: list[tuple[int, int]] = []

if ips[0][0] > MIN_IP:
    whitelist.append((MIN_IP, ips[0][0]-1))

for lo, hi in ips:
    if blacklist and lo <= blacklist[-1][1] + 1:
        blacklist[-1] = blacklist[-1][0], max(blacklist[-1][1], hi)
    else:
        if blacklist:
            whitelist.append((blacklist[-1][1]+1, lo-1))
        blacklist.append((lo, hi))

if blacklist[-1][1] < MAX_IP:
    whitelist.append((blacklist[-1][1]+1, MAX_IP))

print(f"Part 1: {whitelist[0][0]}")
print(f"Part 2: {sum(hi+1 - lo for lo, hi in whitelist)}")