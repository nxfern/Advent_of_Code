import sys, heapq

disk: list[int | None] = []
files: list[list[int]] = []
free_heaps: list[list[int]] = [[] for _ in range(10)]
pos = 0
with open(sys.argv[1]) as f:
    for i, d in enumerate(f.read()):
        n = int(d)
        if i % 2 == 0:
            disk.extend([i//2] * n)
            files.append([i//2, pos, n])
        elif n > 0:
            heapq.heappush(free_heaps[n], pos)
            disk.extend([None] * n)
        pos += n

left, right = 0, len(disk) - 1
while left < right:
    if disk[left] is not None:
        left += 1
    elif disk[right] is None:
        right -= 1
    else:
        disk[left], disk[right] = disk[right], disk[left]
        left += 1
        right -= 1

print(f"Part 1: {sum(i * v for i, v in enumerate(disk) if v is not None)}")

for fid, fpos, fsize in reversed(files):
    best_size, best_pos = -1, float("inf")
    for size in range(fsize, 10):
        if free_heaps[size] and free_heaps[size][0] < best_pos:
            best_pos, best_size = free_heaps[size][0], size
    if best_size != -1 and best_pos < fpos:
        heapq.heappop(free_heaps[best_size])
        assert isinstance(best_pos, int)    # satisfying Pylance complaint
        files[fid][1] = best_pos
        leftover = best_size - fsize
        if leftover > 0:
            heapq.heappush(free_heaps[leftover], best_pos + fsize)

print(f"Part 2: {sum(fid * (size * pos + size * (size - 1) // 2) for fid, pos, size in files)}")