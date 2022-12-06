from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle6')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


def process_signal(datastream, length_to_find):
    i = length_to_find
    while i < len(datastream):
        check_vector = datastream[i-length_to_find: i]
        if len(set(check_vector)) == len(check_vector):
            return i
        else:
            i += 1


data = data[0]

scores1 = process_signal(data, 4)


# Question 1 - How many characters need to be processed before the first start-of-packet marker is detected?
print(
    f"Q1: Start of marker after {scores1} characters")

scores2 = process_signal(data, 14)


# Question 2 - How many characters if start-of-message marker is 14?
print(
    f"Q2: Start of marker after {scores2} characters")
