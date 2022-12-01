from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle1')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


def splitter(sequence, sep=''):
    """split sequence into sub-sequences on a separator

    Args:
        sequence (list): the sequence to split apart
        sep (str, optional): the separator sequence. Defaults to ''.

    Yields:
        subsequence (list of int): yields a subsequence as int from the original sequence
    """
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(int(val))
    yield chunk


#inventories = {i: item for i, item in enumerate(splitter(data))}
inventory_counts = [sum(entry) for entry in splitter(data)]
inventory_counts.sort(reverse=True)

# Question 1 - how many calories is the Elf carrying the most carrying?
print(f"Q1: The elf carrying the most is carrying: {max(inventory_counts)}")


# Question 2 - how many calories are the top 3 carriers carrying?
print(f"Q2: The top3 carrying elfs are carrying: {sum(inventory_counts[:3])}")