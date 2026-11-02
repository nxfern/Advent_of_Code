import sys
from functools import reduce
from operator import xor

with open(sys.argv[1]) as f:
    raw = f.read()

def knot_hash(data: str, p2: bool = False) -> int | str:
    if p2:
        lengths = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    else:
        lengths = list(map(int, data.split(",")))

    nums = list(range(256))
    l = len(nums)
    i = skip = 0
    for _ in range(64):
        for lng in lengths:
            indices = [(i + j) % l for j in range(lng)]
            values = [nums[idx] for idx in indices][::-1]
            for idx, val in zip(indices, values):
                nums[idx] = val
            i = (i + lng + skip) % l
            skip += 1

        if not p2:
            return nums[0] * nums[1]

    dense = [reduce(xor, nums[i:i+16]) for i in range(0, 256, 16)]
    return "".join(f"{x:02x}" for x in dense)

if __name__ == "__main__":
    print(f"Part 1: {knot_hash(raw)}")
    print(f"Part 2: {knot_hash(raw, p2=True)}")