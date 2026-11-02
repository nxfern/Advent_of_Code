import sys

with open(sys.argv[1]) as f:
    row, col = [int(part) for part in f.read().split(".")[1].replace(",", "").split() if part.isnumeric()]

n = (row + col - 1) * (row + col - 2) // 2 + col
part1 = (20151125 * pow(252533, n-1, 33554393)) % 33554393
print(f"Part 1: {part1}")