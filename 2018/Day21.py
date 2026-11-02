import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    seti = int(lines[8].split()[1])
    bani_small = int(lines[9].split()[2])
    bori = int(lines[7].split()[2])
    bani_large = int(lines[11].split()[2])
    muli = int(lines[12].split()[2])
    gtir = int(lines[14].split()[1])

seen = set()
c, last_unique_c = 0, -1
part1, part2 = None, None
while True:
    a = c | bori
    c = seti

    while True:
        c = (((c + (a & bani_small)) & bani_large) * muli) & bani_large

        if gtir > a:
            if part1 is None:
                part1 = c

            if c not in seen:
                seen.add(c)
                last_unique_c = c
                break
            else:
                part2 = last_unique_c
                break
        else:
            a //= gtir
    
    if part2 is not None:
        break

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')