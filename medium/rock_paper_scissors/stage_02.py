# Rock, Paper, Scissors - Stage 02
# https://hyperskill.org/projects/78/stages/432/implement

'''
Objectives
Your program should:

Read the user input that includes an option;
Choose a random option;
Compare the options and determine the winner;
Output one of the lines above depending on the result of the game.

There are a few examples below to provide the output for any outcome (<option> is the option chosen by your program):

Loss: Sorry, but the computer chose <option>;
Draw: There is a draw (<option>);
Win: Well done. The computer chose <option> and failed;
'''

print('Rock, Paper, Scissors - Stage 02\n')

import random

def random_option():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def determine_winner(user, computer):
    # win_dict[key] wins against key
    win_dict = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    if user == computer:
        print(f'There is a draw ({user}).')
    elif computer == win_dict[user]: # if the computer's choice is equal to the value that beats the user's choice
        print(f'Sorry, but the computer chose {computer}.')
    else:
        print(f'Well done. The computer chose {computer} and failed.')

def main():
    while True:
        user = input('Choose option: ').strip().lower()
        if user in ['rock', 'paper', 'scissors']:
            computer = random_option()
            print('computer: ', computer)
            determine_winner(user, computer)
            break

main()  