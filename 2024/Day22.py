import sys
import numpy as np

with open(sys.argv[1]) as f:
    n = np.array(f.read().split(), dtype=np.int64)

B = len(n)
MASK = (1 << 24) - 1

S = np.empty((2001, B), dtype=np.int64)
S[0] = n
for t in range(2000):
    n ^= (n << 6) & MASK
    n ^= n >> 5
    n ^= (n << 11) & MASK
    S[t + 1] = n

print(f"Part 1: {S[-1].sum()}")

prices = (S % 10).T
d = np.diff(prices, axis=1) + 9
keys = d[:, :-3] * 6859 + d[:, 1:-2] * 361 + d[:, 2:-1] * 19 + d[:, 3:]
vals = prices[:, 4:]
K = 19 ** 4
flat = keys + np.arange(B)[:, None] * K
uniq, first = np.unique(flat.ravel(), return_index=True)
totals = np.bincount(uniq % K, weights=vals.ravel()[first], minlength=K)
print(f"Part 2: {int(totals.max())}")