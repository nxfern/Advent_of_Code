import sys

with open(sys.argv[1]) as f:
    SEQ = list(enumerate(map(int, f.read().splitlines())))
    L = len(SEQ) - 1

def mix(rounds: int, key: int | None = None) -> int:
    mix = [(i, n*key) for i, n in SEQ] if key else SEQ.copy()
    z = (0, 0)
    for _ in range(rounds):
        for i, n in SEQ:
            t = (i, n*key) if key else (i, n)
            if n == 0:
                z = t
            j = mix.index(t)
            mix.insert((j+t[1])%L, mix.pop(j))

    z = mix.index(z)
    return sum(mix[(z+o)%(L+1)][1] for o in [1000, 2000, 3000])

print(f"Part 1: {mix(1)}")
print(f"Part 2: {mix(10, 811589153)}")