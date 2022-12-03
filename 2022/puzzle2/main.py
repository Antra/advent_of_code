from utils import read_text_file_lines
from pathlib import Path

DIR = Path('2022/puzzle2')

#file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


scores = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
    'X': 1,  # Rock / lose
    'Y': 2,  # Paper / draw
    'Z': 3,   # Scissors / win
    'loss': 0,
    'draw': 3,
    'win': 6
}

# resolver written from "my" perspective
resolver = {'AX': 'draw',
            'AY': 'win',
            'AZ': 'loss',
            'BX': 'loss',
            'BY': 'draw',
            'BZ': 'win',
            'CX': 'win',
            'CY': 'loss',
            'CZ': 'draw'}

# this is for part two where the second column changes meaning - what should my move be?
counter_moves = {'A X': 'A Z',
                 'A Y': 'A X',
                 'A Z': 'A Y',
                 'B X': 'B X',
                 'B Y': 'B Y',
                 'B Z': 'B Z',
                 'C X': 'C Y',
                 'C Y': 'C Z',
                 'C Z': 'C X'}


def resolve_game(game, round2=False):
    """resolves the game, and returns my score

    Args:
        opponent (str): the move the opponent plays
        my (str): the move I play according to the guide
    """
    if round2:
        game = counter_moves.get(game)
    opponent, my = game.split(' ')
    move_score = scores.get(my)
    game_combo = opponent+my
    game_score = scores.get(resolver.get(game_combo))
    return move_score+game_score


scores1 = [resolve_game(game) for game in data]


# Question 1 - what would be your total score if everything goes exactly according to your strategy guide?
print(
    f"Q1: following the strategy guide gives the following score: {sum(scores1)}")

scores2 = [resolve_game(game, round2=True) for game in data]


# Question 2 - how many calories are the top 3 carriers carrying?
print(
    f"Q2: Using the strategy guide correctly gives the following scores: {sum(scores2)}")
