import sys

with open(sys.argv[1]) as f:
    buffer = f.read()

part1, i = 0, 4
while i < len(buffer) and len(set(buffer[i-14:i])) < 14:
    if part1 == 0 and len(set(buffer[i-4:i])) == 4:
        part1 = i
    i += 1

print(f"Part 1: {part1}")
print(f"Part 2: {i}")