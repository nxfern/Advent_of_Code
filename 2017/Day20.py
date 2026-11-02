import re
import sys
from dataclasses import dataclass, astuple
from collections import defaultdict

@dataclass
class Particle:
    a: list[int]
    v: list[int]
    p: list[int]

    @staticmethod
    def parse(line: str) -> "Particle":
        values = list(map(int, re.findall(r"-?\d+", line)))
        assert len(values) == 9, f"Failed to parse line: {line}"
        return Particle(values[6:9], values[3:6], values[0:3])

    def tick(self):
        self.v[0] += self.a[0]; self.v[1] += self.a[1]; self.v[2] += self.a[2]
        self.p[0] += self.v[0]; self.p[1] += self.v[1]; self.p[2] += self.v[2]

    def pos_key(self) -> tuple:
        return (self.p[0], self.p[1], self.p[2])


def manhattan(vec: list[int]) -> int:
    return sum(abs(v) for v in vec)

with open(sys.argv[1]) as f:
    particles = [Particle.parse(line) for line in f.read().splitlines()]

# Part 1
print(f"Part 1: {min(range(len(particles)), key=lambda i: tuple(manhattan(v) for v in astuple(particles[i])))}")

# Part 2
def remove_collisions(particles: list[Particle], steps: int = 50) -> int:
    for _ in range(steps):
        positions = defaultdict(list)
        for p in particles:
            p.tick()
            positions[p.pos_key()].append(p)
        particles = [g[0] for g in positions.values() if len(g) == 1]
    return len(particles)

print(f"Part 2: {remove_collisions(particles)}")