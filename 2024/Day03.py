import sys, re

memory: dict[str, int] = {"do": 0, "don't": 0}
key = "do"  # default key
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        for m in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", line):
            if m.group() == "do()":
                key = "do"
            elif m.group() == "don't()":
                key = "don't"
            elif m.group().startswith("mul"):
                a, b = map(int, re.findall(r"\d+", m.group()))
                memory[key] += a * b

print(f"Part 1: {sum(memory.values())}")
print(f"Part 2: {memory["do"]}")