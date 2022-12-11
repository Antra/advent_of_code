from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle10')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)

value_list = [[0, int(entry.split(' ')[1])] if entry[:4] == 'addx' else [
    0] for entry in data]

value_list = [0] + [item for sublist in value_list for item in sublist]

hit_values = [20, 60, 100, 140, 180, 220]

scores1 = sum([(1+sum(value_list[:val]))*val for val in hit_values])


# Question 1 - What is the scores?
print(
    f"Q1: The scores is: {scores1}")

# can we draw and reshape?
crt_display = []
x = 1

for i, val in enumerate(value_list):
    x += val
    if i % 40 in [x-1, x, x+1]:
        crt_display.append('#')
    else:
        crt_display.append('.')


# Question 2 - Printing the letters
for i in range(0, 241, 40):
    print(''.join(crt_display[i:i+40]))
