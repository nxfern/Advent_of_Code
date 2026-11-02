import sys

with open(sys.argv[1]) as f:
    diagnostic = f.read().splitlines()

gamma = epsilon = ""
oxygen, c02 = diagnostic[:], diagnostic[:]
for i in range(len(diagnostic[0])):
    bits = [d[i] for d in diagnostic]
    ones, zeros = bits.count("1"), bits.count("0")
    gamma += "1" if ones > zeros else "0"
    epsilon += "0" if ones > zeros else "1"
    
    if len(oxygen) > 1:
        o_ones = sum(o[i] == "1" for o in oxygen)
        oxygen = [o for o in oxygen if o[i] == ("1" if o_ones >= len(oxygen) - o_ones else "0")]

    if len(c02) > 1:
        c_ones = sum(c[i] == "1" for c in c02)
        c02 = [c for c in c02 if c[i] == ("0" if c_ones >= len(c02) - c_ones else "1")]

print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")
print(f"Part 2: {int("".join(oxygen), 2) * int("".join(c02), 2)}")