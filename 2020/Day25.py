import sys

with open(sys.argv[1]) as f:
    card, door = map(int, f.readlines())

m = int(20201227 ** .5) + 1
table: dict[int, int] = {}
val = 1
for j in range(m):
    table[val] = j
    val = val * 7 % 20201227

factor = pow(pow(7, m, 20201227), 20201225, 20201227)
val = card
card_loop = 0
for i in range(m):
    if val in table:
        card_loop = i * m + table[val]
        break
    val = (val * factor) % 20201227

print(f"Answer: {pow(door, card_loop, 20201227)}")