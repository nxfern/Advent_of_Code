import sys

with open(sys.argv[1]) as f:
    navi = f.read().splitlines()

VALID: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
SCORE: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
ADDED: dict[str, int] = {"(": 1, "[": 2, "{": 3, "<": 4}

part1 = 0
results: list[int] = []
for line in navi:
    stack: list[str] = []
    for ch in line:
        if ch in VALID.keys():
            stack.append(ch)
        if stack and ch in VALID.values():
            if VALID[stack[-1]] != ch:
                part1 += SCORE[ch]
                break
            stack.pop()
    else:
        result = 0
        while stack:
            result = result * 5 + ADDED[stack.pop()]
        results.append(result)
results, l = sorted(results), len(results)
part2 = results[l//2] if l % 2 == 1 else (results[l//2] + results[l//2 + 1]) // 2

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")