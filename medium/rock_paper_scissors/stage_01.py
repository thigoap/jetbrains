# Rock, Paper, Scissors - Stage 01
# https://hyperskill.org/projects/78/stages/431/implement

'''
Objectives
Your program should:

Take input from the user;
Find an option that wins over the user's option;
Output the line: Sorry, but the computer chose <option>.
'''

print('Rock, Paper, Scissors - Stage 01\n')

while True:
    user = input('Choose option: ').strip().lower()
    if user in ['rock', 'paper', 'scissors']:
        break

# win_dict[key] wins against key
win_dict = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

for key in win_dict:
    if user == key:
        print(f'Sorry, but the computer chose {win_dict[key]}.')
    