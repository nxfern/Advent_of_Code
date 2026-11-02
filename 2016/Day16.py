import sys

def dragon(a: str) -> str:
    b = a[::-1].translate(str.maketrans("10", "01"))
    return a + "0" + b

def compress(seq: str) -> str:
    return "".join("1" if a == b else "0" for a, b in zip(seq[::2], seq[1::2]))

def get_checksum(seq: str, n: int) -> str:
    while len(seq) < n:
        seq = dragon(seq)
    seq = seq[:n]
    while len(seq) % 2 == 0:
        seq = compress(seq)
    return seq

with open(sys.argv[1]) as f:
    start = f.read()

print(f"Part 1: {get_checksum(start, 272)}")
print(f"Part 2: {get_checksum(start, 35651584)}")