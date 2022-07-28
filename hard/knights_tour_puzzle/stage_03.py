# Knight's Tour Puzzle - Stage 03
# https://hyperskill.org/projects/141/stages/748/implement

'''
Objectives
In this stage, you should modify your program to do the following:

Check all 8 possible moving directions from the starting position.
If the move is possible, mark the landing position with the letter 'O'.
If the move is not possible, no action is required.
Don't forget that column and row numbers, as well as the knight position and the 'O' letter for the landing position, should be aligned to the right. For example, for a three-symbols long placeholder, the landing position should look like __O.

Please, don't forget about functional decomposition: splitting your code into reusable functions is very important for the next stages
'''

print("Knight's Tour Puzzle - Stage 03\n")

def check_board(board_dimension):
    try:
        board_dimension = list(map(int, board_dimension.split()))
        assert len(board_dimension) == 2
        if board_dimension[0] < 1 or board_dimension[1] < 1:
            raise ValueError
        return True
    except (ValueError, AssertionError):
        print('Invalid dimensions!')


def check_pos(board_dimension, position):
    board_dimension = list(map(int, board_dimension.split()))
    try:
        position = list(map(int, position.split()))
        assert len(position) == 2
        if position[0] not in range(1, board_dimension[0] + 1) or position[1] not in range(1, board_dimension[1] + 1):
            raise ValueError
        return True
    except (ValueError, AssertionError):
        print('Invalid position!')


def update_matrix(board_dimension, current_pos, visited_pos=[]):
    columns, lines = list(map(int, board_dimension.split()))
    digits = int(len(str(columns * lines)))
    current_pos = list(map(int, current_pos.split()))
    placeholder = '_' * digits
    placeholder_visited = ' ' * (digits - 1)
    board_matrix = [[[column, line] for column in range(1, columns + 1)] for line in range(lines, 0, -1)]
    
    possible_moves = check_possibilities(columns, lines, current_pos)

    board_display = []
    for line in board_matrix:
        for position in line:
            if position == current_pos:
                board_display.append(f'{placeholder_visited}X')
            elif position in possible_moves:
                board_display.append(f'{placeholder_visited}O')
            elif position in visited_pos:
                board_display.append(f'{placeholder_visited}*')
            else:
                board_display.append(placeholder)

    visited_pos.append(current_pos)
    return columns, lines, board_display

def check_possibilities(columns, lines, current_pos):
    deltas = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, -1], [-2, 1], [1, -2], [-1, -2]]
    all_pos = []
    for delta in deltas:
        pos = [x + y for x, y in zip(current_pos, delta)]
        all_pos.append(pos)

    possible_pos = [pos for pos in all_pos if 0 < pos[0] <= columns and 0 < pos[1] <= lines]
    return possible_pos


def display_board(columns, lines, board_display):
    digits = int(len(str(columns * lines)))
    border_length = columns * (digits + 1) + 3
    interval = [(columns * part) - 1 for part in range(lines + 1)]
    print('\nHere are the possible moves:')
    print(' ' * int(len(str(lines))) + '-' * border_length)

    for line in range(lines, 0, -1):
        gap = int(len(str(lines))) - int(len(str(line)))
        # print('slice_inf', str(interval[board_dim[1] - line] + 1))
        # print('slice_sup', str(interval[board_dim[1] - line + 1] + 1))
        board_line = ' '.join(board_display[interval[lines - line] + 1: interval[lines - line + 1] + 1])
        print(' ' * gap + f'{line}| ' + board_line + ' |')

    print(' ' * int(len(str(lines))) + '-' * border_length)
    columns_list = ''.join([' ' * (digits - int(len(str(column + 1)) - 1)) + str(column + 1) for column in range(columns)])
    print(' ' * (1 + int(len(str(lines)))) + columns_list)


board = False
while not board:
    board_dim = input('Enter your board dimensions: ')
    board = check_board(board_dim)

start = False
while not start:
    start_pos = input('Enter the knight\'s starting position: ')
    start = check_pos(board_dim, start_pos)

columns, lines, board_display = update_matrix(board_dim, start_pos)
display_board(columns, lines, board_display)
