# Currency Converter - Stage 04
# https://hyperskill.org/projects/157/stages/820/implement

'''
Objectives
Get the number of conicoins from user input.
Print how much you will get in all five currencies mentioned below.
RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.
'''

print('Currency Converter - Stage 04\n')

amount = float(input())
currencies = ['RUB', 'ARS', 'HNL', 'AUD', 'MAD']
rates = [2.98, 0.82, 0.17, 1.9622, 0.208]

for idx, rate in enumerate(rates):
    value = round(amount * rate, 2)
    print(f'I will get {value} {currencies[idx]} from the sale of {amount} conicoins.')