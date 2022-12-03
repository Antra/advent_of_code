from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle3')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)

PRIORITY = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def split_rucksack(contents):
    """Splits the contents of a rucksack into its two compartments

    Args:
        contents (str): the string of its contents

    Returns:
        part1: the contents of the first compartment
        part2: the contents of the second compartment
        overlap: the overlapping item which appears in both compartments
        priority: priority of the overlapping item
    """
    size = int(len(contents)/2)
    part1 = contents[:size]
    part2 = contents[size:]

    overlap = list(set(part1).intersection(part2))[0]
    priority = PRIORITY.index(overlap)

    return part1, part2, overlap, priority


scores1 = [split_rucksack(contents)[3] for contents in data]


# Question 1 - what is the sum of priorities of the overlapping items?
print(
    f"Q1: What is the sum of priorities of the overlapping items: {sum(scores1)}")


def identify_badges(sack1, sack2, sack3):
    """Identifies the badge and priority for 3 rucksacks

    Args:
        sack1 (str): the content string of the first rucksack
        sack2 (str): the content string of the second rucksack
        sack3 (str): the content string of the third rucksack

    Returns:
        str: the identity badge of the group
        int: the priority score of that badge
    """
    overlap = list(set(sack1).intersection(
        set(sack2)).intersection(set(sack3)))[0]
    priority = PRIORITY.index(overlap)

    return overlap, priority


scores2 = []

for i in range(0, len(data), 3):
    sack1 = data[i]
    sack2 = data[i+1]
    sack3 = data[i+2]
    score = identify_badges(sack1, sack2, sack3)[1]
    scores2.append(score)


# Question 2 - what is the sum of the priority scores of the identification badges?
print(
    f"Q2: What is the sum of the priority scores of the identification badges: {sum(scores2)}")
