import sys

with open(sys.argv[1]) as f:
    cups = list(map(int, f.read().strip()))

def solve(cups: list[int], N: int, rounds: int) -> list[int]:
    next_cup = [0] * (N + 1)
    for i in range(len(cups) - 1):
        next_cup[cups[i]] = cups[i + 1]

    if N > len(cups):
        next_cup[cups[-1]] = len(cups) + 1
        for i in range(len(cups) + 1, N):
            next_cup[i] = i + 1
        next_cup[N] = cups[0]
    else:
        next_cup[cups[-1]] = cups[0]

    curr = cups[0]
    for _ in range(rounds):
        a = next_cup[curr]
        b = next_cup[a]
        c = next_cup[b]
        next_cup[curr] = next_cup[c]

        dest = curr - 1 if curr > 1 else N
        while dest in (a, b, c):
            dest = dest - 1 if dest > 1 else N

        next_cup[c] = next_cup[dest]
        next_cup[dest] = a

        curr = next_cup[curr]

    return next_cup

next_cup = solve(cups, len(cups), 100)
result = []
cup = next_cup[1]
while cup != 1:
    result.append(str(cup))
    cup = next_cup[cup]
print(f"Part 1: {''.join(result)}")

next_cup = solve(cups, 1_000_000, 10_000_000)
a = next_cup[1]
b = next_cup[a]
print(f"Part 2: {a * b}")