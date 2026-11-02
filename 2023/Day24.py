import sys
from itertools import combinations
from sympy import symbols, Eq, Matrix, solve

class Hailstone:
    def __init__(self, p: list[int], v: list[int]) -> None:
        self.p = p
        self.v = v

    def crosses(self, other: "Hailstone", lo: int, hi: int) -> bool:
        det = other.v[0] * self.v[1] - self.v[0] * other.v[1]
        if det == 0:
            return False

        t1 = ((other.p[0] - self.p[0]) * -other.v[1] + (other.p[1] - self.p[1]) * other.v[0]) / det
        t2 = ((other.p[1] - self.p[1]) * self.v[0] - (other.p[0] - self.p[0]) * self.v[1]) / det
        if t1 < 0 or t2 < 0:
            return False

        x = self.p[0] + self.v[0] * t1
        y = self.p[1] + self.v[1] * t1
        return lo <= x <= hi and lo <= y <= hi

class Weather:
    def __init__(self, data: str) -> None:
        self.hailstones: list[Hailstone] = []
        for line in data.splitlines():
            p, v = [list(map(int, part.split(", "))) for part in line.split(" @ ")]
            self.hailstones.append(Hailstone(p, v))

    def intersections(self, lo: int, hi: int) -> int:
        return sum(h1.crosses(h2, lo, hi) for h1, h2 in combinations(self.hailstones, 2))

    def magic_rock(self) -> int:
        rx, ry, rz, vx, vy, vz = symbols("rx ry rz vx vy vz")
        R = Matrix([rx, ry, rz])
        V = Matrix([vx, vy, vz])
        h0, *rest = self.hailstones[:3]
        p0, v0 = Matrix(h0.p), Matrix(h0.v)

        eqs = []
        for h in rest:
            p1, v1 = Matrix(h.p), Matrix(h.v)
            lhs = R.cross(v0 - v1) + (p0 - p1).cross(V)
            rhs = p0.cross(v0) - p1.cross(v1)
            eqs.extend(Eq(l, r) for l, r in zip(lhs, rhs))

        sol = solve(eqs, [rx, ry, rz, vx, vy, vz])
        return sol[rx] + sol[ry] + sol[rz]

with open(sys.argv[1]) as f:
    weather = Weather(f.read())

print(f"Part 1: {weather.intersections(200_000_000_000_000, 400_000_000_000_000)}")
print(f"Part 2: {weather.magic_rock()}")