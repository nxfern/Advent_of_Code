import sys

def fft(seq: list[int], p2: bool = False) -> str:
    base = [0, 1, 0, -1]
    half = len(seq) // 2 if not p2 else 0
    for _ in range(100):
        new = seq[:]
        for i in range(len(seq)-2, half - 1, -1):
            new[i] = (new[i] + new[i + 1]) % 10
        
        if p2:
            seq = new
            continue
        
        for i in range(half - 1, -1, -1):
            total = 0
            for j in range(i, len(seq)):
                pattern_val = base[((j + 1) // (i + 1)) % 4]
                total += seq[j] * pattern_val
            new[i] = abs(total) % 10
        seq = new
    return "".join(map(str, seq[:8]))

with open(sys.argv[1]) as f:
    seq = list(map(int, f.read().strip()))

print(f"Part 1: {fft(seq)}")

offset = int("".join(map(str, seq[:7])))
print(f"Part 2: {fft((seq * 10_000)[offset:], p2=True)}")