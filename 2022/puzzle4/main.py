from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle4')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)

fully_enclosed_counter = 0


def fully_enclosed(sections):
    sec1, sec2 = sections.split(',')
    sec1_start, sec1_end = sec1.split('-')
    sec2_start, sec2_end = sec2.split('-')
    sec1_start, sec1_end = int(sec1_start), int(sec1_end)
    sec2_start, sec2_end = int(sec2_start), int(sec2_end)
    sec1_len = sec1_end - sec1_start
    sec2_len = sec2_end - sec2_start

    # is sec2 fully within sec1?
    sector = list('.' * 100)
    sector[sec1_start:sec1_end+1] = ['x' for _ in range(sec1_end-sec1_start+1)]
    sec2_enclosed = all(
        [True if sec == 'x' else False for sec in sector[sec2_start:sec2_end+1]])

    # is sec1 fully within sec2?
    sector = list('.' * 100)
    sector[sec2_start:sec2_end+1] = ['x' for _ in range(sec2_end-sec2_start+1)]
    sec1_enclosed = all(
        [True if sec == 'x' else False for sec in sector[sec1_start:sec1_end+1]])

    if sec1_enclosed or sec2_enclosed:
        return 1
    else:
        return 0


def overlapping(sections):
    sec1, sec2 = sections.split(',')
    sec1_start, sec1_end = sec1.split('-')
    sec2_start, sec2_end = sec2.split('-')
    sec1_start, sec1_end = int(sec1_start), int(sec1_end)
    sec2_start, sec2_end = int(sec2_start), int(sec2_end)
    sec1_len = sec1_end - sec1_start
    sec2_len = sec2_end - sec2_start

    # is there any overlap?
    sector = list('.' * 100)
    sector[sec1_start:sec1_end+1] = ['x' for _ in range(sec1_end-sec1_start+1)]

    overlaps = any(
        [True if sec == 'x' else False for sec in sector[sec2_start:sec2_end+1]])

    if overlaps:
        return 1
    else:
        return 0


scores1 = [fully_enclosed(entry) for entry in data]


# Question 1 - how many assignment pairs does one range fully contain the other?
print(
    f"Q1: There are: {sum(scores1)} fully enclosed assignment pairs")


scores2 = [overlapping(entry) for entry in data]


# Question 2 - how many assignment pairs do the ranges overlap
print(
    f"Q2: how many assignment pairs do the ranges overlap? {sum(scores2)}")
