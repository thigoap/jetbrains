# Markdown Editor - Stage 05
# https://hyperskill.org/projects/162/stages/843/implement

'''
Description
By this moment, our program can recognize some of the formatters and special commands, it can also print the results and exit. We need to implement yet another very useful feature — the ability to save the text to a file.

Objectives
Modify your !done function that was implemented in the second stage. Apart from exiting the program, it should save the final result of a session to a file, let's call it output.md. Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.
'''

print('Markdown Editor - Stage 05\n')

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
        with open('output.md', 'w') as file:
            file.write(saved_text)
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
    
