import sys
import re
from collections.abc import Callable

passports: list[dict[str, str]] = []
with open(sys.argv[1]) as f:
    for block in f.read().split("\n\n"):
        fields: dict[str, str] = {}
        for line in block.splitlines():
            for part in line.split():
                k, v = part.split(":")
                fields[k] = v
        passports.append(fields)

REQUIRED: set[str] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
RULESETS: dict[str, Callable[[dict[str, str], str], bool]] = {
    "byr": lambda p, f: 1920 <= int(p[f]) <= 2002,
    "iyr": lambda p, f: 2010 <= int(p[f]) <= 2020,
    "eyr": lambda p, f: 2020 <= int(p[f]) <= 2030,
    "hgt": lambda p, f: (150 <= int(p[f][:-2]) <= 193) if p[f].endswith("cm") else (59 <= int(p[f][:-2]) <= 76),
    "hcl": lambda p, f: bool(re.fullmatch(r"#[0-9a-f]{6}", p[f])),
    "ecl": lambda p, f: p[f] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda p, f: bool(re.fullmatch(r"\d{9}", p[f])),
}

part1 = part2 = 0
for p in passports:
    if REQUIRED.issubset(p.keys()):
        part1 += 1
        if not p["hgt"].endswith(("cm", "in")):
            continue
        part2 += all(RULESETS[f](p, f) for f in REQUIRED)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")