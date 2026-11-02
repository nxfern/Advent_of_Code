import sys

with open(sys.argv[1]) as f:
    elves = int(f.read())

# Part 1
def josephus(n: int) -> int:
    power = 1
    while power * 2 <= n:
        power *= 2
    return (n - power) * 2 + 1

part1 = josephus(elves)
print(f"Part 1: {part1}")

# Part 2
def elf_across_math(n: int) -> int:
    power = 1
    while power * 3 <= n:
        power *= 3
    return n if n == power else n - power + max(n - 2 * power, 0)

part2 = elf_across_math(elves)
print(f"Part 2: {part2}")