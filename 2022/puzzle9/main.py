from utils import read_text_file_lines
from pathlib import Path
import numpy as np
import math

DIR = Path('2022/puzzle9')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)
# what size should it be?? let's just try to hardcode
shape0 = 500
shape1 = 500
overview = np.array(['.']*shape0*shape1).reshape(shape0, shape1)

visited = set()

# in the sample, we start in the lower left corner, which has 's', 'T' overlapped by 'H'
# overview[-1, 0] = 'H'
# in the input however, let's start in the middle, so we have space to move around; it seems to work with a 500x500 map
overview[round(shape0/2), round(shape1/2)] = 'H'

# rope definition
# ['H', 'T']
# ['H', 1, 2, 3, 4, 5, 6, 7, 8, 9]
#rope_def = ['H', 'T']
rope_def = ['H', 1, 2, 3, 4, 5, 6, 7, 8, 9]

coords = {k: np.argwhere(overview == 'H')[0]
          for k in rope_def}


def _visited(knot, coord, endknots=['T', 9]):
    if knot in endknots:
        visited.add(tuple(coord))


def _update(direction, pair1, pair2=None, move1=True):
    new_pair1 = pair1.copy()
    if move1:
        # move first pair
        if direction == 'R':
            # move right; aka [x; y+1]
            new_pair1[1] = new_pair1[1] + 1
        if direction == 'L':
            # move left; aka [x; y-1]
            new_pair1[1] = new_pair1[1] - 1
        if direction == 'U':
            # move up; aka [x-1; y]
            new_pair1[0] = new_pair1[0] - 1
        if direction == 'D':
            # move down; aka [x+1; y]
            new_pair1[0] = new_pair1[0] + 1

    if pair2 is not None:
        # what is the distance?
        dist = np.linalg.norm(new_pair1 - pair2)
        new_pair2 = pair2.copy()
        if dist >= 1.5:  # diagonal dist is ~1.4
            # if 'H' and 'T' are in the same row/column, T must take a step towards 'H'
            # otherwise 'T' must take a diagonal step towards 'H'
            hor = new_pair1[1] - new_pair2[1]
            ver = new_pair1[0] - new_pair2[0]
            if hor < 0:
                hor = -1
            elif hor > 0:
                hor = 1
            if ver < 0:
                ver = -1
            elif ver > 0:
                ver = 1
            new_pair2[1] = new_pair2[1] + hor
            new_pair2[0] = new_pair2[0] + ver

        return new_pair1, new_pair2
    else:
        return new_pair1


def _update_old(direction):
    # h_loc = np.where(overview == 'H')
    h_loc = np.argwhere(overview == 'H')
    new_h = h_loc.copy()
    if 'T' in overview:
        t_loc = np.argwhere(overview == 'T')
    else:
        t_loc = h_loc
    # ensure we have recorded this visit
    visited.add(tuple(t_loc[0]))

    # move H
    if direction == 'R':
        # move right; aka [x; y+1]
        new_h[0, 1] = new_h[0, 1] + 1
    if direction == 'L':
        # move left; aka [x; y-1]
        new_h[0, 1] = new_h[0, 1] - 1
    if direction == 'U':
        # move up; aka [x-1; y]
        new_h[0, 0] = new_h[0, 0] - 1
    if direction == 'D':
        # move down; aka [x+1; y]
        new_h[0, 0] = new_h[0, 0] + 1
    # update the map so we can follow visually
    if all(h_loc[0] == t_loc[0]):
        overview[h_loc[0, 0], h_loc[0, 1]] = 'T'
    else:
        overview[h_loc[0, 0], h_loc[0, 1]] = '.'
    overview[new_h[0, 0], new_h[0, 1]] = 'H'
    # update T?
    t_dist = np.linalg.norm(new_h - t_loc)
    if t_dist >= 1.5:
        new_t = t_loc.copy()
        # if 'H' and 'T' are in the same row/column, T must take a step towards 'H'
        # otherwise 'T' must take a diagonal step towards 'H'
        hor = new_h[0, 1] - t_loc[0, 1]
        ver = new_h[0, 0] - t_loc[0, 0]
        if hor < 0:
            hor = -1
        elif hor > 0:
            hor = 1
        if ver < 0:
            ver = -1
        elif ver > 0:
            ver = 1
        new_t[0, 1] = new_t[0, 1] + hor
        new_t[0, 0] = new_t[0, 0] + ver
        overview[t_loc[0, 0], t_loc[0, 1]] = '.'
        if not all(new_t[0] == new_h[0]):
            overview[new_t[0, 0], new_t[0, 1]] = 'T'

        # ensure we have recorded this visit
        visited.add(tuple(new_t[0]))


# NB, this takes a few minutes to run for the full input
for entry in data:
    direction, length = entry.split(' ')
    for step in range(int(length)):
        # first move 'H', then move the rest accordingly
        coord = coords.get('H')
        coords['H'] = _update(direction, coord)

        for i in range(1, len(rope_def)):
            prev = rope_def[i-1]
            knot = rope_def[i]
            coord1 = coords.get(prev)
            coord2 = coords.get(knot)
            _visited(knot, coord2)
            new1, new2 = _update(direction, coord1, coord2, move1=False)
            coords[knot] = new2
            _visited(knot, new2)

scores1 = len(visited)


# Question 1 - How many places did the Tail visit?
print(
    f"Q1: The tail visited: {scores1} places")


# NB, this takes a few minutes to run for the full input
for entry in data:
    direction, length = entry.split(' ')
    for step in range(int(length)):
        # first move 'H', then move the rest accordingly
        coord = coords.get('H')
        coords['H'] = _update(direction, coord)

        for i in range(1, len(rope_def)):
            prev = rope_def[i-1]
            knot = rope_def[i]
            coord1 = coords.get(prev)
            coord2 = coords.get(knot)
            _visited(knot, coord2)
            new1, new2 = _update(direction, coord1, coord2, move1=False)
            coords[knot] = new2
            _visited(knot, new2)


scores2 = max_view


# Question 2 - What is the heightest tree view score??
print(
    f"Q2: The heighest tree view score is: {scores2}")
