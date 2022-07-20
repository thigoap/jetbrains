# Loan Calculator - Stage 04
# https://hyperskill.org/projects/90/stages/503/implement

'''
Objectives
In this stage, you are going to implement the following features:

Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).
The final version of your program is supposed to work from the command line and parse the following parameters:

--type indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
--payment is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too:
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
--periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing:
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
You should also display an error message when negative values are entered:

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!
'''

# print('Loan Calculator - Stage 04\n')

import math
import argparse

def validate_params(args, numbers):
    try:
        numbers = [float(number) for number in numbers]
    except TypeError:
        print('Incorrect parameters.')
        return False
    if len(numbers) < 3 or any(n < 0 for n in numbers):
        print('Incorrect parameters.')
        return False
    elif not args.type or not args.interest or\
            (args.type != 'annuity' and args.type != 'diff'):
        print('Incorrect parameters.')
        return False
    elif args.type == 'diff' and args.payment:
        print('Incorrect parameters.')
        return False
    return True


def calculate_principal(interest, payment, periods):
    interest = interest / (12 * 100)
    principal = payment / ((interest * math.pow((1 + interest), periods)) / (math.pow((1 + interest), periods) - 1))
    print(f'Your loan principal = {math.floor(principal)}!')
    overpayment = payment * periods - principal
    print(f'Overpayment = {math.ceil(overpayment)}')


def calculate_periods(interest, payment, principal):
    interest = interest / (12 * 100)
    periods = math.log((payment / (payment - (interest * principal))), (1 + interest))
    y, m = divmod(periods, 12)
    if m > 11:
        m = 0
        y += 1
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
    overpayment = (payment * (12 * y + m)) - principal
    print(f'Overpayment = {math.ceil(overpayment)}')


def calculate_payments(typ, interest, principal, periods):
    interest = interest / (12 * 100)
    if typ == 'annuity':
        annuity = principal * ((interest * math.pow((1 + interest), periods)) / (math.pow((1 + interest), periods) - 1))
        print(f'Your annuity payment = {math.ceil(annuity)}!')
        overpayment = (math.ceil(annuity) * periods) - principal
        print(f'Overpayment = {math.ceil(overpayment)}')
    elif typ == 'diff':
        monthly = [math.ceil((principal / periods) + (interest * (principal - (principal * (month + 1 - 1)) / periods))) for month in range(periods)]
        for month in range(periods):
            print(f'Month {month + 1}: payment is {monthly[month]}')

        overpayment = sum(monthly) - principal
        print(f'\nOverpayment = {math.ceil(overpayment)}')


def loan_calculator(args, numbers):
    valid = validate_params(args, numbers)
    if not valid:
        return False
    if args.principal is None:
        interest = float(args.interest)
        payment = float(args.payment)
        periods = int(args.periods)
        calculate_principal(interest, payment, periods)
    elif args.periods is None:
        interest = float(args.interest)
        payment = float(args.payment)
        principal = float(args.principal)
        calculate_periods(interest, payment, principal)
    elif args.payment is None:
        typ = args.type
        interest = float(args.interest)
        principal = float(args.principal)
        periods = int(args.periods)
        calculate_payments(typ, interest, principal, periods)


parser = argparse.ArgumentParser(description="Loan Calculator.")
parser.add_argument("-t", "--type",
                    choices=["annuity", "diff"],
                    help="You need to choose between annuity or diff.")
parser.add_argument("-i", "--interest",
                    help="The loan interest. Always needed.")

parser.add_argument("-pay", "--payment",
                    help="The loan payment. Needs interest, principal, and periods.")
parser.add_argument("-pri", "--principal",
                    help="The loan principal. Needs interest, annuity payment, and periods.")
parser.add_argument("-per", "--periods",
                    help="The loan periods. Needs interest, annuity payment, and principal.")

args = parser.parse_args()
numbers = [args.interest, args.payment, args.principal, args.periods]
numbers = [number for number in numbers if number is not None]

loan_calculator(args, numbers)
