# Bill Splitter - Stage 03
# https://hyperskill.org/projects/175/stages/903/implement

'''
Objectives
In this stage your program should perform the following steps together with the steps from the previous stages:

In case of an invalid number of people, "No one is joining for the party" is expected as an output;
Otherwise, ask the user whether they want to use the "Who is lucky?" feature;
Take input from the user;
If a user wants to use the feature (Yes), choose a name from the dictionary keys at random and print the following: {Name} is the lucky one!;
If the user enters anything else, print No one is going to be lucky.
Do not print the output of the previous stage (see examples).
'''

print('Bill Splitter - Stage 03\n')

from random import choice

def check_invites():
    try: 
        number = int(input('Enter the number of friends joining (including you):\n'))
        if number <= 0:
            raise ValueError          
    except ValueError:
        print('\nNo one is joining for the party')
    else:
        print('\nEnter the name of every friend (including you), each on a new line:')
        party_dict = {input(): 0 for _ in range(number)}
        while True:
            try:
                total = float(input('\nEnter the total bill value:\n'))
            except ValueError:
                print('\nNeed a float number.')
            else:
                partial = round(total / number, 2)
                # party_dict = {key: partial for key in party_dict}
                # print(f'\n{party_dict}')
        
                lucky_feat = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
                if lucky_feat == 'Yes':
                    lucky_one = choice(list(party_dict))
                    print(f'\n{lucky_one} is the lucky one!')
                else:
                    print('\nNo one is going to be lucky')
                break

check_invites()