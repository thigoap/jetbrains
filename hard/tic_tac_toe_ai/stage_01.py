# Tic Tac Toe with AI - Stage 01
# https://hyperskill.org/projects/82/stages/452/implement

'''
Description
In this project, you'll write a game called Tic-Tac-Toe that you can play against your computer. The computer will have three levels of difficulty — easy, medium, and hard.

To begin with, let's write a program that knows how to work with coordinates and determine the state of the game.

The top-left cell will have the coordinates (1, 1) and the bottom-right cell will have the coordinates (3, 3), as shown in this table:

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

The program should ask the user to enter the coordinates of the cell where they want to make a move.

Keep in mind that the first coordinate goes from left to right, and the second coordinate goes from top to bottom. Also, notice that coordinates start with 1 and can be 1, 2, or 3.

But what if the user attempts to enter invalid coordinates? This could happen if they try to enter letters or symbols instead of numbers, or the coordinates of an already occupied cell. Your program needs to prevent these things from happening by checking the user's input and catching possible exceptions.

Objectives
The program should work in the following way:

Ask the user to provide the initial state of the 3x3 table with the first input line. This must include nine symbols that can be X, O or _ (the latter represents an empty cell).
Output the specified 3x3 table before the user makes a move.
Request that the user enters the coordinates of the move they wish to make.
The user then inputs two numbers representing the cell in which they wish to place their X or O. The game always starts with X, so the user's move should be made with this symbol if there are an equal number of X's and O's in the table. If the table contains an extra X, the move should be made with O.
Analyze the user input and show messages in the following situations:
• This cell is occupied! Choose another one! — if the cell is not empty;
• You should enter numbers! — if the user tries to enter letters or symbols instead of numbers;
• Coordinates should be from 1 to 3! — if the user attempts to enter coordinates outside of the table's range.
Display the table again with the user's most recent move included.
Output the state of the game.
The possible states are:

Game not finished — when no side has three in a row, but the table still has empty cells;
Draw — when no side has three in a row, and the table is complete;
X wins — when there are three X's in a row;
O wins — when there are three O's in a row.
If the user provides invalid coordinates, the program should repeat the request until numbers that represent an empty cell on the table are supplied. You should ensure that the program only outputs the table twice — before the move and after the user makes a legal move.
'''

print("Tic Tac Toe with AI - Stage 01\n")

def initial_state():
    while True:
        initial_state = input('Enter the cells: ')
        if len(initial_state) == 9 and all([True if char.upper() in 'XO_' else False for char in initial_state]):
            return draw_board(initial_state)
        else:
            print('Invalid symbols. Use X, O, or _.')


def draw_board(board, coord=[]):
    if not coord:
        line_1 = board[:3].upper().replace('_', ' ')
        line_2 = board[3:6].upper().replace('_', ' ')
        line_3 = board[6:].upper().replace('_', ' ')
    else:
        coord = list(map(int, coord.split()))
        print(board)
        turn = define_turn(board)
        print('turn', turn)

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
    if coord:
        end_game = check_status(lines)
        if not end_game:
            return lines
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
        else:
            print('Game not finished')
            return False


def check_move(coord, board):
    try:
        coord = list(map(int, coord.split()))
        assert len(coord) == 2
        assert coord[0] in range(1, 4) and coord[1] in range(1, 4)
        char = board[coord[0] - 1][coord[1] - 1]
        # print('char', char)
        if char in 'XO':
            print('This cell is occupied! Choose another one!')
            return False
    except ValueError:
        print('You should enter numbers!')
        return False
    except AssertionError:
        print('Coordinates should be from 1 to 3!')
        return False
    return True


def game_loop(board):
    valid = ''
    while not valid:
        coord = input('Enter the coordinates: ')
        valid = check_move(coord, board)
    draw_board(board, coord)


board = initial_state()
# print('status', board)
while board:
    game_loop(board)