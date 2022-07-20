# Honest Calculator - Stage 01
# https://hyperskill.org/projects/208/stages/1039/implement

'''
Objectives
Implement the flowchart above. Please, follow our recommendations:

The variable calc should have the following format: x operation y. For example: 2 + 3, 2 + g or 3.1 r 5;
The variables x and y must be of the float or int type. The oper variable is a one-character string. Check whether the passed values have proper types. The delimiter must be a dot;
Don't use the built-in eval() function to calculate from a string, please! It'll be much more useful to you if you try to apply the tools you've learned in theory and practice to use them for specific tasks;
Copy the messages below carefully. The tests will check if the correct message appears in the correct order. Please, do not add extra lines or characters.
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
'''

print('Honest Calculator - Stage 01\n')

def handle_inputs():
    while True:
        msg_0 = "Enter an equation: "
        msg_1 = "Do you even know what numbers are? Stay focused!"
        msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

        x, oper, y = input(msg_0).split()

        try:
            x = float(x)
            y = float(y)

        except ValueError:
            print(msg_1)
        
        else:
            if oper not in '+-*/':
                print(msg_2)
            else:
                break

handle_inputs()