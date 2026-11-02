import sys
from math import ceil
from functools import reduce
from itertools import permutations

def explode(pairs: list[list[int]]) -> bool:
    for i in range(len(pairs) - 1):
        vl, dl = pairs[i]
        vr, dr = pairs[i + 1]
        if dl == dr and dl >= 5:
            if i > 0:
                pairs[i - 1][0] += vl
            if i + 2 < len(pairs):
                pairs[i + 2][0] += vr
            pairs[i:i + 2] = [[0, dl - 1]]
            return True
    return False

def split(pairs: list[list[int]]) -> bool:
    for i, (v, d) in enumerate(pairs):
        if v >= 10:
            pairs[i:i + 1] = [[v // 2, d + 1], [ceil(v / 2), d + 1]]
            return True
    return False

def reduce_flat(pairs: list[list[int]]) -> list[list[int]]:
    while explode(pairs) or split(pairs):
        pass
    return pairs

def add_flat(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    result = [[v, d + 1] for v, d in a] + [[v, d + 1] for v, d in b]
    return reduce_flat(result)

def magnitude_flat(pairs: list[list[int]]) -> int:
    p = [list(x) for x in pairs]
    while len(p) > 1:
        for i in range(len(p) - 1):
            if p[i][1] == p[i + 1][1]:
                p[i:i + 2] = [[3 * p[i][0] + 2 * p[i + 1][0], p[i][1] - 1]]
                break
    return p[0][0]

snailfish: list[list[list[int]]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        out, depth, i = [], 0, 0
        while i < len(line):
            c = line[i]
            if   c == '[': depth += 1; i += 1
            elif c == ']': depth -= 1; i += 1
            elif c == ',': i += 1
            else:
                j = i
                while j < len(line) and line[j].isdigit(): j += 1
                out.append([int(line[i:j]), depth])
                i = j
        snailfish.append(out)

total = reduce(lambda a, b: add_flat([list(x) for x in a], [list(x) for x in b]), snailfish)
part1 = magnitude_flat(total)
part2 = max(magnitude_flat(add_flat([list(x) for x in snailfish[i]], [list(x) for x in snailfish[j]]))
            for i, j in permutations(range(len(snailfish)), 2))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")