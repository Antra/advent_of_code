from utils import read_text_file_lines
from pathlib import Path
import re

DIR = Path('2023/puzzle1')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def find_num(string, pattern, reverse=False):
    """find the numeral in the substring using regex

    Args:
        string (str): the string to search for a numeric character
        pattern (str): the regex string to search for
        reverse (bool): return the first or the last match
    """
    hits = pattern.findall(string)
    if reverse:
        return hits[-1]
    else:
        return hits[0]


def calc_score(string, wordify=False):
    """calculate the score sum of the strings

    Args:
        string (string): the string to search for the numerals
    """
    if wordify:
        # find either a digit or one of the written numericals
        pattern = re.compile(r"(?=(\d|" + "|".join(digits.keys()) + r"))")
    else:
        # find only a digit
        pattern = re.compile(r"(?=(\d))")

    val1 = str(find_num(string, pattern, reverse=False))
    val2 = str(find_num(string, pattern, reverse=True))

    val1 = str(digits.get(val1, val1))
    val2 = str(digits.get(val2, val2))

    return int(val1+val2)


# Question 1 - calculate the score of the input
score = sum([calc_score(substring) for substring in data])
print(f"Q1: The score is {score}")


# Question 2 - calculate the score of the input permitting the numerals to be written as well
score = sum([calc_score(substring, wordify=True) for substring in data])
print(f"Q2: The score is {score}")
