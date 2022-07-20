# Honest Calculator - Stage 02
# https://hyperskill.org/projects/208/stages/1040/implement

'''
Objectives
Implement the flowchart above. While doing it, please, follow our recommendations:

Don't use the built-in functions to calculate from a string;
The result variable must be of the float type;
Copy the message. The tests will check if the correct message appears in the correct order. So don't add extra lines or characters: msg_3 = "Yeah... division by zero. Smart move..."
'''

print('Honest Calculator - Stage 02\n')

def handle_inputs():
    while True:
        msg_0 = "Enter an equation: "
        msg_1 = "Do you even know what numbers are? Stay focused!"
        msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        msg_3 = "Yeah... division by zero. Smart move..."
       
        x, oper, y = input(msg_0).split()

        try:
            x = float(x)
            y = float(y)

        except ValueError:
            print(msg_1)
        
        else:
            if oper not in '+-*/':
                print(msg_2)
            elif oper == '/' and y == 0:
                print(msg_3)
            else:
                do_calcs(x, oper, y)
                break

def do_calcs(x, oper, y):
    if oper == '+':
        print(x + y)
    elif oper == '-':
        print(x - y)
    elif oper == '*':
        print(x * y)
    elif oper == '/':
        print(x / y)

handle_inputs()