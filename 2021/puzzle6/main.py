from collections import Counter
import numpy as np

file = '2021/puzzle6/input.txt'

with open(file, 'r') as f:
    content = f.read()

#content_list = content.split('\n')
numbers = [int(number) for number in content.split(',')]


class Lanternfish(object):
    def __init__(self, timer) -> None:
        self.timer = timer

    # def __repr__(self):
    #     return '< Lanternfish >'

    def make_turn(self):
        if self.timer == 0:
            self.proliferate()
            self.timer = 6
        else:
            self.timer -= 1

    def proliferate(self):
        fish_school.append(Lanternfish(8))


fish_school = [Lanternfish(timer) for timer in numbers]


for turn in range(0, 80, 1):
    _ = [fish.make_turn() for fish in fish_school[:]]


print(
    f'How many fish are there in the fish school after 80 days? {len(fish_school)}')

# 362666 after 80 days -- remember to run the turns on a copy of the list!


# part 2 - how about after 256 days?
for turn in range(0, 256, 1):
    _ = [fish.make_turn() for fish in fish_school[:]]


print(
    f'How many fish are there in the fish school after 256 days? {len(fish_school)}')

# Started around 8:30 - didn't finish yet at 10:00
# This takes forever to calculate even on 32GB RAM -- I need to find another approach!!


# part 2 - approach two; let's try with a Numpy array and logic instead.
fish_school = np.array([timer for timer in numbers])

days = 256

for turn in range(0, days, 1):
    print(f'Starting turn #{turn}')
    # first we see if we need to create new fish
    new_fish = np.count_nonzero(fish_school == 0)
    # then we reduce all the fish by 1
    fish_school -= 1
    #  add the new fish and reset the birthing fish to 6
    fish_school = np.append(fish_school, [8]*new_fish)
    fish_school[np.where(fish_school == -1)] = 6


print(
    f'How many fish are there in the fish school after {days} days? {fish_school.size}')

# This fails after 187 days, so new appraoch
# 188797604 -> too low


# Part 2 -- approach 3, what if I just keep track of how many there are at each timer point?
freq_dict = Counter(numbers)

fish_school = [0]*9

for k, v in freq_dict.items():
    fish_school[k] = v


days = 256

for turn in range(0, days, 1):
    print(f'Starting turn #{turn}')
    # pop the item at index#0 to get the number of new fish as well as reducing all counters by 1
    new_fish = fish_school.pop(0)
    fish_school.append(0)
    # then add new fish back to position 6 (self) and position 8 (child)
    fish_school[6] = fish_school[6] + new_fish
    fish_school[8] = new_fish


print(
    f'How many fish are there in the fish school after {days} days? {sum(fish_school)}')
