# Rock, Paper, Scissors - Stage 03
# https://hyperskill.org/projects/78/stages/433/implement

'''
Objectives
Your program should:

Take input from users;
If the input contains !exit, output Bye! and stop the game;
If the input is the name of the option, then pick a random option and output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Loss: Sorry, but the computer chose <option>
Draw: There is a draw (<option>)
Win: Well done. The computer chose <option> and failed
If the input corresponds to anything else, output Invalid input;
Repeat it all over again.
'''

print('Rock, Paper, Scissors - Stage 03\n')

from random import choice

def determine_winner(user, computer):
    # win_dict[key] wins against key
    win_dict = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    if user == computer:
        print(f'There is a draw ({user}).')
    elif computer == win_dict[user]:  # if the computer's choice is equal to the value that beats the user's choice
        print(f'Sorry, but the computer chose {computer}.')
    else:
        print(f'Well done. The computer chose {computer} and failed.')

def main():
    options = ['rock', 'paper', 'scissors']
    while True:
        user = input('Choose option: ').strip().lower()
        if user in options:
            computer = choice(options)
            # print('computer: ', computer)
            determine_winner(user, computer)
        elif user == '!exit':
            print('Bye!')
            break
        else:
            print('Invalid input')

main()  