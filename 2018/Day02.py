import sys
from collections import Counter

with open(sys.argv[1]) as f:
    boxes = f.read().splitlines()

doubles = triples = 0
length = len(boxes[0])
candidates: set[str] = set()
part2 = None
for box in boxes:
    counts = Counter(box).values()
    doubles += 2 in counts
    triples += 3 in counts

    if part2:
        continue
    for i in range(length):
        candidate = box[:i] + box[i+1:]
        if candidate in candidates:
            part2 = candidate
            break
        candidates.add(candidate)

print(f"Part 1: {doubles * triples}")
print(f"Part 2: {part2}")