import sys
from itertools import product, combinations

boss: dict[str, int] = {}
with open(sys.argv[1]) as f:
    stats: list[int] = [int(line.split()[-1]) for line in f.read().splitlines()]
    boss["hp"] = stats[0]
    boss["attack"] = stats[1]
    boss["defense"] = stats[2]

weapons: list[tuple[int, int, int]] = [
    (8, 4, 0),      # Dagger
    (10, 5, 0),     # Shortsword
    (25, 6, 0),     # Warhammer
    (40, 7, 0),     # Longsword
    (74, 8, 0)      # Greataxe
]
gear: list[tuple[int, int, int]] = [
    (0, 0, 0),      # Nothing
    (13, 0, 1),     # Leather
    (31, 0, 2),     # Chainmail
    (53, 0, 3),     # Splintmail
    (75, 0, 4),     # Bandedmail
    (102, 0, 5),    # Platemail
]
rings: list[tuple[int, int, int]] = [
    (0, 0, 0),      # Nothing
    (0, 0, 0),      # Nothing
    (25, 1, 0),     # Damage +1
    (50, 2, 0),     # Damage +2
    (100, 3, 0),    # Damage +3
    (20, 0, 1),     # Defense +1
    (40, 0, 2),     # Defense +2
    (80, 0, 3),     # Defense +3
]

part1, part2 = 1000, 0
for weapon, armor, (r1, r2) in product(weapons, gear, combinations(rings, 2)):
    player_hp, boss_hp = 100, boss["hp"]
    cost = weapon[0] + armor[0] + r1[0] + r2[0]
    attack = weapon[1] + r1[1] + r2[1]
    defense = armor[2] + r1[2] + r2[2]
    while player_hp > 0 and boss_hp > 0:
        boss_hp -= max(attack - boss["defense"], 1)
        if boss_hp <= 0:
            part1 = min(cost, part1)
            break
        player_hp -= max(boss["attack"] - defense, 1)
    else:
        part2 = max(cost, part2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")