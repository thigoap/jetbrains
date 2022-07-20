# Honest Calculator - Stage 03
# https://hyperskill.org/projects/208/stages/1041/implement

'''
Objectives
To complete this stage, you need to implement the flowchart above. While doing it, please, follow our recommendations below:

Don't use the built-in function eval() to calculate from a string;
The memory variable must be of a float type;
There are no tests when M is negative. For example, there will be no test input like this: -M + 6;
Copy two messages. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"
'''

print('Honest Calculator - Stage 03\n')

memory = 0

def handle_inputs():
    global memory 
    while True:
        msg_0 = "Enter an equation"
        msg_1 = "Do you even know what numbers are? Stay focused!"
        msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        msg_3 = "Yeah... division by zero. Smart move..."
        msg_4 = "Do you want to store the result? (y / n):"
        msg_5 = "Do you want to continue calculations? (y / n):"

        x, oper, y = input(msg_0).split()
        
        try:
            x = memory if x == 'M' else float(x)
            y = memory if y == 'M' else float(y)

        except ValueError:
            print(msg_1)
        
        else:
            if oper not in '+-*/':
                print(msg_2)
            elif oper == '/' and y == 0:
                print(msg_3)
            else:
                result = do_calcs(x, oper, y)

                while True:
                    store = input(msg_4)
                    if store.lower() == 'y':
                        memory = result
                        break
                    elif store.lower() == 'n':
                        break

                while True:
                    cont = input(msg_5)
                    if cont.lower() == 'y':
                        break
                    elif cont.lower() == 'n':
                        exit()

def do_calcs(x, oper, y):
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        result = x / y
    print(result)
    return result

handle_inputs()