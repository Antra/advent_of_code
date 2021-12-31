file = '2021/puzzle10/input.txt'

with open(file, 'r') as f:
    content = f.read()

content_list = content.split('\n')

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

opposite = {
    '<': '>',
    '(': ')',
    '[': ']',
    '{': '}'
}

repair_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# content_list = ['[({(<(())[]>[[{[]{<()<>>',
#                 '[(()[<>])]({[<{<<[]>>(',
#                 '{([(<{}[<>[]}>{[]{[(<()>',
#                 '(((({<>}<{<{<>}{[]{[]{}',
#                 '[[<[([]))<([[{}[[()]]]',
#                 '[{[{({}]{}}([{[{{{}}([]',
#                 '{<[[]]>}<{[{[{[]{()[[[]',
#                 '[<(<(<(<{}))><([]([]()',
#                 '<{([([[(<>()){}]>(<<{{',
#                 '<{([{{}}[<[[[<>{}]]]>[]]']


all_bad_chars = []

repair_lines = []
p2_scores = []

for charstring in content_list:
    stack = []
    bad_chars = []
    for char in charstring:
        if len(stack) > 0 and stack[-1] == char:
            # is it the opposing character? Then pop it from the stack
            _ = stack.pop()
        elif char in opposite.keys():
            # is it an opening character? Then add it to the stack
            op_char = opposite[char]
            stack.append(op_char)
        elif char in opposite.values():
            # that is a bad move; we have an incorrectly formatted string!
            bad_chars.append(char)
            # we should break here, but let's catch all
            # break
    if bad_chars:
        # was this a broken line?
        all_bad_chars.append(bad_chars)
    else:
        # otherwise we keep it
        repair_lines.append(charstring)
        # and find the repair string; it's the reverse of our stack
        repair_string = list(reversed(stack))
        score = 0
        for rep_char in repair_string:
            score *= 5
            score += repair_score[rep_char]
        p2_scores.append(score)

score = sum([scoring[char]
            for bad_chars in all_bad_chars for char in bad_chars])

print(f'Scoring: {score}')

# Part 2 - discard the corrupt lines and repair the rest
# the winning p2 score is the middle repair score; so sort them and find the middle position
p2_scores.sort()
p2_score_pos = len(p2_scores) // 2
score = p2_scores[p2_score_pos]

print(f'P2 scoring: {score}')
