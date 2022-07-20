# Loan Calculator - Stage 02
# https://hyperskill.org/projects/90/stages/501/implement

'''
Objectives
The behavior of your program should look like this:

Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
To perform further calculations, you'll also have to ask for the required missing value.
Finally, output the results for the user.
'''

print('Loan Calculator - Stage 02\n')

import math

principal = float(input('Enter the loan principal: '))
option = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
''')

if option == 'm':
    monthly = float(input('Enter the monthly payment: '))
    months = math.ceil(principal / monthly)
    print(f'It will take {months} months to repay the loan' if months > 1 else f'It will take {months} month to repay the loan')
    
elif option == 'p':
    months = int(input('Enter the number of months: '))
    monthly = math.ceil(principal / months)
    rest = (months * monthly) - principal
    print(f'Your monthly payment = {monthly}' if rest <= 0 else f'Your monthly payment = {monthly} and the last payment = {round(monthly - rest)}.')