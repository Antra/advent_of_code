from utils import read_text_file_lines
from pathlib import Path
import re
import numpy as np

DIR = Path('2024/puzzle4')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'


data = read_text_file_lines(file)

data = [list(line) for line in data if line != ""]

# as the data is read; we can search forwards and backwards
layout = np.array(data)
# transposed; so first column is first row and last column is last row
layout_tr = np.transpose(data)
# the counter-clockwise rotation of the layout (same as np.flipud(transposed))
layout_rot = np.rot90(m=data, k=1, axes=(0, 1))


def count_pattern(char_list, search_string, counter=0):
    pattern = re.compile(fr"(?={search_string})")
    char_str = "".join(char_list)
    matches = [match for match in re.finditer(
        pattern=pattern, string=char_str)]
    counter += len(matches)
    char_str_rev = char_str[::-1]
    matches = [match for match in re.finditer(
        pattern=pattern, string=char_str_rev)]
    counter += len(matches)
    return counter


# round#1
score1 = 0
search_string = "XMAS"
# normal forwards and backwards search
for row in layout:
    score1 += count_pattern(char_list=row, search_string=search_string)

# upwards/downwards search (forwards and backwards)
# using the transposed layout
for col in layout_tr:
    score1 += count_pattern(char_list=col, search_string=search_string)


# diagonal search (top-left to bot-right diagonals) - forward and backwards
# diagonal is always from 0,0 to n,n
for i in range(-(layout.shape[0]-1), layout.shape[1]):
    diag_line = np.diag(layout, k=i)
    score1 += count_pattern(char_list=diag_line, search_string=search_string)

# diagonal search2 (bot-left to top-right diagonals) - forward and backwards
# diagonal is always from 0,0 to n,n - so we use the rotated layout
for i in range(-(layout.shape[0]-1), layout.shape[1]):
    diag_line = np.diag(layout_rot, k=i)
    score1 += count_pattern(char_list=diag_line, search_string=search_string)


# round2
score2 = 0

# find all "A"'s and check if the surrounding locations match the characters we want

match_inds = np.where(layout == "A")
match_inds_coords = list(zip(*match_inds))
match_vals = layout[match_inds_coords]


for val1, val2 in match_inds_coords:
    if (val1 > 0 and val1 < layout.shape[0]-1) and (val2 > 0 and val2 < layout.shape[1]-1):
        diag1 = layout[val1-1, val2-1] + "A" + layout[val1+1, val2+1]
        diag2 = layout[val1+1, val2-1] + "A" + layout[val1-1, val2+1]
        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            score2 += 1


# Question 1 - calculate the score of the input
print(f"Q1: The score is {score1}")


# Question 2 - calculate the score of the input permitting the numerals to be written as well
print(f"Q2: The score is {score2}")
