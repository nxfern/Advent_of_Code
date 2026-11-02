import sys

lines: list[tuple[str, int]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        parts = line.split()
        if "cut" in line:
            lines.append((parts[0], int(parts[1])))
        elif "stack" in line:
            lines.append((parts[-1], 0))
        else:
            lines.append((parts[2], int(parts[-1])))

def compose(f: tuple[int, int], g: tuple[int, int], N: int) -> tuple[int, int]:
    """Compose two linear functions f(g(x)) where each is (a, b)."""
    fa, fb = f
    ga, gb = g
    return (fa * ga % N, (fa * gb + fb) % N)

def power(f: tuple[int, int], k: int, N: int) -> tuple[int, int]:
    """Apply linear function f, k times using repeated squaring."""
    result = (1, 0)  # identity
    while k:
        if k % 2 == 1:
            result = compose(result, f, N)
        f = compose(f, f, N)
        k //= 2
    return result

def shuffle(lines: list[tuple[str, int]], size: int, pos: int, repeat: int = 0) -> int:
    a, b = 1, 0
    for inst, n in lines:
        if inst == "stack":
            a, b = -a, -b - 1
        elif inst == "cut":
            a, b = a, b - n
        else:
            a, b = a * n, b * n
    if repeat == 0:
        a, b = a % size, b % size
        return (a * pos + b) % size
    a, b = power((a, b), repeat, size)
    return (pos - b) * pow(a, -1, size) % size

print(f"Part 1: {shuffle(lines, size=10_007, pos=2019)}")
print(f"Part 2: {shuffle(lines, size=119_315_717_514_047, pos=2020, repeat=101_741_582_076_661)}")