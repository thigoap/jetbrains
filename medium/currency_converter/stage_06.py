# Currency Converter - Stage 06
# https://hyperskill.org/projects/157/stages/822/implement

'''
Description
Now your program knows how to get up-to-date rates. Let's make it more interactive! In this stage, you need to read from the input the currency you have, the currency you want to exchange your money for, and the amount of money you want to exchange. Mind that the input number can have a fractional part!

Keep in mind that the currency you have stays the same, you read it only once in the beginning, then you only need to read the currency you want to exchange your money for and the amount of money since they change. If you come across an empty input, the options for exchange are over.

In product development, the performance is key. Let's use a simple way to speed up the program, called caching. What if you need to do the math for the same exchange target several times? Isn't it better to save rates at runtime, instead of wasting resources on retrieving the same data from the Internet? If you already did calculations for this exchange target before, you know the rate, so there is no need to connect to the Internet, you only need to refer to the data in cache. You can organize the cache anyway you like, but the easiest way would be to use (as you probably already did in stage 5) a dictionary with currencies as keys and rates as values.

Objectives
Let's go over the steps one more time:

Take the first input – the currency that you have. It is default for all the calculations.
Retrieve the data from FloatRates as before.
Save the exchange rates for USD and EUR (these are the most popular ones, so it's good to have rates for them in advance).
Take the second input – the currency code that you want to exchange money for, and the third input – amount of money you have.
Check the cache. Maybe you already have what you need?
If you have the currency in your cache, calculate the result.
If not, get it from the site, and calculate the result.
Save the rate to your cache.
Print the result.
Repeat steps 4-9 until there is no currency left to process.
'''

print('Currency Converter - Stage 06\n')

import requests

your_currency = input('Currency: ').strip()
res = requests.get(f'https://www.floatrates.com/daily/{your_currency}.json')

if res.status_code == 200:
    rates_dict = {}
    if your_currency != 'usd':
        rates_dict['usd'] = res.json()['usd']['rate']
    if your_currency != 'eur':    
        rates_dict['eur'] = res.json()['eur']['rate']

    while True:
        change_to = input('Change to: ')
        if not change_to.strip():
            break
        try:
            amount = float(input('Amount: '))
        except ValueError:
            print('Value Error')
            break
        
        print('Checking the cache...')

        if change_to in rates_dict:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            try:
                rates_dict[change_to] = res.json()[change_to]['rate']
            except KeyError:
                print('Currency not in database.')
                break
        
        print(f'You received {amount * rates_dict[change_to]:.2f} {change_to.upper()}.')

else:
    print('Currency not in database.')
