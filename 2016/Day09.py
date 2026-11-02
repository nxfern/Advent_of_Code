import sys
import re

with open(sys.argv[1]) as f:
    seq = f.read()

def decompress(seq, recursive=False):
    total = 0
    i = 0
    while i < len(seq):
        if seq[i] == "(":
            j = seq.index(")", i)
            n, r = map(int, re.findall(r"\d+", seq[i:j]))
            inner = seq[j+1:j+n+1]
            if recursive:
                total += r * decompress(inner, recursive=True)
            else:
                total += n * r
            i = j + n + 1
        else:
            total += 1
            i += 1
    return total

print(f"Part 1: {decompress(seq)}")
print(f"Part 2: {decompress(seq, recursive=True)}")