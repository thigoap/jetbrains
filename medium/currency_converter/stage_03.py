# Currency Converter - Stage 03
# https://hyperskill.org/projects/157/stages/819/implement

'''
Objectives
Get the number of conicoins from the user input.
Get the exchange rate from the user input.
Calculate and print the result.
'''

print('Currency Converter - Stage 03\n')

amount = float(input('Please, enter the number of conicoins you have: '))
rate = float(input('Please, enter the exchange rate: '))
dollars = amount * rate
print(f'The total amount of dollars: {dollars:.2f}')

