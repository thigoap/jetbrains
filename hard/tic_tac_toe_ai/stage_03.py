# Tic Tac Toe with AI - Stage 03
# https://hyperskill.org/projects/82/stages/454/implement

'''
Description
It's time to make things more interesting by adding some game variations. What if you want to play against a friend instead of the AI? How about if you get tired of playing the game and want to see a match between two AIs? You also need to give the user the option of going first or second when playing against the AI.

It should be possible for the user to quit the game after the result is displayed as well.

Objectives
Your tasks for this stage are:

Write a menu loop, which can interpret two commands: start and exit.
Implement the command start. It should take two parameters: who will play X and who will play O. Two options are possible for now: user to play as a human, and easy to play as an AI.
The exit command should simply end the program.
In later steps, you will add the medium and hard levels.

Don't forget to handle incorrect input! The message Bad parameters! should be displayed if what the user enters is invalid.
'''

print("Tic Tac Toe with AI - Stage 03\n")

from random import randint

def draw_board(board, coord=[]):
    if not coord:
        line_1 = '   '
        line_2 = '   '
        line_3 = '   '
    else:
        coord = list(map(int, coord.split()))
        # print('board', board)
        turn = define_turn(board)
        # print('turn', turn)

        new_board = []
        for line in board:
            temp = [char for char in line]
            new_board.append(temp)
        new_board[coord[0] - 1][coord[1] - 1] = turn

        line_1 = new_board[0]
        line_2 = new_board[1]
        line_3 = new_board[2]
    print('-' * 9)
    print(f'| {line_1[0]} {line_1[1]} {line_1[2]} |')
    print(f'| {line_2[0]} {line_2[1]} {line_2[2]} |')
    print(f'| {line_3[0]} {line_3[1]} {line_3[2]} |')
    print('-' * 9)
    lines = [line_1, line_2, line_3]
    # print('lines', lines)
    if coord:
        end_game = check_status(lines)
        if not end_game:
            # print('lines', lines)
            return lines
        else:
            return False
    else:
        return lines


def define_turn(board):
    board = [char for line in board for char in line]
    return 'X' if board.count('X') == board.count('O') else 'O'


def check_status(lines):
    while True:
        # check lines
        for line in lines:
            if line.count('X') == 3:
                print('X wins')
                return True
            elif line.count('O') == 3:
                print('O wins')
                return True
        # check columns
        for j in range(3):
            if lines[0][j] == lines[1][j] and lines[0][j] == lines[2][j] and lines[0][j] in 'OX':
                print(f'{lines[0][j]} wins')
                return True
        # check diagonals
        if lines[0][0] == lines[1][1] and lines[1][1] == lines[2][2] and lines[0][0] in 'OX':
            print(f'{lines[0][0]} wins')
            return True
        elif lines[0][2] == lines[1][1] and lines[1][1] == lines[2][0] and lines[0][2] in 'OX':
            print(f'{lines[0][2]} wins')
            return True
        # check board
        # flatten the list
        board = [char for line in lines for char in line]
        if all([True if char in 'XO' else False for char in board]):
            print('Draw')
            return True
        return False


def check_move(coord, board):
    try:
        coord = list(map(int, coord.split()))
        assert len(coord) == 2
        assert coord[0] in range(1, 4) and coord[1] in range(1, 4)
        char = board[coord[0] - 1][coord[1] - 1]
        # print('char', char)
        if char == 'X' or char == 'O':
            print('This cell is occupied! Choose another one!')
            return False
    except ValueError:
        print('You should enter numbers!')
        return False
    except AssertionError:
        print('Coordinates should be from 1 to 3!')
        return False
    return True


def ia_moves(board):
    print('Making move level "easy"')
    # print(board)
    pos = ''
    while pos != ' ':
        pos_x = randint(1,3)
        pos_y = randint(1,3)
        pos = board[pos_x - 1][pos_y - 1]
    str_coord = str(pos_x) + ' ' + str(pos_y)
    # print(str_coord)
    board = draw_board(board, str_coord)
    return board


def check_input(command):
    players = ['user', 'easy', 'medium', 'hard']
    if command and command[0] == 'exit':
        return True
    elif len(command) == 3 and command[0] == 'start' and command[1] is not None and command[2] is not None:
        if command[1] in players and command[2] in players:
            return True
    print('Bad parameters!')
    return False


def game_loop(command):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_1, player_2 = command[1], command[2]
    # print(player_1, player_2)
    draw_board(board)

    while True:
        for move in range(1,3):
            if command[move] == 'user':
                valid = ''
                while not valid:
                    coord = input('Enter the coordinates: ')
                    valid = check_move(coord, board)
                board = draw_board(board, coord)
            else:
                board = ia_moves(board)
            if not board:
                start_game()    

def start_game():
    command = []
    valid = False
    while not valid:
        command = list(input('Input command: ').split())
        valid = check_input(command)

    if command[0] == 'exit':
        exit()
    elif command[0] == 'start':
        game_loop(command)


start_game()