import sys
from ast import literal_eval
from json import dumps

code = memory = encoded = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        code += len(line)
        memory += len(literal_eval(line))
        encoded += len(dumps(line))

# Part 1
part1 = code - memory
print(f"Part 1: {part1}")

# Part 2
part2 = encoded - code
print(f"Part 2: {part2}")