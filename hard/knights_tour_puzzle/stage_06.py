# Knight's Tour Puzzle - Stage 06
# https://hyperskill.org/projects/141/stages/764/implement

'''
Objectives
In this stage, you should modify your program to do the following:

Set up the board.
Ask the player whether they want to try the puzzle or see the solution with a line Do you want to try the puzzle? (y/n):. If the user enters y, proceed to step 3. If the user enters n, proceed to step 4. In the case of any other input print Invalid input! and ask the same question.
If the player wants to try the puzzle, check whether the board has a solution. If not, print No solution exists! and end the game. Otherwise, let the player give the puzzle a try like in the previous stage.
If they want to see the solution, check whether the board has one. Print No solution exists! in case there is none. If a solution exists, label the starting point as 1, then label each move with the next number until you have visited all the squares.
If the board is big and the number of moves exceeds 9, use spaces for the extra digits and align the text to the right.
The most intuitive method for the solution finder is to use recursion and backtracking. The recursive function should check the best possible move based on Warnsdorff's rule. The function should call itself from the new position, and continue to call itself until there are no more possible moves. If you've visited all the squares, then it is the solution you're looking for. If not, it means you've reached a dead end and need to go back to the previous square and check the next best possible move. Obviously, bigger boards take much longer to solve.
'''

print("Knight's Tour Puzzle - Stage 06\n")

from ktp_solver import ktp_solver 

def check_board(board_dimension):
    try:
        board_dimension = list(map(int, board_dimension.split()))
        assert len(board_dimension) == 2
        if board_dimension[0] < 1 or board_dimension[1] < 1:
            raise ValueError
        return True
    except (ValueError, AssertionError):
        print('Invalid dimensions!')


def check_start(board_dimension, start_pos):
    board_dimension = list(map(int, board_dimension.split()))
    try:
        start_pos = list(map(int, start_pos.split()))
        assert len(start_pos) == 2
        if start_pos[0] not in range(1, board_dimension[0] + 1) or start_pos[1] not in range(1, board_dimension[1] + 1):
            raise ValueError
        return True
    except (ValueError, AssertionError):
        print('Invalid position!')


def check_move(position, possibilities):
    try:
        position = list(map(int, position.split()))
        assert len(position) == 2
        if position not in possibilities:
            return False
        return True
    except (ValueError, AssertionError):
        return False


def update_matrix(board_dimension, current_pos, visited_pos=[]):
    columns, lines = list(map(int, board_dimension.split()))
    digits = int(len(str(columns * lines)))
    current_pos = list(map(int, current_pos.split()))
    placeholder = '_' * digits
    placeholder_visited = ' ' * (digits - 1)
    board_matrix = [[[column, line] for column in range(1, columns + 1)] for line in range(lines, 0, -1)]
    
    possible_moves, len_pos = check_possibilities(columns, lines, current_pos, visited_pos)

    board_display = []
    for line in board_matrix:
        for position in line:
            if position == current_pos:
                board_display.append(f'{placeholder_visited}X')
            elif position in possible_moves:
                possible, num_possibilities = check_possibilities(columns, lines, position, visited_pos)
                board_display.append(f'{placeholder_visited}{num_possibilities}')
            elif position in visited_pos:
                board_display.append(f'{placeholder_visited}*')
            else:
                board_display.append(placeholder)

    visited_pos.append(current_pos)
    return columns, lines, board_display, possible_moves


def check_possibilities(columns, lines, current_pos, visited_pos=[]):
    deltas = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, -1], [-2, 1], [1, -2], [-1, -2]]
    all_pos = []
    for delta in deltas:
        pos = [x + y for x, y in zip(current_pos, delta)]
        all_pos.append(pos)

    possible_pos = [pos for pos in all_pos if
        0 < pos[0] <= columns and
        0 < pos[1] <= lines and
        pos not in visited_pos]

    return possible_pos, len(possible_pos) - 1


def display_board(columns, lines, board_display):
    digits = int(len(str(columns * lines)))
    border_length = columns * (digits + 1) + 3
    interval = [(columns * part) - 1 for part in range(lines + 1)]
    print(' ' * int(len(str(lines))) + '-' * border_length)

    for line in range(lines, 0, -1):
        gap = int(len(str(lines))) - int(len(str(line)))
        # print('slice_inf', str(interval[board_dim[1] - line] + 1))
        # print('slice_sup', str(interval[board_dim[1] - line + 1] + 1))
        board_line = ' '.join(board_display[interval[lines - line] + 1: interval[lines - line + 1] + 1])
        print(' ' * gap + f'{line}| ' + board_line + ' |')

    print(' ' * int(len(str(lines))) + '-' * border_length)
    columns_list = ''.join([' ' * (digits - int(len(str(column + 1)) - 1)) + str(column + 1) for column in range(columns)])
    print(' ' * (1 + int(len(str(lines)))) + columns_list + '\n')


def display_solution(solved):
    if not solved:
        print('No solution exists!')
    else:
        print('\nHere\'s the solution!')
        solved_flat = [(item) for sublist in solved for item in sublist]
        placeholder = ' ' * (len(str(max(solved_flat))) - 1) 
        solved_flat_str = [placeholder + str(item) if len(str(item)) < len(str(max(solved_flat))) else str(item) for item in solved_flat ]
        display_board(columns, lines, solved_flat_str)


board = False
while not board:
    board_dim = input('Enter your board dimensions: ')
    board = check_board(board_dim)

start = False
while not start:
    start_pos = input('Enter the knight\'s starting position: ')
    start = check_start(board_dim, start_pos)


answer = ''
while answer.lower() != 'n' and answer.lower() != 'y':
    answer = input('Do you want to try the puzzle? (y/n): ')
    if answer.lower() != 'n' and answer.lower() != 'y':
        print('Invalid input!', end=' ')

columns, lines, board_display, possible_pos = update_matrix(board_dim, start_pos)
solved = ktp_solver(board_dim, start_pos)

if answer.lower() == 'y':
    if not solved:
        display_solution(solved)
        exit()

    display_board(columns, lines, board_display)

    counter = 1
    while True:
        
        if len(possible_pos) == 0:
            if counter == columns * lines:
                print('What a great tour! Congratulations!')      
            else:
                print('No more possible moves!')
                print(f'Your knight visited {counter} squares!')
            break
        
        valid = False
        while not valid:
            move_pos = input('Enter your next move: ')
            valid = check_move(move_pos, possible_pos)
            if not valid:
                print('Invalid move! ', end='')

        columns, lines, board_display, possible_pos = update_matrix(board_dim, move_pos)
        display_board(columns, lines, board_display)
        counter += 1
elif answer.lower() == 'n':
    display_solution(solved)