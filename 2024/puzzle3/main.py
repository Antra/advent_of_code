from utils import read_text_file_lines
from pathlib import Path
import re

DIR = Path('2024/puzzle3')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

# sample input
data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
# second sample input
data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

data = read_text_file_lines(file)


# round#1
pattern = r"mul\((\d+),(\d+)\)"
matches = []
for line in data:
    matches.extend(re.findall(pattern, line))


# round2
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"
matches = []
for line in data:
    matches.extend(re.findall(pattern, line))

result = 0
enabled = True

for match in matches:
    if enabled and match[0] != "" and match[1] != "":
        result += int(match[0]) * int(match[1])
    else:
        if match[2] == "do":
            enabled = True
        else:
            enabled = False


# Question 1 - calculate the score of the input
score = sum([(int(a) * int(b)) for a, b in matches])
print(f"Q1: The score is {score}")


# Question 2 - calculate the score of the input permitting the numerals to be written as well
print(f"Q2: The score is {result}")
