from utils import read_text_file_lines
from pathlib import Path


DIR = Path('2023/puzzle4')

# file = DIR / 'sample1.txt'
file = DIR / 'input.txt'

data = read_text_file_lines(file)


win_points = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


def game(gamestring):
    # split the numbers, get rid of the double-spaces for single-digit numbers
    winners, numbers = gamestring.replace('  ', ' ').split(' | ')
    winners = winners.split(' ')
    numbers = numbers.split(' ')
    winning_numbers = sum(x in winners for x in numbers)
    score = win_points[winning_numbers]
    return score


# Question 1 - calculate the score of all the scratchcards
total_score = 0
for item in data:
    card_num, gamestring = item.replace('Card ', '').split(': ')
    total_score += game(gamestring=gamestring)
print(f"Q1: The score is {total_score}")


# Question 2 - calculate the total number of scratchcards using the new rule
game_cards = {}
# prep and store the cards so we can retrieve them
for item in data:
    card_num, gamestring = item.replace('Card ', '').split(': ')
    card_num = card_num.replace(' ', '')
    game_cards[card_num] = gamestring


def game2(card_num, gamestring):
    # determine the score from this card
    winners, numbers = gamestring.replace('  ', ' ').split(' | ')
    winners = winners.split(' ')
    numbers = numbers.split(' ')
    score = sum(x in winners for x in numbers)

    # determine the new cards we won
    new_cards = []
    for item in range(int(card_num)+1, int(card_num)+score+1):
        tup = (str(item), game_cards.get(str(item)))
        new_cards.append(tup)
    return new_cards


all_cards = []
new_cards = list(game_cards.items())

# we can modify the list while looping and keep us running -- this will take a couple of minutes though :)
for entry in new_cards:
    card_num = entry[0]
    gamestring = entry[1]
    all_cards.append(card_num)
    winnings = game2(card_num=card_num, gamestring=gamestring)
    # new_cards = new_cards + winnings
    _ = [new_cards.append(item) for item in winnings]


print(f"Q2: The score is {len(all_cards)}")
