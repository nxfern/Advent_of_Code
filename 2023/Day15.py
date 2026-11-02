import sys

with open(sys.argv[1]) as f:
    seq = f.read().split(",")

def hashing(h: str, c: int = 0) -> int:
    for ch in h:
        c = ((c + ord(ch)) * 17) & 255
    return c

boxes: list[dict[str, int]] = [{} for _ in range(256)]
for h in seq:
    if h[-1] == "-":
        label = h[:-1]
        box = boxes[hashing(label)]
        box.pop(label, None)
    else:
        label, val = h.split("=", 1)
        box = boxes[hashing(label)]
        box[label] = int(val)

part2 = 0
for i, box in enumerate(boxes, start=1):
    for slot, focus in enumerate(box.values(), start=1):
        part2 += i * slot * focus

print(f"Part 1: {sum(hashing(h) for h in seq)}")
print(f"Part 2: {part2}")