import numpy as np

file = '2021/puzzle5/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')


def rrange(start, stop):
    """helper function to generate a range going either direction"""
    return range(start, stop+1) if stop >= start else range(start, stop-1, -1)


class Board(object):
    def __init__(self, id) -> None:
        self.id = id
        self.grid = np.zeros((999, 999), dtype=int)

    def __repr__(self) -> str:
        return '< Board ID: ' + str(self.id) + ' >'

    def add_line(self, x1, y1, x2, y2, diagonals=False):
        if x1 == x2 or y1 == y2:
            self.grid[rrange(y1, y2), rrange(x1, x2)] += 1
        elif diagonals and abs(x1-x2) == abs(y1-y2):
            self.grid[rrange(y1, y2), rrange(x1, x2)] += 1

    def get_crossings(self, threshold):
        return self.grid[np.where(self.grid >= threshold)].size


# Create the board and add the lines from the coords
board = Board(1)
for coords in content_list:
    coord1, coord2 = coords.split(' -> ')
    x1, y1 = coord1.split(',')
    x2, y2 = coord2.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    board.add_line(x1, y1, x2, y2)


# Part 1
board.get_crossings(2)


# Part 2 - recreate board and add the diagonals.
board = Board(1)
for coords in content_list:
    coord1, coord2 = coords.split(' -> ')
    x1, y1 = coord1.split(',')
    x2, y2 = coord2.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    board.add_line(x1, y1, x2, y2, diagonals=True)


board.get_crossings(2)
