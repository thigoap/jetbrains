# Knight's Tour Puzzle - Stage 02
# https://hyperskill.org/projects/141/stages/747/implement

'''
Objectives
In this stage, you should modify your program to do the following:

Ask the user for the board's dimensions using X for columns and Y for rows.
If the board's dimensions contain non-integer numbers print Invalid dimensions!.
If the board's dimensions contain more than 2 numbers print Invalid dimensions!.
If the board's dimensions contain negative numbers print Invalid dimensions!.
If invalid dimensions were provided by the user, ask them for valid dimensions again after outputting Invalid dimensions!
Once the starting position is determined, check whether it is valid as in the previous stage.
If not, you should show the Invalid position! error message and then prompt the user for another starting position.
Draw the board.
Use an underscore symbol _ to mark empty board squares; the number of underscore symbols for each empty square should be chosen according to the total number of cells: there should be as many underscores for each cell as there are digits in the total number of cells. For example, a 10 x 10 board has 100 spaces, so your placeholder should be ___ for an empty cell. If your board dimension is 6 x 5, your placeholder will be __. This will be used in later stages.

Make sure that the column numbers are exactly under the placeholders for the given column. Also, make sure your column, row numbers, and the knight position are aligned to the right: for example, the knight positions should be marked as _X or __X (instead of X_ or _X_), depending on the number of underscores for each square.

The border's length also depends on the size of the field. Use the following formula to calculate the length of the required border: column_n * (cell_size + 1) + 3, where column_n is the number of columns, and cell_size is the length of a placeholder for one cell.
'''

print("Knight's Tour Puzzle - Stage 02\n")

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


def display_board(board_dimension, current_pos, visited_pos=[]):
    board_dimension = list(map(int, board_dimension.split()))
    current_pos = tuple(map(int, current_pos.split()))
    digits = int(len(str(board_dimension[0] * board_dimension[1])))
    border_length = board_dimension[0] * (digits + 1) + 3
    placeholder = '_' * digits
    placeholder_visited = ' ' * (digits - 1)

    board_matrix = [[(column, line) for column in range(1, board_dimension[0] + 1)] for line in range(board_dimension[1], 0, -1)]

    board_display = []
    for line in board_matrix:
        for position in line:
            if position == current_pos:
                board_display.append(f'{placeholder_visited}X')
            elif position in visited_pos:
                board_display.append(f'{placeholder_visited}*')
            else:
                board_display.append(placeholder)

    interval = [(board_dimension[0] * part) - 1 for part in range(board_dimension[1] + 1)]

    print(' ' * int(len(str(board_dimension[1]))) + '-' * border_length)

    for line in range(board_dimension[1], 0, -1):
        gap = int(len(str(board_dimension[1]))) - int(len(str(line)))
        # print('slice_inf', str(interval[board_dim[1] - line] + 1))
        # print('slice_sup', str(interval[board_dim[1] - line + 1] + 1))
        board_line = ' '.join(board_display[interval[board_dimension[1] - line] + 1: interval[board_dimension[1] - line + 1] + 1])
        print(' ' * gap + f'{line}| ' + board_line + ' |')

    print(' ' * int(len(str(board_dimension[1]))) + '-' * border_length)
    columns_list = ''.join([' ' * (digits - int(len(str(column + 1)) - 1)) + str(column + 1) for column in range(board_dimension[0])])
    print(' ' * (1 + int(len(str(board_dimension[1])))) + columns_list)

    visited_pos.append(current_pos)


board = False
while not board:
    board_dim = input('Enter your board dimensions: ')
    board = check_board(board_dim)

start = False
while not start:
    start_pos = input('Enter the knight\'s starting position: ')
    start = check_pos(board_dim, start_pos)

display_board(board_dim, start_pos)
