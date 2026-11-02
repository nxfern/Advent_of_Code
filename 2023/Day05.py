import sys

class Map:
    def __init__(self, block: str) -> None:
        self.starts = []
        self.ends = []
        self.offsets = []
        for line in block.splitlines()[1:]:
            dest, source, length = map(int, line.split())
            self.starts.append(source)
            self.ends.append(source + length)
            self.offsets.append(source - dest)
    
    def translate_seed(self, seed: int) -> int:
        for start, end, offset in zip(self.starts, self.ends, self.offsets):
            if start <= seed < end:
                return seed - offset
        return seed
    
    def translate_seed_range(self, seeds: list[tuple[int, int]]) -> list[tuple[int, int]]:
        seed_ranges = seeds.copy()
        adj_ranges = []
        while seed_ranges:
            rng_start, rng_end = seed_ranges.pop()
            # Check if current range overlaps with any mapping rule
            for start, end, offset in zip(self.starts, self.ends, self.offsets):
                # Find intersection of [rng_start, rng_end) and [start, end)
                if (adj_start := max(start, rng_start)) < (adj_end := min(end, rng_end)):
                    # Map the intersecting portion
                    adj_ranges.append((adj_start - offset, adj_end - offset))
                    # Split remaining portions that didn't overlap and examine them again
                    if rng_start < adj_start:
                        seed_ranges.append((rng_start, adj_start))
                    if adj_end < rng_end:
                        seed_ranges.append((adj_end, rng_end))
                    break
            else:
                # No mapping found, range passes through unchanged
                adj_ranges.append((rng_start, rng_end))
        return adj_ranges


class Almanac:
    def __init__(self, data: str) -> None:
        blocks = data.split("\n\n")
        self.seeds = list(map(int, blocks[0].split(": ")[1].split()))
        self.seed_ranges = [(seed, seed + length) for seed, length in zip(*[iter(self.seeds)]*2)]
        self.maps = [Map(block) for block in blocks[1:]]
    
    def apply_map(self, seed: int) -> int:
        for map in self.maps:
            seed = map.translate_seed(seed)
        return seed
    
    def lowest_location(self) -> int:
        locations = []
        for seed in self.seeds:
            locations.append(self.apply_map(seed))
        return min(locations)
    
    def lowest_range_location(self) -> int:
        rngs = self.seed_ranges.copy()
        for map in self.maps:
            rngs = map.translate_seed_range(rngs)
        return min(start for start, _ in rngs)


with open("../../Data/2023/Day05") as f:
    puzzle = f.read()

ALMANAC = Almanac(puzzle)
print(f"Part 1: {ALMANAC.lowest_location()}")
print(f"Part 2: {ALMANAC.lowest_range_location()}")