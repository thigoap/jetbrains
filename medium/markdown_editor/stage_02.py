# Markdown Editor - Stage 02
# https://hyperskill.org/projects/162/stages/840/implement

'''
Objectives
Implement the help function (!help) that will print available syntax commands, which we have indicated above, as well as the special commands. When called, it should print the following:

Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
Implement the exit function (!done) that exits the editor without saving.

Ask a user for input: Choose a formatter:.

If the input contains one of the correct formatters (plain, bold, italic, etc.), ask for the input once again.
If the input contains no formatters or unknown command is sent, print the following message and ask for input again: Unknown formatting type or command.
If the input contains !help, print the list of available commands, as shown in the example below. If the input contains !done, exit the editor without saving.
'''

print('Markdown Editor - Stage 02\n')

def help(list):
    formatters_string = ' '.join(list)
    print(f'Available formatters: {formatters_string}')
    print('Special commands: !help !done')

formatters_list = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']

while True:
    formatter = input('Choose a formatter: ')
    if formatter.lower().strip() not in formatters_list:
        if formatter.lower().strip() == '!help':
            help(formatters_list)
        elif formatter.lower().strip() == '!done':
            break
        elif formatter.lower().strip() not in formatters_list:
            print('Unknown formatting type or command')
