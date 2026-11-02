import sys
import re
from itertools import combinations
from math import gcd

class Moon:
    def __init__(self, pos: list[int]) -> None:
        self.pos = pos.copy()
        self.vel = [0] * len(pos)
    
    def gravity(self, other: "Moon") -> None:
        for i in range(len(self.pos)):
            self.vel[i] += 1 if self.pos[i] < other.pos[i] else -1 if self.pos[i] > other.pos[i] else 0
    
    def update_pos(self) -> None:
        for i in range(len(self.pos)):
            self.pos[i] += self.vel[i]

with open(sys.argv[1]) as f:
    start = [list(map(int, re.findall(r"-?\d+", line))) for line in f.read().splitlines()]

moons = [Moon(s) for s in start]
for _ in range(1000):
    for m1, m2 in combinations(moons, 2):
        m1.gravity(m2)
        m2.gravity(m1)
    for m in moons:
        m.update_pos()

print(f"Part 1: {sum(sum(map(lambda p: abs(p), m.pos)) * sum(map(lambda v: abs(v), m.vel)) for m in moons)}")

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def find_cycle(moons: list[Moon], ax: int) -> int:
    initial = [(m.pos[ax], m.vel[ax]) for m in moons]
    steps = 0
    while True:
        for m1, m2 in combinations(moons, 2):
            if m1.pos[ax] < m2.pos[ax]:
                m1.vel[ax] += 1
                m2.vel[ax] -= 1
            elif m1.pos[ax] > m2.pos[ax]:
                m1.vel[ax] -= 1
                m2.vel[ax] += 1
        for m in moons:
            m.pos[ax] += m.vel[ax]
        steps += 1
        current = [(m.pos[ax], m.vel[ax]) for m in moons]
        if current == initial:
            return steps

states = [find_cycle([Moon(s) for s in start], i) for i in range(3)]
print(f"Part 2: {lcm(lcm(states[0], states[1]), states[2])}")