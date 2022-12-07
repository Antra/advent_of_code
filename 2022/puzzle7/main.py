from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle7')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


def _update_path(path, current_path):
    if path[-2:] == '..':
        current_path.pop()
        return current_path
    else:
        path = path.split(' ')[-1]
        return current_path + [path]


def parser(data):
    # what should we do?
    # we're basically exploring, so figure out which are moves (cd) and which are looking (ls) and which are results
    # map out the "rooms" and store the content results
    filesystem = {}
    current_path = []
    for entry in data:
        if entry[0:4] == '$ cd':
            current_path = _update_path(path=entry, current_path=current_path)
            name = entry.split(' ')[-1]
            path = '/'.join(current_path).replace('//', '/')
            filesystem[path] = filesystem.get(path, {})
        elif entry[0:4] == '$ ls':
            # we're listing current_path
            pass
        elif entry[0:3] == 'dir':
            # we are seeing a subdirectory, for now do nothing
            pass
        else:
            # we're seeing a file in current_path
            path = '/'.join(current_path).replace('//', '/')
            size, name = entry.split(' ')
            filesystem[path][name] = int(size)
            # lets update the folder sizes accordingly
            filesystem[path]['folder_size'] = filesystem[path].get(
                'folder_size', 0) + int(size)
            for i, parent in enumerate(current_path):
                # if parent == '/':
                #    filesystem['/']['total_size'] = filesystem['/'].get('total_size', 0) + int(size)
                # else:
                #    abs_path = '/'.join(current_path[:i+1]).replace('//', '/')
                abs_path = '/'.join(current_path[:i+1]).replace('//', '/')
                filesystem[abs_path]['total_size'] = filesystem[abs_path].get(
                    'total_size', 0) + int(size)

    return filesystem


filesystem = parser(data)

folders_exceeding = [k for k in filesystem.keys(
) if filesystem[k].get('total_size') <= 100000]

scores1 = sum([filesystem.get(folder).get('total_size')
              for folder in folders_exceeding])


# Question 1 - How many folders do not exceed 100000 ?
print(
    f"Q1: How many folders do not exceed 100000?  {len(scores1)}")

total_size = 70000000
update_size = 30000000
free_space = total_size - filesystem['/'].get('total_size')
minimum = update_size - free_space

folders_exceeding = [k for k in filesystem.keys(
) if filesystem[k].get('total_size') > minimum]

scores2 = min([filesystem.get(folder).get('total_size')
              for folder in folders_exceeding])


# Question 2 - What is the size of the smallest folder that is big enough?
print(
    f"Q2: What is the size of the smallest folder that is big enough?  {scores2}")
