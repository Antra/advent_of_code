from utils import read_text_file_lines
from pathlib import Path


DIR = Path('2023/puzzle2')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


max_dict = {'red': 12,
            'green': 13,
            'blue': 14}


def calc_score(games, power=False):
    valid_games = []
    min_powers = []
    for game in games:
        min_dict = {'red': 0,
                    'green': 0,
                    'blue': 0}
        valid_game = True
        split_string = game.replace('Game ', '').split(': ')
        game_id = int(split_string[0])
        subgames = split_string[1]
        reveals = subgames.split('; ')
        for reveal in reveals:
            subreveals = reveal.split(', ')
            for subreveal in subreveals:
                count, colour = subreveal.split(' ')
                if max_dict.get(colour) < int(count):
                    valid_game = False
                min_dict[colour] = max(int(count), min_dict.get(colour))

        if valid_game:
            valid_games.append(game_id)

        game_power = min_dict.get(
            'red', 0) * min_dict.get('green', 0) * min_dict.get('blue', 0)
        min_powers.append(game_power)

    if not power:
        return sum(valid_games)
    else:
        return sum(min_powers)


# Question 1 - calculate the score of the input
print(f"Q1: The score is {calc_score(data)}")


# Question 2 - calculate the score of the input using the Power variant
print(f"Q2: The score is {calc_score(data, power=True)}")
