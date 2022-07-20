# Honest Calculator - Stage 04
# https://hyperskill.org/projects/208/stages/1042/implement

'''
Objectives
Implement the flowchart with two functions. Please, mind the recommendations below:

Don't use the built-in function eval() to calculate from a string;
Notice that the function is_one_digit() is supposed to check whether it has an integer value in the mathematical sense, e.g. 3.0 is an integer, 3.1 is a non-integer number. Thus, do NOT check the type of variable, but the number itself. You can use a special build-in method .is_integer() on a float variable to check if a number is an integer.
Copy the messages carefully. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
'''

print('Honest Calculator - Stage 04\n')

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
                check(x, oper, y)
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

def check(x, oper, y):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg += msg_7
    if (x == 0 or y == 0) and (oper in '*+-'):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

def is_one_digit(v):
    if v > - 10 and v < 10 and float(v).is_integer():
        return True
    return False

handle_inputs()