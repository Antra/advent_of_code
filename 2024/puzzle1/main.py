from utils import read_text_file_lines
from pathlib import Path
import re

DIR = Path('2024/puzzle1')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


def split_to_lists(big_list):
    list_a, list_b = [], []
    for item in big_list:
        a, b = re.sub('\s+', ' ', item).split(' ')
        list_a.append(int(a))
        list_b.append(int(b))
    return list_a, list_b


list_a, list_b = split_to_lists(data)

sorted_list_a = sorted(list_a)
sorted_list_b = sorted(list_b)


def score1(a, b):
    sum = 0
    for item in zip(a, b):
        sum += abs(item[0] - item[1])
    return sum


def score2(a, b):
    sum = 0
    for item in a:
        presence = b.count(item)
        sum += presence * item

    return sum


# Question 1 - calculate the score of the input
score = score1(sorted_list_a, sorted_list_b)
print(f"Q1: The score is {score}")


# Question 2 - calculate the score of the input permitting the numerals to be written as well
score = score2(list_a, list_b)
print(f"Q2: The score is {score}")
