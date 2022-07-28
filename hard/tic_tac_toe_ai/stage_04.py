# Tic Tac Toe with AI - Stage 04
# https://hyperskill.org/projects/82/stages/455/implement

'''
Description
Let's write the medium difficulty level now. To do this, we need to add awareness to our AI.

This level will be a lot harder to beat than easy, even though the initial moves are still random. When the AI is playing at medium level, it wins when it can because of its first rule, and stops all simple attempts to beat it due to its second.

You can see these rules below.

Objectives
When the AI is playing at medium difficulty level, it makes moves using the following logic:

If it already has two in a row and can win with one further move, it does so.
If its opponent can win with one move, it plays the move necessary to block this.
Otherwise, it makes a random move.
You should add a medium parameter so that you can play against this level. It should also be possible to make AIs using easy and medium levels play against each other!
'''

print("Tic Tac Toe with AI - Stage 04\n")

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


def execute_move(board, str_coord):
    board = draw_board(board, str_coord)
    return board


def easy_moves(board):
    pos = ''
    while pos != ' ':
        pos_x = randint(1,3)
        pos_y = randint(1,3)
        pos = board[pos_x - 1][pos_y - 1]
    str_coord = str(pos_x) + ' ' + str(pos_y)
    print('Random move.')
    return str_coord


def check_gaps(board, turn):
    for line_idx, line in enumerate(board):
        if line.count(turn) == 2 and line.count(' ') == 1:
            pos_x = line_idx + 1
            for column_idx, position in enumerate(board[line_idx]):
                if position == ' ':
                    pos_y = column_idx + 1
            str_coord = str(pos_x) + ' ' + str(pos_y)
            return str_coord


def win_or_block(board, turn):
    found = False
    # check lines
    found = check_gaps(board, turn)
    if found:
        print(f'Line: {turn} can win with {found}')
    if not found:  # check columns
        # transpose the board
        board_t = [[board[j][i] for j in range(3)] for i in range(3)]
        found = check_gaps(board_t, turn) 
        if found:
            found = found[::-1]
            print(f'Column: {turn} can win with {found}') 
        if not found:  # check diagonals
            board_d = [
                [board[0][0], board[1][1], board[2][2]],
                [board[2][0], board[1][1], board[0][2]]
                ]
            found = check_gaps(board_d, turn)
            if found:
                temp_coords = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3']
                correct_coords = ['1 1', '2 2', '3 3', '3 1', '2 2', '1 3']
                idx = temp_coords.index(found)
                found = correct_coords[idx]
                print(f'Diag: {turn} can win with {found}')
    return found


def medium_moves(board):
    turn = define_turn(board)
    str_coord = False
    # 1. If it already has two in a row and can win with one further move, it does so.
    str_coord = win_or_block(board, turn)
    if not str_coord:
        # 2. If its opponent can win with one move, it plays the move necessary to block this.
        turn = 'X' if turn == 'O' else 'O'
        str_coord = win_or_block(board, turn)  
        turn = 'X' if turn == 'O' else 'O'
        if not str_coord:
            print('Any winning or blocking move found.')            
            # 3. Otherwise, it makes a random move.
            str_coord = easy_moves(board)
    return str_coord


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
                medium_moves(board)
                valid = ''
                while not valid:
                    coord = input('Enter the coordinates: ')
                    valid = check_move(coord, board)
                board = draw_board(board, coord)
            elif command[move] == 'easy':
                print('Making move level "easy"')
                str_coord = easy_moves(board)
                board = execute_move(board, str_coord)
            elif command[move] == 'medium':
                print('Making move level "medium"')
                str_coord = medium_moves(board)
                board = execute_move(board, str_coord)            
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