# Bill Splitter - Stage 04
# https://hyperskill.org/projects/175/stages/904/implement

'''
Objectives
In this stage your program should perform the following steps together with the steps from the previous stages:

In case of an invalid number of people, "No one is joining for the party" is expected as an output;
Otherwise, if the user choice is Yes, re-split the bill according to the feature;
Round the split value to two decimal places;
Update the dictionary with new split values and 0 for the lucky person;
Print the updated dictionary;
If the user entered anything else instead of Yes, print the original dictionary.
'''

print('Bill Splitter - Stage 04\n')

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
                lucky_feat = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
                if lucky_feat == 'Yes':
                    lucky_one = choice(list(party_dict))
                    print(f'\n{lucky_one} is the lucky one!')
                    partial = round(total / (number - 1), 2)
                    party_dict = {key: partial for key in party_dict}  
                    party_dict[lucky_one] = 0                  
                else:
                    print('\nNo one is going to be lucky')
                    partial = round(total / number, 2)
                    party_dict = {key: partial for key in party_dict}
                
                print(f'\n{party_dict}')
                break

check_invites()