file = '2021/puzzle2/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')

# let's store as a vector tupple of (command, length)
content_list = [tuple(value.split(' ')) for value in content_list]


# valid commands are 'forward' (increase horizontal), 'down' (increase depth), 'up' (decrease depth)

horizontal = 0
depth = 0

for vector in content_list:
    command, length = vector
    length = int(length)

    if command == 'forward':
        horizontal += length
    elif command == 'down':
        depth += length
    elif command == 'up':
        depth -= length

print(
    f'The values are, Horizontal: {horizontal}, Depth: {depth}, the product is: {horizontal*depth}')


# Part 2
# it turns out a third parameter also needs to be tracked; 'aim' - 'down' increases aim, 'up' decreases aim, then 'forward' also affects 'depth' by length * (accumulated) aim


horizontal = 0
depth = 0
aim = 0


for vector in content_list:
    command, length = vector
    length = int(length)

    if command == 'forward':
        horizontal += length
        depth += aim * length
    elif command == 'down':
        aim += length
    elif command == 'up':
        aim -= length

print(
    f'The values are, Horizontal: {horizontal}, Depth: {depth}, the product is: {horizontal*depth}')
