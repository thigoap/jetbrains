# Honest Calculator - Stage 05
# https://hyperskill.org/projects/208/stages/1043/implement

'''
Objectives
Implement the flowchart. Please, follow the recommendations below:

Don't use the built-in function eval() to calculate from a string;
Copy the messages below. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
'''

print('Honest Calculator - Stage 05\n')

memory = 0

def handle_inputs():
    global memory 
    while True:
        msg_0 = "Enter an equation: "
        msg_1 = "Do you even know what numbers are? Stay focused!"
        msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        msg_3 = "Yeah... division by zero. Smart move..."
        msg_4 = "Do you want to store the result? (y / n): "
        msg_5 = "Do you want to continue calculations? (y / n): "

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
                        mem = stupid_questions(result)
                        if mem is not None:
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

def stupid_questions(result):
    msg_10 = "Are you sure? It is only one digit! (y / n): "
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n): "
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n): "
    msgs = [msg_10, msg_11, msg_12]

    if is_one_digit(result):
        msg_idx = 0
        while msg_idx < len(msgs):
            msg_x = input(msgs[msg_idx])
            if msg_x == 'n':
                result = None
                break
            elif msg_x == 'y':
                msg_idx += 1
                # print('msg_idx', msg_idx) 
        return result

    return result

handle_inputs()