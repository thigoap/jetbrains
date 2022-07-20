# Rock, Paper, Scissors - Stage 05
# https://hyperskill.org/projects/78/stages/435/implement

'''
Description
How about new game rules? The original game has a fairly small choice of options.

The extended version of the game makes it hard to draw. Now, your program should accept alternative lists of options, like Rock, Paper, Scissors, Lizard, Spock, and so on. You can take the following options (don't take their relations into account; we'll speak about them further on):
In this stage, before the game starts, users can choose the options. After entering the name, they should provide a list of the options separated by a comma. For example:
rock,paper,scissors,lizard,spock
If users input an empty line, start the game with default options: rock, paper, and scissors.
Once the game options are defined, output Okay, let's start.

Objectives
Your program should:

Output a line Enter your name: . Users enter their names on the same line (not the one following the output);
Read the input with the username and output Hello, <name>;
Read rating.txt and check whether it contains an entry with the current username. If yes, use the score specified in the file as a starting point. If not, start the score from 0;
Read the input with the list of options for the game (options are separated by comma). If the input is an empty line, play with the default options;
Output a line Okay, let's start;
Play the game by the rules defined in the previous stages and read the user's input;
If the input is !exit, output Bye! and stop the game;
If the input is the name of the option, then pick a random option and output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Loss: Sorry, but the computer chose <option>
Draw: There is a draw (<option>)
Win: Well done. The computer chose <option> and failed
For each draw, add 50 points to the score. For each user's win, add 100 to their score. In case of a loss, don't change the score;
If input corresponds to anything else, output Invalid input;
Restart the game (with the same options defined before the start of the game).
'''

print('Rock, Paper, Scissors - Stage 05\n')

from random import choice

def determine_winner(user, computer):
    # win_dict[key] wins against key
    win_dict = {
        "rock": ["lightning", "gun", "air", "water", "dragon", "paper", "devil"],
        "gun": ["lightning", "sponge", "air", "water", "dragon", "paper", "devil"],
        "lightning": ["wolf", "sponge", "air", "water", "dragon", "paper", "devil"],
        "devil": ["wolf", "sponge", "air", "water", "dragon", "paper", "tree"],
        "dragon": ["wolf", "sponge", "air", "water", "human", "paper", "tree"],
        "water": ["wolf", "sponge", "air", "snake", "human", "paper", "tree"],
        "air": ["wolf", "sponge", "scissors", "snake", "human", "paper", "tree"],
        "paper": ["wolf", "sponge", "scissors", "snake", "human", "fire", "tree"],
        "sponge": ["wolf", "rock", "scissors", "snake", "human", "fire", "tree"],
        "wolf": ["gun", "rock", "scissors", "snake", "human", "fire", "tree"],
        "tree": ["gun", "rock", "scissors", "snake", "human", "fire", "lightning"],
        "human": ["gun", "rock", "scissors", "snake", "devil", "fire", "lightning"],
        "snake": ["gun", "rock", "scissors", "dragon", "devil", "fire", "lightning"],
        "scissors": ["gun", "rock", "water", "dragon", "devil", "fire", "lightning"],
        "fire": ["lightning", "gun", "air", "water", "dragon", "rock", "devil"]
    }

    if user == computer:
        print(f'There is a draw ({user}).')
        return 'draw'
    elif computer in win_dict[user]:  # if the computer's choice is in value that beats the user's choice
        print(f'Sorry, but the computer chose {computer}.')
        return 'lose'
    else:
        print(f'Well done. The computer chose {computer} and failed.')
        return 'win'


def get_score(name):
    with open('C:/Users/thiag/Documents/prog/Python/py/jetbrains/medium/rock_paper_scissors/rating.txt', 'r') as scores:
        for line in scores.readlines():
            return line.split()[1] if line.startswith(name) else '0'


def validate_options():
    valid_options = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
    while True:
        options = input('Choose options: ')
        if options == '':
            valid_options = ['rock', 'paper', 'scissors']
            # print('valid_options', valid_options)
            return valid_options
        options = options.split(',')
        if [option for option in options if option not in valid_options]:
            print('Invalid option.')
            print('Valid options are: rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire.')
        else:
            valid_options = options
            return valid_options

def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    score = int(get_score(name))

    options = validate_options()
    print('options in the game: ', options)
    while True:
        user = input('Choose option: ').strip().lower()
        if user in options:
            computer = choice(options)
            # print('computer: ', computer)
            result = determine_winner(user, computer)
            if result == 'draw':
                score += 50
            elif result == 'win':
                score += 100
        elif user == '!exit':
            print('Bye!')
            break
        elif user == '!rating':
            print(f'Your rating: {score}')
        else:
            print('Invalid input')

main()  