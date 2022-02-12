from utils import get_data
from collections import Counter
file = '2021/puzzle14/input.txt'
data = get_data(file)

# sample data
# data = ['NNCB',
#         '',
#         'CH -> B',
#         'HH -> N',
#         'CB -> H',
#         'NH -> C',
#         'HB -> C',
#         'HC -> B',
#         'HN -> C',
#         'NN -> C',
#         'BH -> H',
#         'NC -> B',
#         'NB -> B',
#         'BN -> B',
#         'BB -> N',
#         'BC -> B',
#         'CC -> N',
#         'CN -> C']

template = [item for item in data if '->' not in item and item != ''][0]
# data = [item for item in data if '->' in item and item != '']
rules = {item.split(' -> ')[0]: item.split(' -> ')[1]
         for item in data if '->' in item and item != ''}


def grow(polymer, rules, n=0):
    print(f'Start growing, n-value: {n}')
    new_polymer = []
    for index, char in enumerate(polymer):
        if index != len(polymer)-1:

            first, second = char, polymer[index+1]
            string = first + rules[first+second]
            new_polymer.append(string)
            # print(f'String: {first+second} matches replacement rule: {rules[first+second]} and becomes: {new_polymer} (and {second} carries over) in next step')
        else:
            # print(f'last step, so just appending {char}')
            new_polymer.append(char)
    new_polymer = ''.join(new_polymer)
    if n:
        return grow(new_polymer, rules, n-1)
    else:
        return new_polymer


# n is number of growing steps to apply beyond the initial
# part1
polymer = grow(template, rules, n=9)
# part2 -- cannot be done in the same way, that'll take days to calculate!
# polymer = grow(template, rules, n=39)


# print(polymer)
print(len(polymer))

# most/least common elements
most_common = max(set(polymer), key=polymer.count)
most_common_freq = polymer.count(most_common)
least_common = min(set(polymer), key=polymer.count)
least_common_freq = polymer.count(least_common)

print(f'Most common element is {most_common} ({most_common_freq}) and least common element is {least_common} ({least_common_freq}, the difference is: {most_common_freq - least_common_freq})')


# part2 -- more efficient method: https://dev.to/qviper/advent-of-code-2021-python-solution-day-14-4395
current = Counter(a+b for a, b in zip(template, template[1:]))
chars = Counter(template)
for _ in range(40):
    tmp = Counter()
    for (c1, c2), value in current.items():
        mc = rules[c1+c2]
        tmp[c1+mc] += value
        tmp[mc+c2] += value
        chars[mc] += value
    current = tmp
max(chars.values()) - min(chars.values())
