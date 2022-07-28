# Tic Tac Toe with AI - Stage 02
# https://hyperskill.org/projects/82/stages/453/implement

'''
Description
Now it's time to make a working game, so let's create our first opponent! In this version of the program, the user will be playing as X, and the computer will be playing as O at easy level. This will be our first small step towards creating the AI!

Let's design it so that at this level the computer makes random moves. This should be perfect for people who have never played the game before!

If you want, you could make the game even simpler by including a difficulty level where the computer never wins. Feel free to create this along with the easy level if you like, but it won't be tested.

Objectives
In this stage, you should implement the following:

Display an empty table when the program starts.
The user plays first as X, and the program should ask the user to enter cell coordinates.
Next, the computer makes its move as O, and the players then move in turn until someone wins or the game results in a draw.
Print the final outcome at the very end of the game.
'''

print("Tic Tac Toe with AI - Stage 02\n")

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
            print('lines', lines)
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
    print(str_coord)
    board = draw_board(board, str_coord)
    return board


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
move = 'user'
draw_board(board)

while True:
    if move == 'user':
        move = 'ia'
        valid = ''
        while not valid:
            coord = input('Enter the coordinates: ')
            valid = check_move(coord, board)
        board = draw_board(board, coord)
    else:
        move = 'user'
        board = ia_moves(board)
    if not board:
        break