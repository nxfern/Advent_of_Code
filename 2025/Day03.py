import sys

with open(sys.argv[1]) as f:
    joltages = f.read().splitlines()

def power_banks(bank: str, b: int) -> int:
    drop, stack = len(bank) - b, []
    for d in bank:
        while drop and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)
    return int("".join(stack[:b]))

print(f"Part 1: {sum(power_banks(bank, b=2) for bank in joltages)}")
print(f"Part 2: {sum(power_banks(bank, b=12) for bank in joltages)}")