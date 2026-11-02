import sys
import numpy as np
from math import prod

a = np.loadtxt(sys.argv[1], delimiter=",", dtype=np.int64)
n = len(a)

iu, ju = np.triu_indices(n, 1)
diff = a[iu] - a[ju]
d = np.einsum("ij,ij->i", diff, diff)

order = np.argsort(d, kind="stable")
I, J = iu[order].tolist(), ju[order].tolist()

parent = list(range(n))
size = [1] * n
comps = n
part1 = part2 = 0

for e, (i, j) in enumerate(zip(I, J), 1):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    while parent[j] != j:
        parent[j] = parent[parent[j]]
        j = parent[j]

    if i != j:
        if size[i] < size[j]:
            i, j = j, i
        parent[j] = i
        size[i] += size[j]
        comps -= 1
        if comps == 1:
            part2 = int(a[I[e - 1], 0]) * int(a[J[e - 1], 0])

    if e == 1000:
        part1 = prod(sorted((size[r] for r in range(n) if parent[r] == r), reverse=True)[:3])
    if e >= 1000 and comps == 1:
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")