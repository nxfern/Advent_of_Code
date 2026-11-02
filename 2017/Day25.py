import sys
from collections import defaultdict
import re

State = dict[int, tuple[int, int, str]]

def regex_line(line: str) -> int:
    return int(m.group()) if (m := re.search(r"\d+", line)) else -2

states: dict[str, State] = {}
with open(sys.argv[1]) as f:
    blocks = [b.splitlines() for b in f.read().split("\n\n")]
    start = blocks[0][0].split()[-1].strip(".")
    steps = regex_line(blocks[0][1])
    for block in blocks[1:]:
        state = block[0].split()[-1].strip(":")
        lines = block[1:]
        states[state] = {
            regex_line(lines[i]): (
                regex_line(lines[i+1]),
                -1 if lines[i+2].split()[-1].strip(".") == "left" else 1,
                lines[i+3].split()[-1].strip("."))
            for i in range(0, len(lines), 4)
        }

def checksum(states: dict[str, State], curr_state: str):   # local vars > global vars for large loops
    tape: defaultdict[int, int] = defaultdict(int)
    pos = 0
    for _ in range(steps):
        val, move, curr_state = states[curr_state][tape[pos]]
        tape[pos] = val
        pos += move
    return tape.values()

print(f"Answer: {sum(checksum(states, start))}")