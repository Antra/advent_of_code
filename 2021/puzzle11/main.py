import numpy as np
file = '2021/puzzle11/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')

# content_list = ['5483143223',
#                 '2745854711',
#                 '5264556173',
#                 '6141336146',
#                 '6357385478',
#                 '4167524645',
#                 '2176841721',
#                 '6882881134',
#                 '4846848554',
#                 '5283751526']

numbers = [int(number) for row in content_list for number in row]


def get_neighbours(array, row, col, d=1, increment=0):
    """Returns the surrounding elements from a specific row, col index location

    Args:
        array ([np.array]): the NumPy array to get the neighbours from
        row ([int]): the row index of the centre
        col ([int]): the col index of the centre
        d (int, optional): the distance around the centre to gather neighbours from. Defaults to 1.
        increment (int, optional): which incremental value should be used before returning the array?. Defaults to 0.

    Returns:
        [np.array]: the resulting NumPy array of the centre and its neighbours
    """
    left = max(0, row-d)
    right = min(array.shape[0]+1, row+d+1)
    top = max(0, col-d)
    bottom = min(array.shape[1]+1, col+d+1)

    array[left:right, top:bottom] += increment

    return array


# first everyone is increased by 1
# then anyone higher than 9 flashes to all the diagonals around them
# then anyone NOW at 9 also flashes, etc. etc.
# then finally anyone that has flashed will reset their energy to 0
def take_turn():
    global map, flash_counter, first_sync_step, turn, highest_flashes
    map += 1
    while np.count_nonzero((map >= 10) & (map < 100)):
        row, col = np.where((map >= 10) & (map < 100))
        for loc in zip(row, col):
            # set the already flashed so high they won't be taken again
            map[loc[0], loc[1]] = 100
            flash_counter += 1
            map = get_neighbours(map, loc[0], loc[1], d=1, increment=1)
    # and finally reset the flashed back to 0
    map[np.where(map >= 100)] = 0
    if len(map[np.where(map == 0)]) == map.size:
        first_sync_step = min(turn, first_sync_step)


flash_counter = 0
number_turns = 1000
first_sync_step = number_turns + 1
map = np.array(numbers).reshape(10, 10)
for turn in range(number_turns):
    take_turn()


print(f'After {number_turns} turns, there have been {flash_counter} flahes and the first sync flash was after step# {first_sync_step+1}')
