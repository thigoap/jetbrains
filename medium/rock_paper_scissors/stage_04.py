# Rock, Paper, Scissors - Stage 04
# https://hyperskill.org/projects/78/stages/434/implement

'''
Description
People love to see their results as they're advancing to their goals. So, let's learn how to show the scoreboard!

When the game starts, users must be able to enter their names. After that, the program should greet users and read a file named rating.txt. It is the file that contains the current scores for different players. You can see the file format below: lines containing user names and their scores divided by a single space:

Tim 350
Jane 200
Alex 400
Take the current user score from the file and use it as a basis for counting the score during the game. For example, if a user entered Tim, then their score at the start of the game is 350. If a user inputs a name that is not on the list, the program should count the score from 0.

No need to write anything to the rating.txt file.
Print the user score with the !rating command. For example, if your rating is 0, then the program should print:

Your rating: 0
Add 50 points for every draw, 100 for every win, and 0 for losing.

Objectives
Your program should:

Output a line Enter your name: . Users enter their names on the same line (not the one following the output!);
Read input with the name and output a new line: Hello, <name>
Read rating.txt and check whether it contains an entry with the current username. If yes, use the score specified in the file as a starting point. If not, start the score from 0.
Play the game by the rules defined in the previous stages and read the user input;
If the input is !exit, output Bye! and stop the game;
If the input is the name of the option, then pick a random option and output a line with the result in the following format (<option> is the name of the option chosen by the program):
Loss: Sorry, but the computer chose <option>
Draw: There is a draw (<option>)
Win: Well done. The computer chose <option> and failed
For each draw, add 50 points to the score. For each win, add 100 points. In case a user loses, don't change the score;
If the input corresponds to anything else, output Invalid input;
Restart the game.
'''

print('Rock, Paper, Scissors - Stage 04\n')

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
        return 'draw'
    elif computer == win_dict[user]:  # if the computer's choice is equal to the value that beats the user's choice
        print(f'Sorry, but the computer chose {computer}.')
        return 'lose'
    else:
        print(f'Well done. The computer chose {computer} and failed.')
        return 'win'


def get_score(name):
    with open('C:/Users/thiag/Documents/prog/Python/py/jetbrains/medium/rock_paper_scissors/rating.txt', 'r') as scores:
        for line in scores.readlines():
            return line.split()[1] if line.startswith(name) else '0'


def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    score = int(get_score(name))

    options = ['rock', 'paper', 'scissors']
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