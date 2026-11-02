import sys
from collections import deque
from math import lcm
from typing import TypedDict

class FlipFlop(TypedDict):
    status: bool
    children: list[str]

class Conjunction(TypedDict):
    memory: dict[str, bool]
    children: list[str]

broadcaster: list[str] = []
flipflops: dict[str, FlipFlop] = {}
conjunctions: dict[str, Conjunction] = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        if line.startswith("%"):
            module, children = line.split(" -> ")
            flipflops[module[1:]] = {"status": False, "children": children.split(", ")}
        elif line.startswith("&"):
            module, children = line.split(" -> ")
            conjunctions[module[1:]] = {"memory": {}, "children": children.split(", ")}
        else:
            broadcaster = line.split(" -> ")[1].split(", ")

all_children = {**{k: v["children"] for k, v in flipflops.items()},
                **{k: v["children"] for k, v in conjunctions.items()},
                "broadcaster": broadcaster}
for src, children in all_children.items():
    for child in children:
        if child in conjunctions:
            conjunctions[child]["memory"][src] = False

final = next(name for name, children in all_children.items() if "rx" in children)
watch = {name for name, children in all_children.items() if final in children}
cycle_lengths: dict[str, int] = {}
part1 = [0, 0]
presses = 0
while len(cycle_lengths) < len(watch):
    presses += 1
    part1[0] += 1
    queue = deque([("button", False, broadcaster)])
    while queue:
        src, pulse, dests = queue.popleft()
        part1[pulse] += len(dests)
        if src in watch and pulse and src not in cycle_lengths:
            cycle_lengths[src] = presses
        for dest in dests:
            if dest in flipflops:
                if not pulse:
                    flipflops[dest]["status"] = not flipflops[dest]["status"]
                    queue.append((dest, flipflops[dest]["status"], flipflops[dest]["children"]))
            elif dest in conjunctions:
                conjunctions[dest]["memory"][src] = pulse
                queue.append((dest, not all(conjunctions[dest]["memory"].values()), conjunctions[dest]["children"]))

    if presses == 1000:
        print(f"Part 1: {part1[0] * part1[1]}")

print(f"Part 2: {lcm(*cycle_lengths.values())}")