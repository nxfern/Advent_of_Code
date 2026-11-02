import sys

def solve(data):
    target_str = data.strip()
    target = [int(c) for c in target_str]
    target_num = int(target_str)
    target_len = len(target)
    recipes = [3, 7]
    i1, i2 = 0, 1
    found_part2 = None

    while found_part2 is None or len(recipes) < target_num + 10:
        v1 = recipes[i1]
        v2 = recipes[i2]
        s = v1 + v2

        if s >= 10:
            recipes.append(1)
            recipes.append(s - 10)
            if found_part2 is None:
                pos = len(recipes) - target_len - 1
                if pos >= 0 and recipes[pos:pos + target_len] == target:
                    found_part2 = pos
                else:
                    pos += 1
                    if recipes[pos:pos + target_len] == target:
                        found_part2 = pos
        else:
            recipes.append(s)
            if found_part2 is None:
                pos = len(recipes) - target_len
                if pos >= 0 and recipes[pos:pos + target_len] == target:
                    found_part2 = pos

        n = len(recipes)
        i1 = (i1 + 1 + v1) % n
        i2 = (i2 + 1 + v2) % n

    print(f'Part 1: {"".join(map(str, recipes[target_num:target_num + 10]))}')
    print(f'Part 2: {found_part2}')

with open(sys.argv[1]) as f:
    solve(f.read())