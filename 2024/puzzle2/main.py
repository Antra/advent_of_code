from utils import read_text_file_lines
from pathlib import Path
import re

DIR = Path('2024/puzzle2')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


def safety_check(series, safety_threshold=-1):
    level = [int(x) for x in series.split(' ')]

    safety_check = []

    # two rules, all numbers are either increasing or decreasing
    # the difference is at least 1 and at most 3

    if level[0] < level[1]:
        increasing = True
    else:
        increasing = False

    unsafety_count = 0
    for i in range(1, len(level)):
        if (not increasing & (level[i] < level[i-1])) | (increasing & (level[i] > level[i-1])):
            if (abs(level[i] - level[i-1]) >= 1) & (abs(level[i] - level[i-1]) <= 3):
                safety_check.append(True)
            elif (i+1 < len(level)) & (((abs(level[i] - level[i-1]) >= 1) & (abs(level[i] - level[i-1]) <= 3)) | (unsafety_count < safety_threshold)):
                unsafety_count += 1
                if (((abs(level[i+1] - level[i-1]) >= 1) & (abs(level[i+1] - level[i-1]) <= 3)) | (unsafety_count < safety_threshold)):
                    safety_check.append(True)
                else:
                    safety_check.append(False)
            else:
                safety_check.append(False)
        elif i+1 < len(level) & ((((not increasing & (level[i] < level[i-1])) | (increasing & (level[i] > level[i-1]))) | (unsafety_count < safety_threshold))):
            unsafety_count += 1
            if ((not increasing & (level[i+1] < level[i-1])) | (increasing & (level[i+1] > level[i-1]))):
                safety_check.append(True)
            else:
                safety_check.append(False)
        else:
            safety_check.append(False)

    return all(safety_check)


# round#1
safety_checks = []
for level in data:
    safety_checks.append(safety_check(level))

# round2
safety_checks_v2 = []
for level in data:
    safety_checks_v2.append(safety_check(level, safety_threshold=1))


# Question 1 - calculate the score of the input
score = sum(safety_checks)
print(f"Q1: The score is {score}")


# Question 2 - calculate the score of the input permitting the numerals to be written as well
score = sum(safety_checks_v2)
print(f"Q2: The score is {score}")
