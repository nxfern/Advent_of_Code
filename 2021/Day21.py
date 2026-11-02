import sys
from itertools import cycle
from functools import cache

with open(sys.argv[1]) as f:
    start = [int(line.split()[-1]) for line in f.read().splitlines()]

score = [0, 0]
pos = start.copy()
turn = cycle([0, 1])
die = cycle(range(1, 101))
rolls = 0
while all(p < 1000 for p in score):
    t = next(turn)
    toss = sum(next(die) for _ in range(3))
    rolls += 3
    pos[t] = (pos[t] + toss) % 10
    score[t] += 10 if pos[t] == 0 else pos[t]

print(f"Part 1: {score[next(turn)] * rolls}")

outcomes = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)] # toss sums and frequencies

@cache
def dirac(score: tuple[int, int], pos: tuple[int, int], t: bool) -> tuple[int, int]:
    if any(s >= 21 for s in score):
        return score[0] >= 21, score[1] >= 21

    p1 = p2 = 0
    for toss, freq in outcomes:
        npos, nscore = list(pos), list(score)
        npos[t] = (npos[t] + toss) % 10
        nscore[t] += 10 if npos[t] == 0 else npos[t]
        w1, w2 = dirac(tuple(nscore), tuple(npos), not t)
        p1 += w1 * freq
        p2 += w2 * freq

    return p1, p2

print(f"Part 2: {max(dirac((0, 0), tuple(start), False))}")