import sys, re, math, statistics as st

with open(sys.argv[1]) as f:
    robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in f.read().splitlines()]

W, H, T = 101, 103, 100
quads = [0, 0, 0, 0]
for px, py, vx, vy in robots:
    x = (px + T * vx) % W
    y = (py + T * vy) % H
    if x == W//2 or y == H//2:
        continue
    quads[(x > W//2) + 2 * (y > H//2)] += 1

tx = min(range(W), key=lambda t: st.pvariance([(px + t * vx) % W for px, py, vx, vy in robots]))
ty = min(range(H), key=lambda t: st.pvariance([(py + t * vy) % H for px, py, vx, vy in robots]))
t = tx + W * (((ty - tx) * pow(W, -1, H)) % H)

print(f"Part 1: {math.prod(quads)}")
print(f"Part 2: {t}")