from utils import splitter
from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle5')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)

towers, moves = [item for item in splitter(data)]


def construct_towers(data):
    construct = {1: [],
                 2: [],
                 3: [],
                 4: [],
                 5: [],
                 6: [],
                 7: [],
                 8: [],
                 9: []}
    data.reverse()
    for i, row in enumerate(data):
        if i > 0:
            for j, start in enumerate(range(0, len(row), 4)):
                end = start + 3
                block = row[start:end]
                if block != '   ':
                    construct.get(j+1).append(block[1])

    return construct


def play_moves(data, round2=False):
    # a move consists of:
    # move int from int to int
    _, num, _, source, _, destination = data.split(' ')
    num = int(num)
    source = int(source)
    destination = int(destination)
    if not round2:
        for move in range(num):
            block = towers.get(source, []).pop()
            towers.get(destination).append(block)
    elif round2:
        start = (num)*-1
        blocks = towers.get(source, [])[start:]
        towers[source] = towers.get(source, [])[:start]
        [towers.get(destination).append(block) for block in blocks]


towers = construct_towers(towers)
[play_moves(move) for move in moves]


scores1 = ''.join([towers.get(num)[-1]
                  for num in range(1, 10) if towers.get(num) != []])


# Question 1 - what does the top boxes look like after moving all moves?
print(
    f"Q1: The top boxes are: {scores1}")


towers = construct_towers(towers)
[play_moves(move, round2=True) for move in moves]


scores2 = ''.join([towers.get(num)[-1]
                  for num in range(1, 10) if towers.get(num) != []])


# Question 2 - what does the top boxes look like after moving all moves on the CrateMover 9001?
print(
    f"Q2: When using the CrateMover 9001, the top boxes are {scores2}")
