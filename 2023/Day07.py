import sys
from collections import Counter

def hand_key(hand: str, joker: bool) -> tuple[list[int], tuple[int, ...]]:
    order = "23456789TJQKA" if not joker else "J23456789TQKA"
    card_ranks = tuple(order.index(c) for c in hand)
    counts = Counter(hand)
    if joker and "J" in counts and len(counts) > 1:
        j = counts.pop("J")
        best = max(counts, key=lambda c: counts[c])
        counts[best] += j

    type_rank = sorted(counts.values(), reverse=True)
    return (type_rank, card_ranks)

def total_winnings(lines: list[str], joker: bool = False) -> int:
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((hand_key(hand, joker), int(bid)))

    hands.sort(key=lambda x: x[0])  # weakest -> strongest
    return sum(rank * bid for rank, (_, bid) in enumerate(hands, start=1))

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

print("Part 1:", total_winnings(lines, joker=False))
print("Part 2:", total_winnings(lines, joker=True))