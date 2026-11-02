import sys
from collections import deque, defaultdict

def marble_game(n_players: int, l_marble: int) -> int:
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, l_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % n_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    
    return max(scores.values())

with open(sys.argv[1]) as f:
    parts = f.read().split()
    players, last_marble = int(parts[0]), int(parts[6])

print(f"Part 1: {marble_game(players, last_marble)}")
print(f"Part 2: {marble_game(players, last_marble * 100)}")