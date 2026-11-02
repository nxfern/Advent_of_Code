import sys
from functools import cache

rules: dict[str, str | list[list[str]]] = {}
with open(sys.argv[1]) as f:
    lines, messages = f.read().split("\n\n")
    messages = messages.splitlines()
    for line in lines.splitlines():
        key, val = line.split(": ")
        rules[key] = val[1:-1] if '"' in val else [alt.split() for alt in val.split(" | ")]

@cache
def matches(rule_id: str, s: str, i: int) -> frozenset[int]:
    rule = rules[rule_id]
    if isinstance(rule, str):
        if i < len(s) and s[i] == rule:
            return frozenset({i + 1})
        return frozenset()
    
    result = set()
    for alt in rule:
        pos = {i}
        for sub_rule in alt:
            pos = set().union(*(matches(sub_rule, s, k) for k in pos))
        result |= pos
    return frozenset(result)

print(f"Part 1: {sum(len(m) in matches("0", m, 0) for m in messages)}")

# altering ruleset for part 2
matches.cache_clear()   # clearing the cache from part 1
rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]
print(f"Part 2: {sum(len(m) in matches("0", m, 0) for m in messages)}")