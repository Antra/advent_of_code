from utils import read_text_file_lines
from pathlib import Path


DIR = Path('2023/puzzle5')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)

# create the mapping rules
seeds = [int(num) for num in data.pop(0).split(': ')[1].split(' ')]


def map_function(input):
    value = input
    for map in maps:
        value = next((destination_range.start + (value - source_range.start)
                     for source_range, destination_range in map.items() if value in source_range), value)

    return value


def reverse_map_function(location):
    value = location
    for current_map in reversed(maps):
        value = next(
            (source_range.start + (value - destination_range.start) for source_range, destination_range in current_map.items() if value in destination_range), value)
    return value


# build the maps
maps = []
# build the maps
for item in data:
    if "map" in item:
        maps.append(dict())
    elif item != '':
        dest, src, length = [int(num) for num in item.split(' ')]
        maps[-1][range(src, src+length)] = range(dest, dest+length)


locations = [map_function(seed) for seed in seeds]


# Question 1 - calculate the lowest location ID
print(f"Q1: The lowest location is {min(locations)}")


# fix the new seed ranges instead
seed_ranges = []
for index in range(0, len(seeds) - 1, 2):
    start, length = seeds[index:index+2]
    seed_ranges.append(range(start, start+length))


# brute-forcing Question 2 -- this will take a while. :)
location = 0
while True:
    potential_seed = reverse_map_function(location)
    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(f"Q2: The lowest location is {location}")
        break

    location += 1
