import sys

with open(sys.argv[1]) as f:
    bios = f.read()

WIDTH, HEIGHT = 25, 6
AREA = WIDTH * HEIGHT

layers = [bios[i:i+AREA] for i in range(0, len(bios), AREA)]
min_0 = min(layers, key=lambda l: l.count("0"))
print(f"Part 1: {min_0.count("1") * min_0.count("2")}")

img_map: dict[str, str] = {"0": ".", "1": "#"}
image = [[" "] * WIDTH for _ in range(HEIGHT)]
for r in range(HEIGHT):
    for c in range(WIDTH):
        for layer in layers:
            if layer[(r*WIDTH)+c] in ["0", "1"]:
                image[r][c] = img_map[layer[(r*WIDTH)+c]]
                break
for row in image:
    print("".join(row))