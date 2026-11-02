import sys
from heapq import heappop, heappush

with open(sys.argv[1]) as f:
    boss_hp, boss_damage = [int(line.split()[-1]) for line in f.read().splitlines()]

SPELLS = [
    {"name": "missile",  "cost": 53,  "damage": 4, "heal": 0, "duration": 0},
    {"name": "drain",    "cost": 73,  "damage": 2, "heal": 2, "duration": 0},
    {"name": "shield",   "cost": 113, "damage": 0, "heal": 0, "duration": 6},
    {"name": "poison",   "cost": 173, "damage": 0, "heal": 0, "duration": 6},
    {"name": "recharge", "cost": 229, "damage": 0, "heal": 0, "duration": 5},
]

def play_game(p2=False) -> int:
    # mp spent, player hp, mp, boss hp, shield timer, poison timer, recharge timer, player turn
    heap = [(0, 50, 500, boss_hp, 0, 0, 0, True)]
    seen: set[tuple[int, int, int, int, int, int, bool]] = set()
    while heap:
        spent, hp, mp, boss, shield, poison, recharge, p_turn = heappop(heap)
        state = (hp, mp, boss, shield, poison, recharge, p_turn)
        if state in seen:
            continue
        seen.add(state)

        if p2 and p_turn:
            hp -= 1

        armor = 0
        if shield > 0:      armor = 7;  shield -= 1
        if poison > 0:      boss -= 3;  poison -= 1
        if recharge > 0:    mp += 101;  recharge -= 1
        if boss <= 0:
            return spent

        timers = {"shield": shield, "poison": poison, "recharge": recharge}
        if p_turn and hp > 0:
            for spell in SPELLS:
                if spell["cost"] > mp:
                    continue
                if spell["duration"] > 0 and timers.get(spell["name"], 0) > 0:
                    continue
                heappush(heap, (
                    spent + spell["cost"],
                    hp + spell["heal"],
                    mp - spell["cost"],
                    boss - spell["damage"],
                    spell["duration"] if spell["name"] == "shield" else shield,
                    spell["duration"] if spell["name"] == "poison" else poison,
                    spell["duration"] if spell["name"] == "recharge" else recharge,
                    False
                ))
        else:
            dmg = max(1, boss_damage - armor)
            if hp - dmg > 0:
                heappush(heap, (spent, hp-dmg, mp, boss, shield, poison, recharge, True))
    return -1   # Player loses in all scenarios

print(f"Part 1: {play_game()}")
print(f"Part 2: {play_game(p2=True)}")