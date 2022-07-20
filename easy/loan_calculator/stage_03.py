# Loan Calculator - Stage 03
# https://hyperskill.org/projects/90/stages/502/implement

'''
Objectives
In this stage, you should add new behavior to the calculator:

First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
Then, you need to ask them to input the remaining values.
Finally, compute and output the value that they wanted.
Note that you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:

The first is the loan principal (P in the formulas).
The second is the monthly payment (A in the formulas).
The next is the number of monthly payments (n in the formulas).
The last is the loan interest. The user inputs the interest rate as a percentage, for example, 11.7. You should divide this value by 12 and 100 to use it as i in the formula.
Please be careful converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).
'''

print('Loan Calculator - Stage 03\n')

import math

option = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
''')

# calculate number of montlhy payments
if option == 'n':
    p = float(input('Enter the loan principal: '))
    a = float(input('Enter the monthly payment: '))
    ip = float(input('Enter the loan interest: '))
    i = ip / (12 * 100)

    n = math.log( (a / (a - (i * p))), (1 + i) )

    y, m = divmod(n, 12)
    if m > 11:
        m = 0
        y +=1
    y = round(math.ceil(y))
    m = round(math.ceil(m))
    
    year = 'years' if y > 1 else 'year'
    month = 'months' if m > 1 else 'month'

    if y and m:    
        print(f'It will take {y} {year} and {m} {month} to repay this loan!')
    elif y:
        print(f'It will take {y} {year} to repay this loan!') 
    else:
        print(f'It will take {m} {month} to repay this loan!')               
       

# calculate monthly payment (called annuity payment) amount
elif option == 'a':
    p = float(input('Enter the loan principal: '))
    n = int(input('Enter the number of periods: '))
    ip = float(input('Enter the loan interest: '))
    i = ip / (12 * 100)

    a = p * ( (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1) )
    print(f'Your monthly payment = {math.ceil(a)}!')

# calculate loan principal
elif option == 'p':
    a = float(input('Enter the annuity payment: '))
    n = int(input('Enter the number of periods: '))
    ip = float(input('Enter the loan interest: ' ))
    i = ip / (12 * 100)

    p = a / ( (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1) )
    print(f'Your loan principal = {math.floor(p)}!')
    