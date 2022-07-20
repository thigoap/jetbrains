# Bill Splitter - Stage 01
# https://hyperskill.org/projects/175/stages/901/implement

'''
Objectives
In this stage your program should perform the following steps:

Take user input — how many people want to join, including the user;
In case of an invalid number of people (zero or negative), "No one is joining for the party" is expected as an output;
Otherwise, take the friends' names as input, iteratively;
Store them in a dictionary initialized with zeros;
Print out the dictionary.
To communicate with the user, please use the prompts specified in the examples. Note that here and in the following stages we expect you to take every input in a new line.
'''

print('Bill Splitter - Stage 01\n')

def check_invites():
    try: 
        number = int(input('Enter the number of friends joining (including you):\n'))
        if number <= 0:
            raise ValueError          
    except ValueError:
        print('\nNo one is joining for the party')
    else:
        print('\nEnter the name of every friend (including you), each on a new line:')
        party_list = {input(): 0 for _ in range(number)}
        print(f'\n{party_list}')

check_invites()
