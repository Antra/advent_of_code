import numpy as np


file = '2021/puzzle4/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')
numbers = [int(number) for number in content_list.pop(0).split(',')]


class Board(object):
    """helper class to hold the individual Bingo boards"""

    def __init__(self, id) -> None:
        self.id = id
        self.board = np.zeros((5, 5), dtype=int)
        self.scores = np.zeros((5, 5), dtype=int)

    def __repr__(self) -> str:
        return '< Board ID: ' + str(self.id) + ' >'

    def add_row(self, row, row_index=None):
        try:
            row_index = np.where(np.sum(self.board, axis=1) == 0)[0].min()
            self.board[row_index, :] = row
        except ValueError as e:
            print('Board already has 5 rows')

    def get_row(self, row_index):
        return self.board[row_index, :]

    def get_column(self, col_index):
        return self.board[:, col_index]

    def number_exists(self, number):
        return number in self.board.flatten()

    def mark_number(self, number):
        # no need to check if the number is on the board as the array is returned as empty and setting empty array to a value is nothing
        row_index, col_index = np.where(self.board == number)
        self.scores[row_index, col_index] = 1

    def check_win(self):
        # we will have score of 5 in either in the row or the column array then
        return 5 in np.sum(self.scores, axis=0) or 5 in np.sum(self.scores, axis=1)

    def get_unmarked(self):
        # get the sum of the values that are not yet marked as '1'
        row_index, col_index = np.where(self.scores == 0)
        return self.board[row_index, col_index].sum()

    def get_info(self):
        print(f'Board is ID: {self.id}')
        print(self.board)
        print(self.scores)


# Tests and trials
#[number for number in test.split(' ')]
# test = Board(1)

# row1 = ['45', '16', '46', '65', '21']
# row2 = ['60', '54', '43', '12', '1']
# row3 = ['20', '23', '42', '56', '81']
# row4 = ['89', '80', '52', '26', '32']
# row5 = ['73', '78', '47', '2', '7']

# #test = np.array([row1, row2, row3, row4, row5], dtype=np.int8)
# test.add_row(row1)
# test.add_row(row2)
# test.add_row(row3)
# test.add_row(row4)
# test.add_row(row5)
# test.get_info()

# row_index, col_index = np.where(test == 56)
# test[row_index, col_index][0]

# scores = np.zeros((5, 5), dtype=int)
# #scores[row_index, col_index] = 1
# scores[:, col_index] = 1
# scores[:, col_index].sum()
# scores[row_index, :].sum()


# # give the sums of either all the rows or all the columns:
# np.sum(scores, axis=0)
# np.sum(scores, axis=1)


def execute_round(boards, number):
    # If there's only one unwon board, then get the ID of that board as Loser ID
    # TODO: If there are multiple draws left before that board would win this would throw an error as loser_id does not exist in that iteration!
    if [board.check_win() for board in boards].count(True) == len(boards) - 1:
        loser_id = [board.check_win() for board in boards].index(False)
        print(
            f'Only one board has a positive remainder score of 1! It is Board ID: {loser_id}')

    for board in boards:
        board.mark_number(number)

    # do we have a win yet?
    if any([board.check_win() for board in boards]):
        winner_id = [board.check_win() for board in boards].index(True)
        score = boards[winner_id].get_unmarked()
        print(
            f'We have a winner!! Board at index {winner_id} has won!')
        print(
            f'Most recent number was: {number}, unmarked score on the board is: {score}')
        print(f'So the Product is: {number*score}')

    if [board.check_win() for board in boards].count(True) == len(boards):
        score = boards[loser_id].get_unmarked()
        print(
            f'All boards have now won, the remainder score of the loser board is {score}')
        print(
            f'And as the last number drawn was: {number}, it means the product is {number*score}')


# run the initial setup of the boards
boards = []
board_id = 0
for row in content_list:
    if row == '':
        # this is an empty row, so create a new board and increment the ID
        #print(f'adding a new board, board id: {board_id}')
        boards.append(Board(board_id))
        board_id += 1
    else:
        # add the row to the last board in the boards list
        temp = row.replace('  ', ' ').strip().split(' ')
        #print(f'adding the row {temp} to most recent board')
        boards[-1].add_row(temp)


# then run the simulation
# It's the 14th round that finds a winner
while not any([board.check_win() for board in boards]):
    next_number = numbers.pop(0)
    execute_round(boards, next_number)


# Part 2
# I added the get_remaining function as well, now we have to run until only 1 board has not won yet and then inspect the remaining board
while not [board.check_win() for board in boards].count(True) == len(boards):
    next_number = numbers.pop(0)
    execute_round(boards, next_number)
