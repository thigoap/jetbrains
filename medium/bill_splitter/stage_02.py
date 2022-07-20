# Bill Splitter - Stage 02
# https://hyperskill.org/projects/175/stages/902/implement

'''
Objectives
In this stage your program should perform the following steps together with the steps of the previous stage:

If there are no people to split the bill (the number of friends is 0 or an invalid input), output "No one is joining for the party";
Else, take user input: the final bill;
Split the total bill equally among everyone;
Round the split value to two decimal places;
Update the dictionary with the split values;
Print the updated dictionary.
Do not print the output of the previous stage (see examples).
'''

print('Bill Splitter - Stage 02\n')

def check_invites():
    try: 
        number = int(input('\nEnter the number of friends joining (including you):\n'))
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
                party_dict = {key: partial for key in party_dict}
                print(f'\n{party_dict}')
                break

check_invites()
