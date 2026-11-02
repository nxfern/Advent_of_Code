import sys

with open(sys.argv[1]) as f:
    text = f.read()
    lines = [l for l in text.strip().splitlines()]
    blocks = [lines[i:i + 18] for i in range(0, len(lines), 18)]
    params = []
    for block in blocks:
        a = int(block[4].split()[-1])   # 'div z a'
        b = int(block[5].split()[-1])   # 'add x b'
        c = int(block[15].split()[-1])  # 'add y c'
        params.append((a, b, c))

n = len(params)
max_digits = [0] * n
min_digits = [0] * n
stack = []  # holds (index, c) for push blocks
for i, (a, b, c) in enumerate(params):
    if a == 1:  # push block
        stack.append((i, c))
    else:   # pop block: match with the most recent unmatched push
        j, C_push = stack.pop()
        diff = C_push + b  # w_i(pop) relationship: w_i - w_j(push) = diff

        if diff >= 0:
            max_digits[j], max_digits[i] = 9 - diff, 9
            min_digits[j], min_digits[i] = 1, 1 + diff
        else:
            max_digits[j], max_digits[i] = 9, 9 + diff
            min_digits[j], min_digits[i] = 1 - diff, 1

print(f"Part 1: {''.join(map(str, max_digits))}")
print(f"Part 2: {''.join(map(str, min_digits))}")