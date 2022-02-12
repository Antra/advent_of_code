import numpy as np
from utils import get_data
file = '2021/puzzle13/input.txt'
data = get_data(file)

# sample data
# data = ['6,10',
#         '0,14',
#         '9,10',
#         '0,3',
#         '10,4',
#         '4,11',
#         '6,0',
#         '6,12',
#         '4,1',
#         '0,13',
#         '10,12',
#         '3,4',
#         '3,0',
#         '8,4',
#         '1,10',
#         '2,14',
#         '8,10',
#         '9,0',
#         '',
#         'fold along y=7',
#         'fold along x=5']


def folding(paper, axis, index):
    new_paper = paper[:, 0:index] if axis == 'x' else paper[0:index, :]
    folded = paper[:, index+1:] if axis == 'x' else paper[index+1:, :]
    dots_along_y, dots_along_x = np.where(folded == '#')
    # dots_along_x *= -1 if axis == 'x' else 1
    # dots_along_y *= -1 if axis == 'y' else 1
    dots_along_y = np.abs(dots_along_y - (index -
                          1)) if axis == 'y' else dots_along_y
    dots_along_x = np.abs(dots_along_x - (index -
                          1)) if axis == 'x' else dots_along_x

    new_paper[dots_along_y, dots_along_x] = '#'

    return new_paper


instructions = [item for item in data if 'fold along' in item]
data = [item for item in data if ',' in item]


paper_size = max([max(int(item.split(',')[0]), int(item.split(',')[1]))
                  for item in data])+1


paper = np.full([paper_size, paper_size], dtype=str, fill_value='.')
for coor in data:
    x, y = coor.split(',')
    x, y = int(x), int(y)
    # NB, numpy axis=0 is downwards (y) and axis=1 is rightwards (x)
    paper[y, x] = '#'


print(
    f"Paper initialised, there are {len(paper[np.where(paper == '#')])} points")


# part1
instruction = instructions.pop(0)
instruction = instruction.split(' ')[-1]
axis, index = instruction.split('=')
paper = folding(paper, axis, int(index))
print(
    f"Folding done, there are {len(paper[np.where(paper == '#')])} points")


# part2 (execute remaining foldings)
np.set_printoptions(edgeitems=30, linewidth=1000)
for instruction in instructions:
    instruction = instruction.split(' ')[-1]
    axis, index = instruction.split('=')
    paper = folding(paper, axis, int(index))

print(
    f"Folding done, there are {len(paper[np.where(paper == '#')])} points")

# the string is too wide, so print on two lines
paper[:, :20]
paper[:, 20:]
