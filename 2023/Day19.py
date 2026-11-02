import sys, math, re

with open(sys.argv[1]) as f:
    flows_raw, rats_raw = f.read().split("\n\n")

workflows: dict[str, list[tuple[str, str, int, str]]] = {}
for line in flows_raw.splitlines():
    m = re.match(r"(\w+)\{(.+)\}", line)
    assert m
    name, body = m.groups()
    *rules, default = body.split(",")
    parsed = []
    for rule in rules:
        cond, dest = rule.split(":")
        key, op, val = cond[0], cond[1], int(cond[2:])
        parsed.append((key, op, val, dest))
    parsed.append(("", "", 0, default))  # unconditional fallthrough
    workflows[name] = parsed

part1 = 0
for line in rats_raw.splitlines():
    rating = {k: int(v) for k, v in re.findall(r"(\w)=(\d+)", line)}
    curr = "in"
    while curr not in "AR":
        for key, op, val, dest in workflows[curr]:
            if not key or (rating[key] < val if op == "<" else rating[key] > val):
                curr = dest
                break
    if curr == "A":
        part1 += sum(rating.values())

def count(curr: str, ranges: dict[str, tuple[int, int]]) -> int:
    if curr == "R":
        return 0
    if curr == "A":
        return math.prod(hi - lo + 1 for lo, hi in ranges.values())

    total = 0
    for key, op, val, dest in workflows[curr]:
        if not key:
            total += count(dest, ranges)
            break

        lo, hi = ranges[key]
        if op == "<":
            t_lo, t_hi, f_lo, f_hi = lo, min(hi, val - 1), max(lo, val), hi
        else:
            t_lo, t_hi, f_lo, f_hi = max(lo, val + 1), hi, lo, min(hi, val)

        if t_lo <= t_hi:
            total += count(dest, {**ranges, key: (t_lo, t_hi)})
        if f_lo > f_hi:
            break
        ranges = {**ranges, key: (f_lo, f_hi)}
    return total

print(f"Part 1: {part1}")
print(f"Part 2: {count("in", {c: (1, 4000) for c in "xmas"})}")