import sys

with open(sys.argv[1]) as f:
    polymer = f.read()

def react(pol: str) -> list[str]:
    stack: list[str] = []
    for p in pol:
        if stack and stack[-1] != p and stack[-1].lower() == p.lower():
            stack.pop()
        else:
            stack.append(p)
    return stack

reacted = react(polymer.strip())
print(f"Part 1: {len(reacted)}")

part2 = float("inf")
for p in set(c.lower() for c in reacted):
    part2 = min(part2, len(react("".join(c for c in reacted if c.lower() != p))))
print(f"Part 2: {part2}")