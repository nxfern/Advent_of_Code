import sys
from collections import defaultdict

OPS = {"AND": lambda a, b: a & b,
       "OR": lambda a, b: a | b,
       "XOR": lambda a, b: a ^ b,}

with open(sys.argv[1]) as f:
    top, bottom = f.read().split("\n\n")
    wires: dict[str, int] = {}
    for line in top.splitlines():
        name, bit = line.split(": ")
        wires[name] = int(bit)
    gates: list[tuple[str, str, str, str]] = []
    for line in bottom.splitlines():
        a, op, b, _, out = line.split()
        gates.append((a, op, b, out))


rule = {out: (a, op, b) for a, op, b, out in gates}
cache = dict(wires)

def val(w):
    if w in cache:
        return cache[w]
    a, op, b = rule[w]
    cache[w] = r = OPS[op](val(a), val(b))
    return r

zs = sorted((w for w in rule if w[0] == "z"), reverse=True)
print(f"Part 1: {int(''.join(str(val(z)) for z in zs), 2)}")

last_z = max(out for *_, out in gates if out[0] == "z")
used_by = defaultdict(set)
for a, op, b, _ in gates:
    used_by[a].add(op)
    used_by[b].add(op)

bad = set()
for a, op, b, out in gates:
    from_xy = a[0] in "xy" and b[0] in "xy"
    is_first = {a, b} == {"x00", "y00"}

    if out[0] == "z":
        if out == last_z:
            if op != "OR":
                bad.add(out)
        elif op != "XOR":
            bad.add(out)
        continue

    if op == "XOR" and not from_xy:
        bad.add(out)
    elif op == "XOR" and from_xy and not is_first and "XOR" not in used_by[out]:
        bad.add(out)
    elif op == "AND" and not is_first and "OR" not in used_by[out]:
        bad.add(out)
    elif op == "OR" and not {"XOR", "AND"} <= used_by[out]:
        bad.add(out)

print(f"Part 2: {','.join(sorted(bad))}")