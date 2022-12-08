from utils import read_text_file_lines
from pathlib import Path
import numpy as np

DIR = Path('2022/puzzle8')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)
shape0 = len(data[0])
shape1 = len(data)
forest = np.array([int(num) for sublist in data for num in sublist]
                  ).reshape(shape0, shape1)


# what is visible?
# all the edge
num_edge = 2*shape0 + 2*(shape1 - 2)
num_inner = 0


for i in range(1, shape0-1, 1):
    for j in range(1, shape1-1, 1):
        height = forest[i][j]
        left = np.count_nonzero(forest[i, :j] >= height)
        right = np.count_nonzero(forest[i, j+1:] >= height)
        above = np.count_nonzero(forest[:i, j] >= height)
        below = np.count_nonzero(forest[i+1:, j] >= height)
        if any([x == 0 for x in [left, right, above, below]]):
            num_inner += 1


scores1 = num_edge + num_inner


# Question 1 - How many trees are visible?
print(
    f"Q1: Number of visible trees: {scores1}")

max_view = 0

for i in range(0, shape0, 1):
    for j in range(0, shape1, 1):
        height = forest[i][j]
        # where is the tree that blocks view?
        # left = forest[np.where(forest[i, :j] >= height), j][0]  # .max()
        left = np.where(forest[i, :j] >= height)[0]  # .max()
        # right = forest[np.where(forest[i, j+1:] >= height), j][0]  # .min()
        right = np.where(forest[i, j+1:] >= height)[0]  # .min()
        # above = forest[i, np.where(forest[:i, j] >= height)][0]  # .max()
        above = np.where(forest[:i, j] >= height)[0]  # .max()
        # below = forest[i, np.where(forest[i+1:, j] >= height)][0]  # .min()
        below = np.where(forest[i+1:, j] >= height)[0]  # .min()
        trees_left = 0
        trees_right = 0
        trees_above = 0
        trees_below = 0
        if len(left) > 0:
            trees_left = j - left.max()
        else:
            trees_left = j
        if len(right) > 0:
            trees_right = right.min() + 1
        else:
            trees_right = shape1 - j - 1
        if len(above) > 0:
            trees_above = i - above.max()
        else:
            trees_above = i
        if len(below) > 0:
            trees_below = below.min() + 1
        else:
            trees_below = shape0 - i - 1

        view_score = trees_left * trees_right * trees_above * trees_below

        max_view = max(max_view, view_score)


scores2 = max_view


# Question 2 - What is the heightest tree view score??
print(
    f"Q2: The heighest tree view score is: {scores2}")
