import sys

with open(sys.argv[1]) as f:
    puzzle = f.read().splitlines()

DECIMAL = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
SNAFU = {v: k for k, v in DECIMAL.items()}

result = 0
for line in puzzle:
    temp = 0
    for i, ch in enumerate(reversed(line)):
        temp += DECIMAL[ch] * pow(5, i)
    result += temp

snafu = ""
while result:
    result, rem = divmod(result, 5)
    if rem > 2:
        rem -= 5
        result += 1
    snafu += SNAFU[rem]

print(f"Answer: {snafu[::-1]}")