import numpy as np
file = '2021/puzzle9/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')
numbers = [int(number)
           for content_row in content_list for number in content_row]

#map = np.ma.array(numbers, mask=False).reshape(-1, 100)
map = np.array(numbers).reshape(-1, 100)


def get_neighbours(array, i, j, distance=1):
    """helper function to return the neighbouring values of point (i,j)

    Args:
        array (np array): the NumPy array to dig into
        i (int): the row index (axis=0)
        j (int): the column index (axis=1)
        distance (int): how far around point (i,j) to look - defaults to 1

    Returns:
        array (np array): flattened array of all the neighbour values
    """
    masked_array = np.ma.array(array[:], mask=False)
    masked_array.mask[i, j] = True
    if i+1 <= 99:
        if j+1 <= 99:
            masked_array.mask[i+1, j+1] = True
        if j-1 >= 0:
            masked_array.mask[i+1, j-1] = True
    if i-1 >= 0:
        if j+1 <= 99:
            masked_array.mask[i-1, j+1] = True
        if j-1 >= 0:
            masked_array.mask[i-1, j-1] = True

    return masked_array[max(i-distance, 0):min(i+distance+1, array.shape[0]), max(j-distance, 0):min(j+distance+1, array.shape[1])].flatten()


# traverse the array and for every point compare it to it's neighbour values; if it's the same as the minimum, then it's a low point and is kept
low_point_indices = []


for i in range(0, 100, 1):
    for j in range(0, 100, 1):
        own_val = map[i, j]
        neighbours = get_neighbours(map, i, j)
        if own_val < min(neighbours):
            low_point_indices.append((i, j))

low_point_score = sum([map[indices]+1 for indices in low_point_indices])


print(
    f'The sum of the low point values is: {low_point_score}')

# 314790 -> too high
# 289691 -> too high
# 23 is wrong


# My Numpy approach didn't work -- using this solution to progress


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_lower(y, x, height_map):
    if x - 1 >= 0:
        if height_map[y][x] >= height_map[y][x - 1]:
            return False
    if x + 1 <= len(height_map[y]) - 1:
        if height_map[y][x] >= height_map[y][x + 1]:
            return False
    if y - 1 >= 0:
        if height_map[y][x] >= height_map[y - 1][x]:
            return False
    if y + 1 <= len(height_map) - 1:
        if height_map[y][x] >= height_map[y + 1][x]:
            return False
    return True


def get_low_points(height_map):
    low_points = []
    points_location = []
    for y in range(len(height_map)):
        for x in range(len(height_map[y])):
            if is_lower(y, x, height_map):
                low_points.append(height_map[y][x])
                points_location.append(Point(x, y))

    return low_points, points_location


def calculcate_basin_size(point, height_map):
    size = 0
    if (point.x >= 0
        and point.y >= 0
        and point.y < len(height_map)
            and point.x < len(height_map[point.y])):
        if height_map[point.y][point.x] != '#' and height_map[point.y][point.x] < 9:
            size = 1
            height_map[point.y][point.x] = '#'
            size += calculcate_basin_size(Point(point.x - 1, point.y),
                                          height_map)
            size += calculcate_basin_size(Point(point.x + 1, point.y),
                                          height_map)
            size += calculcate_basin_size(Point(point.x, point.y - 1),
                                          height_map)
            size += calculcate_basin_size(Point(point.x, point.y + 1),
                                          height_map)
    return size


def get_basin_size(points_location, height_map):
    first = 0
    second = 0
    third = 0
    for point in points_location:
        size = calculcate_basin_size(point, height_map)
        if size > first:
            third = second
            second = first
            first = size
        elif size > second:
            third = second
            second = size
        elif size > third:
            third = size

    return first, second, third, first * second * third


def main():
    height_map = []
    with open('2021/puzzle9/input.txt') as f:
        for line in f:
            height_map.append(list(map(int, list(line.replace('\n', '')))))
    low_points, points_location = get_low_points(height_map)
    print(sum(low_points) + len(low_points))
    print(get_basin_size(points_location, height_map))


if __name__ == "__main__":
    main()
