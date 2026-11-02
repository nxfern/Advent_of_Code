import sys
import numpy as np

with open(sys.argv[1]) as f:
    algo, image = f.read().split("\n\n")
    image = image.splitlines()

def apply_algo(algo: str, image: list[str], steps: int) -> int:
    algo_arr = np.array([1 if c == "#" else 0 for c in algo], dtype=np.uint8)
    grid = np.array([[1 if c == "#" else 0 for c in row] for row in image], dtype=np.uint8)
    background = 0
    kernel = np.array([[256, 128, 64], [32, 16, 8], [4, 2, 1]])

    for _ in range(steps):
        padded = np.pad(grid, 2, mode="constant", constant_values=background)
        rows, cols = grid.shape

        idx = sum(kernel[i, j] * padded[i:i+rows+2, j:j+cols+2] for i in range(3) for j in range(3))
        grid = algo_arr[idx]
        background = algo_arr[0] if background == 0 else algo_arr[511]

    return int(grid.sum())

print(f"Part 1: {apply_algo(algo=algo, image=image, steps=2)}")
print(f"Part 2: {apply_algo(algo=algo, image=image, steps=50)}")