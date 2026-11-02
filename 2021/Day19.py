import sys
from collections import Counter
from itertools import combinations
from typing import Generator

Point = tuple[int, int, int]

scanners: list[list[Point]] = []
with open(sys.argv[1]) as f:
    for block in f.read().split("\n\n"):
        scanners.append([(x, y, z) for line in block.splitlines()[1:] for x, y, z in [map(int, line.split(","))]])
    
ROTATIONS_24 = [
    lambda x, y, z: ( x,  y,  z), lambda x, y, z: ( x, -y, -z),
    lambda x, y, z: ( x,  z, -y), lambda x, y, z: ( x, -z,  y),
    lambda x, y, z: (-x,  y, -z), lambda x, y, z: (-x, -y,  z),
    lambda x, y, z: (-x,  z,  y), lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: ( y,  x, -z), lambda x, y, z: ( y, -x,  z),
    lambda x, y, z: ( y,  z,  x), lambda x, y, z: ( y, -z, -x),
    lambda x, y, z: (-y,  x,  z), lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y,  z, -x), lambda x, y, z: (-y, -z,  x),
    lambda x, y, z: ( z,  x,  y), lambda x, y, z: ( z, -x, -y),
    lambda x, y, z: ( z,  y, -x), lambda x, y, z: ( z, -y,  x),
    lambda x, y, z: (-z,  x, -y), lambda x, y, z: (-z, -x,  y),
    lambda x, y, z: (-z,  y,  x), lambda x, y, z: (-z, -y, -x),
]

def sq_dist(a: Point, b: Point) -> int:
    return sum((x - y) ** 2 for x, y in zip(a, b))

def build_fingerprint(beacons: list[Point]) -> set[int]:
    return {sq_dist(a, b) for a, b in combinations(beacons, 2)}

def all_orientations(pts: list[Point]) -> Generator[list[Point], None, None]:
    for rot in ROTATIONS_24:
        yield [rot(*p) for p in pts]

def try_align(known: set[Point], candidate: list[Point]) -> tuple[list[Point] | None, Point | None]:
    known_list = list(known)
    known_dists: dict[Point, set[int]] = {p: {sq_dist(p, q) for q in known_list} for p in known_list}
    cand_dists: dict[Point, set[int]] = {p: {sq_dist(p, q) for q in candidate} for p in candidate}
    anchor_k, anchor_c = None, None
    for kp, kd in known_dists.items():
        for cp, cd in cand_dists.items():
            if len(kd & cd) >= 11:  # 11 other shared beacons → 12 total overlap
                anchor_k, anchor_c = kp, cp
                break
        if anchor_k:
            break

    if anchor_k is None or anchor_c is None:
        return None, None

    for oriented in all_orientations(candidate):
        idx = candidate.index(anchor_c)
        rot_anchor = oriented[idx]

        offset = (
            anchor_k[0] - rot_anchor[0],
            anchor_k[1] - rot_anchor[1],
            anchor_k[2] - rot_anchor[2],
        )
        translated = frozenset((x + offset[0], y + offset[1], z + offset[2]) for x, y, z in oriented)
        if len(translated & known) >= 12:
            return list(translated), offset

    return None, None

def manhattan(p1: Point, p2: Point) -> int:
    return sum(abs(a - b) for a, b in zip(p1, p2))

fingerprints = [build_fingerprint(s) for s in scanners]
resolved: list[list[Point]] = [scanners[0]]
resolved_fp: list[set[int]] = [fingerprints[0]]
known = set(scanners[0])
scanner_locations: list[Point] = [(0, 0, 0)]

pending = list(range(1, len(scanners)))
while pending:
    found = False
    for i in pending:
        candidate_fp = fingerprints[i]
        if not any(len(candidate_fp & rfp) >= 66 for rfp in resolved_fp):
            continue

        translated, offset = try_align(known, scanners[i])
        if translated and offset:
            known.update(translated)
            scanner_locations.append(offset)
            resolved_fp.append(build_fingerprint(translated))
            pending.remove(i)
            found = True
            break

    if not found:
        raise RuntimeError("No overlapping scanner found in this pass")

print(f"Part 1: {len(known)}")
print(f"Part 2: {max(manhattan(p1, p2) for p1, p2 in combinations(scanner_locations, 2))}")