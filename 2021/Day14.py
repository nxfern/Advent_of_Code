import sys
from collections import Counter

with open(sys.argv[1]) as f:
    polymer, rules = f.read().split("\n\n")
    rules = {k: v for line in rules.splitlines() for k, v in [line.split(" -> ")]}

def char_count(pairs: Counter[str]) -> int:
    char_counts: Counter = Counter()
    for pair, count in pair_counts.items():
        char_counts[pair[0]] += count
    char_counts[polymer[-1]] += 1  # last character is never a pair's first
    return char_counts.most_common()[0][1] - char_counts.most_common()[-1][1]

pair_counts = Counter(polymer[i:i+2] for i in range(len(polymer) - 1))
part1 = 0
for i in range(40):
    if i == 10:
        part1 = char_count(pair_counts)

    new_counts: Counter = Counter()
    for pair, count in pair_counts.items():
        insert = rules[pair]
        new_counts[pair[0] + insert] += count
        new_counts[insert + pair[1]] += count
    pair_counts = new_counts

print(f"Part 1: {part1}")
print(f"Part 2: {char_count(pair_counts)}")