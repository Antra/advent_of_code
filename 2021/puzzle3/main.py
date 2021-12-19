file = '2021/puzzle3/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')


# Need to use binary input to get 'gamma rate' and 'epsilon rate'
# power consumption is gamma * epsilon

# gamma rate is found by finding the most common bit value for each bit position
# epsilon rate is found by finding the least common bit value for each position - i.e. the inverted gamma value

# Let's build a list of dicts, so we can keep track and get the counts for each position
gamma_bits = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

for value in content_list:
    for bit_index, bit_value in enumerate(value):
        gamma_bits[bit_index][bit_value] = gamma_bits[bit_index].get(
            bit_value, 0) + 1


# construct gamma value
gamma_list = ['1' if freq_dict.get('0', 0) < freq_dict.get(
    '1', 0) else '0' for freq_dict in gamma_bits]
gamma_string = ''.join(gamma_list)
# and then invert it for the epsilon value
epsilon_string = ''.join('1' if bit == '0' else '0' for bit in gamma_string)


# convert binary to integer
gamma_value = int(gamma_string, 2)
epsilon_value = int(epsilon_string, 2)

print(f'Gamma value: {gamma_value} ({gamma_string}), Epsilon value: {epsilon_value} ({epsilon_string}) - the product is: {gamma_value*epsilon_value}')


# Part 2
def get_value(values, bit_position=0, most_common=True):
    """Sift through a list of values, examine a certain position and get the values that fit the pattern

    Args:
        values ([list]): list of values to examine
        bit_position (int): which bit position should be examined
        most_common (bool, optional): should we search for most common occurrence? If not, then least common occurrence. Defaults to True.

    Returns:
        single value fitting the criteria of being constructed from the most/least consisting bit values
    """

    if len(values) == 1:
        # base case, we have only one value left, so return that
        return int(values[0], 2)
    elif bit_position > 12:
        # we seem to have an error, if we get to a higher bit position than the length is!
        print('Error!')
        return -1
    else:
        # otherwise filter down the list and make recursive call
        # first create a frequency dictionary for this position
        frequency_dict = {}
        for value in values:
            bit = value[bit_position]
            frequency_dict[bit] = frequency_dict.get(bit, 0) + 1
        if most_common:
            # keep 1 if same number
            bit_value = '0' if frequency_dict.get(
                '0', 0) > frequency_dict.get('1', 0) else '1'
        else:
            # keep 0 if same number
            bit_value = '1' if frequency_dict.get(
                '0', 0) > frequency_dict.get('1', 0) else '0'
        new_values = [
            value for value in values if value[bit_position] == bit_value]

        return get_value(values=new_values, bit_position=bit_position+1, most_common=most_common)


O2 = get_value(values=content_list)
CO2 = get_value(values=content_list, most_common=False)

print(f'O2: {O2}, CO2: {CO2}, Product: {O2*CO2}')
