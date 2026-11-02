import sys
import re
from typing import NamedTuple, Callable

def swap_pos(s: str, a: str | int, b: str | int) -> str:
    a, b = sorted((int(a), int(b)))
    return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

def swap_letter(s: str, a: str, b: str) -> str:
    return swap_pos(s, s.index(a), s.index(b))

def rotate_basic(s: str, direction: str, count: str | int) -> str:
    count = int(count) % len(s)
    if count == 0:
        return s
    if direction == "left":
        return s[count:] + s[:count]
    return s[-count:] + s[:-count]

def rotate_basic_rev(s: str, direction: str, count: str | int) -> str:
    return rotate_basic(s, "left" if direction == "right" else "right", count)

def rotate_letter(s: str, letter: str) -> str:
    i = s.index(letter)
    steps = 1 + i + (1 if i >= 4 else 0)
    return rotate_basic(s, "right", steps)

def rotate_letter_rev(s: str, letter: str) -> str:
    for i in range(len(s)):
        candidate = rotate_basic(s, "left", i)
        if rotate_letter(candidate, letter) == s:
            return candidate
    raise ValueError(f"Cannot reverse rotate_letter for: {s}, {letter}")

def reverse_range(s: str, a: str | int, b: str | int) -> str:
    a, b = int(a), int(b)
    return s[:a] + s[a:b+1][::-1] + s[b+1:]

def move_pos(s: str, a: str | int, b: str | int) -> str:
    lst = list(s)
    lst.insert(int(b), lst.pop(int(a)))
    return ''.join(lst)

def move_pos_rev(s: str, a: str | int, b: str | int) -> str:
    return move_pos(s, b, a)

class Instruction(NamedTuple):
    pattern: str
    func: Callable
    func_rev: Callable

INSTRUCTIONS = [
    Instruction(r"swap position (\d+) with position (\d+)", swap_pos,       swap_pos),
    Instruction(r"swap letter (\w) with letter (\w)",       swap_letter,    swap_letter),
    Instruction(r"rotate (left|right) (\d+) step",          rotate_basic,   rotate_basic_rev),
    Instruction(r"rotate based on position of letter (\w)", rotate_letter,  rotate_letter_rev),
    Instruction(r"reverse positions (\d+) through (\d+)",   reverse_range,  reverse_range),
    Instruction(r"move position (\d+) to position (\d+)",   move_pos,       move_pos_rev),
]

def apply_instructions(text: str, lines: list[str], reverse: bool = False) -> str:
    for line in (reversed(lines) if reverse else lines):
        instr = next((i for i in INSTRUCTIONS if re.match(i.pattern, line)), None)
        if instr:
            m = re.match(instr.pattern, line)
            if m:
                args = m.groups()
                text = (instr.func_rev if reverse else instr.func)(text, *args)
    return text

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

print(f"Part 1: {apply_instructions('abcdefgh', lines)}")
print(f"Part 2: {apply_instructions('fbgdceah', lines, reverse=True)}")