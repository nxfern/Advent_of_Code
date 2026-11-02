import sys

class Group:
    def __init__(self, units: int, hp: int, imm: list[str], weak: list[str], dmg: int, dtype: str, speed: int) -> None:
        self.units = units
        self.hp_per = hp
        self.dmg = dmg
        self.dtype = dtype
        self.spd = speed
        self.imm = imm
        self.weak = weak

    def get_power(self) -> int:
        return self.dmg * self.units
    
    def attack(self) -> tuple[int, str]:
        return self.get_power(), self.dtype
    
    def damage_calc(self, damage: int, atype: str) -> int:
        if atype in self.imm:
            return 0
        mod = 2 if atype in self.weak else 1
        return damage * mod

    def defend(self, damage: int, atype: str) -> None:
        calc = self.damage_calc(damage, atype)
        if calc == 0:
            return
        killed = min(self.units, calc // self.hp_per)  # floor div, clamped
        self.units -= killed

def parse_input(lines: list[str]) -> list[Group]:
    group: list[Group] = []
    for line in lines:
        units, hp, dmg, speed = [int(n) for n in line.split() if n.isdigit()]
        imm, weak = [], []
        if '(' in line and ')' in line:
            start = line.index('(') + 1
            end = line.index(')')
            traits = line[start:end]
            for part in traits.split(';'):
                part = part.strip()
                if part.startswith("immune to"):
                    imm = [x.strip() for x in part[len("immune to "):].split(',')]
                elif part.startswith("weak to"):
                    weak = [x.strip() for x in part[len("weak to "):].split(',')]
        words = line.split()
        dtype = "None"
        for i, word in enumerate(words):
            if word == "damage" and i >= 2 and words[i-2].isdigit():
                dtype = words[i-1]
        group.append(Group(units, hp, imm, weak, dmg, dtype, speed))
    return group

def targeting_phase(all_groups: list[Group], immune_set: set, infect_set: set) -> dict[Group, Group]:
    targets = {}
    claimed = set()
    for a in sorted(all_groups, key=lambda g: (g.get_power(), g.spd), reverse=True):
        defenders: set[Group] = immune_set if a in infect_set else infect_set
        available: list[Group] = [d for d in defenders if d not in claimed and a.dtype not in d.imm]
        if not available:
            continue
        target = max(available, key=lambda d: (d.damage_calc(*a.attack()), d.get_power(), d.spd))
        targets[a] = target
        claimed.add(target)
    return targets

with open(sys.argv[1]) as f:
    groups = f.read().split("\n\n")
    immune_system = parse_input(groups[0].splitlines()[1:])
    infections = parse_input(groups[1].splitlines()[1:])

immune_system.sort(key=lambda g: (g.get_power(), g.spd), reverse=True)
infections.sort(key=lambda g: (g.get_power(), g.spd), reverse=True)

def battle(good: list[Group], bad: list[Group], boost=0) -> tuple[int, int]:
    immunes = [Group(g.units, g.hp_per, g.imm, g.weak, g.dmg + boost, g.dtype, g.spd) for g in good]
    infects = [Group(g.units, g.hp_per, g.imm, g.weak, g.dmg, g.dtype, g.spd) for g in bad]
    while immunes and infects:
        immune_set = set(immunes)
        infect_set = set(infects)
        targets = targeting_phase(immunes + infects, immune_set, infect_set)
        before = sum(g.units for g in immunes) + sum(g.units for g in infects)
        for a, d in sorted(targets.items(), key=lambda g: g[0].spd, reverse=True):
            if a.units <= 0 or d.units <= 0:
                continue
            d.defend(*a.attack())
        immunes = sorted([g for g in immunes if g.units > 0], key=lambda g: (g.get_power(), g.spd), reverse=True)
        infects = sorted([g for g in infects if g.units > 0], key=lambda g: (g.get_power(), g.spd), reverse=True)
        if sum(g.units for g in immunes) + sum(g.units for g in infects) == before:
            return 0, 0  # stalemate
    return sum(g.units for g in immunes), sum(g.units for g in infects)

# Part 1
part1 = sum(battle(immune_system, infections))
print(f"Part 1: {part1}")

# Part 2
lo, hi = 0, 1
while battle(immune_system, infections, boost=hi)[0] == 0:
    hi *= 2

while lo < hi:
    mid = (lo + hi) // 2
    imm_units, inf_units = battle(immune_system, infections, boost=mid)
    if imm_units > 0 and inf_units == 0:
        hi = mid
    else:
        lo = mid + 1

part2 = battle(immune_system, infections, boost=lo)[0]
print(f"Part 2: {part2}")