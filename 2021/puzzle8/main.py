file = '2021/puzzle8/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')
# numbers = [int(number) for number in content.split(',')]

input_dict = {
    'acedgfb': '8',
    'cdfbe': '5',
    'gcdfa': '2',
    'fbcad': '3',
    'dab': '7',
    'cefabd': '9',
    'cdfgeb': '6',
    'eafb': '4',
    'cagedb': '0',
    'ab': '1'
}

pattern_dict = {''.join(sorted(k)): v for k, v in input_dict.items()}

output_list = [content.split('|')[1].strip().split(' ')
               for content in content_list]
hits = [1 if len(output_item) in [2, 3, 4, 7]
        else 0 for output in output_list for output_item in output]


print(f'Answer to part#1 is: {sum(hits)}')

# Part 2 - we have to decode each line separately using both input and output to figure it out
# if length of any signal is in 2 (1), 3 (7), 4 (4), 7 (8) we know immediately what it is
# afterwards we have to compare the segments used for the other lengths 5 (2, 3, 5) and 6 (0, 6, 9) and see how many they would share with the other digits


def _length_to_digit(length):
    """a little helper function just to map the length to the digit for the unique signals

    Input:
    :length(int): length of a signal string

    Returns:
    :digit(int): the corresponding digit or False if no digit corresponds to that length
    """
    # a {length: digit} dictionary
    length_dict = {2: 1,
                   4: 4,
                   3: 7,
                   7: 8}
    return length_dict.get(length, False)


def decode_signals(signal_list):
    # find the known signals with unique lengths - those correspond to 1, 4, 7, 8
    unique_signals = [signal for signal in signal_list if len(signal) in [
        2, 3, 4, 7]]

    # map the known uniques via their length to corresponding digits
    signal_mapping = {_length_to_digit(
        len(signal)): set(signal) for signal in unique_signals}

    one = signal_mapping.get(1, False)
    four = signal_mapping.get(4, False)
    seven = signal_mapping.get(7, False)
    eight = signal_mapping.get(8, False)

    # These are the unknowns
    length5_signals = [set(signal)
                       for signal in signal_list if len(signal) == 5]
    length6_signals = [set(signal)
                       for signal in signal_list if len(signal) == 6]

    # Start with length5
    # if we have 1,4,7 we can decode all the length5 signals (2, 3, 5)
    for signal in length5_signals:
        # 3 is easiest to find; it has a diff 3 against 1
        if one and len(signal - one) == 3:
            # this is a 3!
            signal_mapping[3] = signal

        if four and seven and len(signal-seven) == 3:
            # this is a 2 or a 5 - we just need the diff against 4 to tell us
            difference = len(signal-four)
            if difference == 3:
                # this is a 2!
                signal_mapping[2] = signal
            elif difference == 2:
                # this is a 5!
                signal_mapping[5] = signal

    # And proceed with length6
    # again if we have 1, 4, and 7 we can decode all the length6 signals (0, 6, 9)
    for signal in length6_signals:
        # 9 is easiest to find; it has a diff 2 against 4:
        if (four and len(signal - four) == 2):
            # this is a 9!
            signal_mapping[9] = signal

        # 6 is easy to find; it has a diff 5 again 1 and a diff 4 against 7:
        if (one and len(signal - one) == 5) or (seven and len(signal - seven) == 4):
            # this is a 6!
            signal_mapping[6] = signal

        # 0 has a diff 3 against 4 and 7 and a diff 4 against 1:
        if (four or seven) and one and len(signal - one) == 4:
            difference = len(signal - four) if four else len(signal - seven)
            if difference == 3:
                # this is a 0!
                signal_mapping[0] = signal

    # and lastly reverse the dictionary so it can be used to translate (NB, key strings are sorted!)
    signal_to_digit = {''.join(sorted(v)): k for k,
                       v in signal_mapping.items()}

    if len(signal_to_digit.keys()) != 10:
        print(
            f'There should be 10 keys in the translation dictionary, but we have {len(signal_to_digit.keys())} for signal_list: {signal_list}')
    return signal_to_digit


# we have to translate all the 4-digit values and add them up
codes = []


for entry in content_list:
    signal_list, digits = entry.split(' | ')
    signal_list = signal_list.split(' ')
    digits = [''.join(sorted(digit)) for digit in digits.split(' ')]
    signal_to_digit = decode_signals(signal_list=signal_list)
    translated_digits = int(
        ''.join([str(signal_to_digit[digit]) for digit in digits]))
    codes.append(translated_digits)


print(f'The sum of the translated 4-digit codes are: {sum(codes)}')
