file = '2021/puzzle7/input.txt'

with open(file, 'r') as f:
    content = f.read()

# content_list = content.split('\n')
numbers = [int(number) for number in content.split(',')]


# positions are from 0 to 1936 -- can I just calculate them all and pick the one with lowest overall cost?

best_position = sum(numbers) / len(numbers)
best_score = sum(numbers)

for position in range(min(numbers), max(numbers)+1, 1):
    position_score = sum([abs(number-position) for number in numbers])
    if position_score < best_score:
        best_score = position_score
        best_position = position

print(
    f'The best position is {best_position} which has a move cost of {best_score}')


# Part 2 -- the cost is increasing by 1 with each step; i.e. first step costs 1, second step costs 2, etc.
best_position = 0
best_score = 215280818


def range_calc(start, stop):
    return sum(range(start, stop+1, 1)) if start <= stop else sum(range(stop, start+1, 1))


for position in range(min(numbers), max(numbers)+1, 1):
    position_score = sum([range_calc(0, abs(position-number))
                         for number in numbers])
    if position_score < best_score:
        best_score = position_score
        best_position = position

print(
    f'The best position is {best_position} which has a move cost of {best_score}')
