import sys

with open(sys.argv[1]) as f:
    ages = list(map(int, f.read().split(",")))

fish: list[int] = [0] * 9
for a in ages:
    fish[a] += 1

part1 = 0
for day in range(256):
    if day == 80:
        part1 = sum(fish)
    new = fish[0]
    for i in range(len(fish)-1):
        fish[i] = fish[i+1]
    fish[6] += new
    fish[8] = new

print(f"Part 1: {part1}")
print(f"Part 2: {sum(fish)}")