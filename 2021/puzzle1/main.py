file = 'input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')

content_list = [int(value) for value in content_list]

# First assignment is to find the number of increases in the dataset

previous_value = content_list[0]
increases = 0
decreases = 0
unchanged = 0

for val in content_list:
    if val > previous_value:
        increases += 1
    elif val < previous_value:
        decreases += 1
    elif val == previous_value:
        unchanged += 1
    previous_value = val


print(f'There are {increases} number of increases in this dataset')


# Second assignment is to compare three-measurement windows and see whether they increase or not.
old_window = []
new_window = []

increases = 0
decreases = 0
unchanged = 0


for value in content_list:
    if len(new_window) == 3:
        old_window = new_window[:]
        _ = new_window.pop(0)
    new_window.append(value)
    if sum(old_window) == 0:
        continue
    if sum(new_window) > sum(old_window):
        increases += 1
    elif sum(new_window) < sum(old_window):
        decreases += 1
    elif sum(new_window) == sum(old_window):
        unchanged += 1


print(f'There are {increases} number of increases in this dataset')


# Pandas approach
# import pandas as pd
#day1 = pd.read_csv(day1.txt, header=None)
#print((day1.rolling(3).sum().diff() > 0).sum())
