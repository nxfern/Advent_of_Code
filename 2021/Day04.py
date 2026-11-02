import sys

with open(sys.argv[1]) as f:
    draws, *blocks = f.read().split("\n\n")
    draws = list(map(int, draws.split(",")))
    cards: list[list[list[int]]] = [[list(map(int, row.split())) for row in block.splitlines()] for block in blocks]

def mark(d: int, card: list[list[int]]) -> None:
    for r, row in enumerate(card):
        for c, n in enumerate(row):
            if d == n:
                card[r][c] = -1
                return

results: list[int] = []
won: set[int] = set()
for d in draws:
    for i, card in enumerate(cards):
        if i in won:
            continue
        mark(d, card)
        if any(sum(line) == -5 for line in (*card, *zip(*card))):
            won.add(i)
            results.append(sum(n for row in card for n in row if n >= 0) * d)

print(f"Part 1: {results[0]}")
print(f"Part 2: {results[-1]}")