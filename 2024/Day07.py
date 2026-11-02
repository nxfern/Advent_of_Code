import sys

equations: list[tuple[int, list[int]]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        t, nums = line.split(": ")
        equations.append((int(t), list(map(int, nums.split()))))

def possible(target: int, nums: list[int], concat: bool = False) -> bool:
    if len(nums) == 1:
        return target == nums[0]
    *rem, n = nums
    if target % n == 0 and possible(target // n, rem, concat):
        return True
    if target >= n and possible(target - n, rem, concat):
        return True
    if concat:
        st, sn = str(target), str(n)
        if st != sn and st.endswith(sn):
            return possible(int(st[:-len(sn)]), rem, concat)
    return False

print(f"Part 1: {sum(k for k, n in equations if possible(k, n))}")
print(f"Part 2: {sum(k for k, n in equations if possible(k, n, concat=True))}")