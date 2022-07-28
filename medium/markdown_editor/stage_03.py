# Markdown Editor - Stage 03
# https://hyperskill.org/projects/162/stages/841/implement

'''
Objectives
Implement a separate function for each of the formatters. It will keep your code structured. With functions, you will also be able to find and fix a bug with ease if something is wrong.

The program should work in the following way:

Ask a user to input a formatter.
If the formatter doesn't exist, print the following error message: Unknown formatting type or command.
Ask a user to input a text that will be applied to the formatter: Text: <user's input>.
Save the text with the chosen formatter applied to it and print the markdown. Each time you should print out the whole text in markdown accumulated so far.
Different formatters may require different inputs. You can find detailed examples in the Examples section below.

Headings require a level and a text to print. The level is a number from 1 to 6. If the input number is out of bounds, print the corresponding error: The level should be within the range of 1 to 6 and ask the user for input again. A heading should always be printed on a new line and automatically add a new line at the end:
Choose a formatter: > header
Level: > 4
Text: Hello World!
#### Hello World!

Plain, bold, italic, and inline-code formatters require only text input. They should not add an extra space or line break at the end and should add a new formatted text to the previously formatted one (you do not need to print the new formatted text on a new line).
The new-line formatter does not require text input.
Link requires a label and a URL. This formatter should not add an extra space or line break at the end.
Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
[Tutorial](https://www.markdownguide.org/basic-syntax/)
'''

print('Markdown Editor - Stage 03\n')

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

formatters_list = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']
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
               
    elif formatter.lower().strip() not in formatters_list:
        print('Unknown formatting type or command')
    
