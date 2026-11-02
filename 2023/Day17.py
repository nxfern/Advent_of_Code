import sys
from heapq import heappush, heappop
from itertools import count

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

target = complex(len(lines[0]) - 1, len(lines) - 1)
pool = {complex(c, r): int(l) for r, row in enumerate(lines) for c, l in enumerate(row)}

def crucible(pool: dict[complex, int], m_min: int = 1, m_max: int = 3) -> int:
    counter = count()
    heap: list[tuple[int, int, complex, complex]] = [(0, next(counter), 0, 0)]
    seen: set[tuple[complex, complex]] = set()
    while heap:
        loss, _, pos, d = heappop(heap)
        if pos == target:
            return loss
        if (pos, d) in seen:
            continue
        seen.add((pos, d))
        turns = [1, 1j, -1, -1j] if d == 0 else [d * 1j, d * -1j]
        for nd in turns:
            step_loss = 0
            npos = pos
            for step in range(1, m_max + 1):
                npos = npos + nd
                if npos not in pool:
                    break
                step_loss += pool[npos]
                if step < m_min or (npos, nd) in seen:
                    continue
                heappush(heap, (loss + step_loss, next(counter), npos, nd))
    return -1

print(f"Part 1: {crucible(pool=pool)}")
print(f"Part 2: {crucible(pool=pool, m_min=4, m_max=10)}")