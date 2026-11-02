import sys

with open(sys.argv[1]) as f:
    earliest, timestamps = f.read().splitlines()
    earliest = int(earliest)
    timestamps = timestamps.split(",")

wait, bus = min((int(b) - (earliest % int(b)), int(b)) for b in timestamps if b.isdigit())
print(f"Part 1: {bus * wait}")

busses = [(i, int(b)) for i, b in enumerate(timestamps) if b.isdigit()]
t, step = 0, 1  # Chinese Remainder Theorem
for i, b in busses:
    while (t + i) % b != 0:
        t += step
    step *= b

print(f"Part 2: {t}")