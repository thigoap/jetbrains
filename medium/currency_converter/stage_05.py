# Currency Converter - Stage 05
# https://hyperskill.org/projects/157/stages/821/implement

'''
Description
In the previous stages, we worked with different real-world currencies but the exchange rates were fixed. Unfortunately (or not, depending on your political stance), we don't really have fixed exchange rates in today's world. At this stage, you will have to work with the Internet to get the information! The FloatRates site contains a special JSON page for each currency. Your task is to make requests to these pages and download the actual data on the exchange rates of the US dollar and the euro. Remember, that the data is stored in JSON format.

Objectives
There are many currency codes, for example, RUB, ARS, HNL, AUD, MAD, etc. Your task is to return the information about the exchange rates from the site specified above for a given currency and USD and EUR.

Take the currency code as the user input.
Make a request to http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json. Don't forget to replace YOUR_CURRENCY_CODE in the link with your currency and put the code in lowercase.
Print your result for USD and EUR.
'''

print('Currency Converter - Stage 05\n')

import requests

currency = input()

r = requests.get(f'https://www.floatrates.com/daily/{currency}.json')
print(r.json()['usd'])
print(r.json()['eur'])
