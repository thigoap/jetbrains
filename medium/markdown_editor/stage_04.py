# Markdown Editor - Stage 04
# https://hyperskill.org/projects/162/stages/842/implement

'''
Description
There is one more feature that can be very useful! Imagine going to a grocery store, we bet you would need some kind of a list there. Markdown lists are straightforward; there are two kinds of them: ordered and unordered. You've already guessed that the difference between them is that an ordered list itemizes the elements (1., 2., 3., and so on) while an unordered list doesn't do it.

Remember the ordered-list and unordered-list formatters we skipped in the last stage? Let's get back to them!

Objectives
Implement the ordered-list and unordered-list formatters. You may want to separate the implementation into two different functions, but we suggest keeping them in one; try to get an idea of how to do it!

As in the previous stage, ask a user to input a formatter: Choose a formatter. Keep all the functions you implemented in the previous stage and add two new ones: ordered-list and unordered-list.

Both of the new formatters should require the following input:

Number of rows: > 3
Row #1: > First element
Row #2: > Second element
Row #3: > Third element
The number of rows should be greater than zero. If it is not, print the message The number of rows should be greater than zero and ask the user for input again.

Both unordered-list and ordered-list should automatically add a new line at the end. All other formatters should preserve their functionality from the previous stage.
'''

print('Markdown Editor - Stage 04\n')

def help(list):
    formatters_string = ' '.join(list)
    print(f'Available formatters: {formatters_string}')
    print('Special commands: !help !done')


def header(saved_text):
    char = '#'
    level = int(input('Level: '))
    while level not in range(1,7):
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    text = input('Text: ')
    new_text = level * char + ' ' + text + '\n'
    return saved_text + '\n' + new_text if saved_text else new_text


def style(formatter, saved_text):
    style_char_dict = {
        'plain': '',
        'bold': '**',
        'italic': '*',
        'inline-code': '`' 
    }
    text = input('Text: ')
    new_text = style_char_dict[formatter] + text + style_char_dict[formatter]
    return saved_text + new_text


def new_line(saved_text):
    return saved_text + '\n'


def link(saved_text):
    label = input('Label: ')
    url = input('URL: ')
    new_text = '[' + label + ']' + '(' + url + ')'
    return saved_text + new_text


def lists(formatter, saved_text):
    while True:
        rows = (input('Number of rows: '))
        try:
            rows = int(rows)
            if int(rows) < 1:
                raise ValueError
            else:
                all_rows = [input(f'Row #{row + 1}: ') for row in range(rows)]

                if formatter == 'ordered-list':
                    new_text_list = [f'{idx + 1}. {row}' for idx, row in enumerate(all_rows)]
                else:
                    new_text_list = [f'* {row}' for row in all_rows]
                new_text = ''
                for text in new_text_list:
                    new_text += text + '\n'
                return saved_text + new_text 
        except ValueError:
            print('The number of rows should be greater than zero')


formatters_list = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
saved_text = ''

while True:
    formatter = input('Choose a formatter: ')
    if formatter.lower().strip() == '!help':
        help(formatters_list)
    elif formatter.lower().strip() == '!done':
        break
    elif formatter.lower().strip() == 'header':
        saved_text = header(saved_text)
        print(saved_text)
    elif formatter.lower().strip() in ['plain', 'bold', 'italic', 'inline-code']:
        saved_text = style(formatter.lower().strip(), saved_text)
        print(saved_text)
    elif formatter.lower().strip() == 'new-line':
        saved_text = new_line(saved_text)
        print(saved_text)
    elif formatter.lower().strip() == 'link':
        saved_text = link(saved_text)
        print(saved_text)
    elif formatter.lower().strip() == 'ordered-list' or formatter.lower().strip() == 'unordered-list':
        saved_text = lists(formatter, saved_text)
        print(saved_text)   

    elif formatter.lower().strip() not in formatters_list:
        print('Unknown formatting type or command')
    
