# Knight's Tour Puzzle - Stage 05
# https://hyperskill.org/projects/141/stages/750/implement

'''
Objectives
In this stage, you should modify your program to do the following:

Set up a board.
Display the board status and the number of possible moves using Warnsdorff's rule.
Prompt the player for the knight's move.
Check whether the move is valid. If not, ask the player for another move.
Move the knight and mark the position with an 'X'. Mark the visited squares with an '*'.
Repeat the above step until there are no more possible moves.
If the player visits every square without repetition, congratulate them on their victory!
If the player loses, print the number of moves they made.
Please, try to organize your code well, split it into functions and methods, and make them reusable: the difficulty of the next stage greatly depends on this. Its implementation will involve the feature of solving the puzzle automatically. This is not an easy task if your code isn't split into functions.
'''

print("Knight's Tour Puzzle - Stage 05\n")

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


board = False
while not board:
    board_dim = input('Enter your board dimensions: ')
    board = check_board(board_dim)

start = False
while not start:
    start_pos = input('Enter the knight\'s starting position: ')
    start = check_start(board_dim, start_pos)

columns, lines, board_display, possible_pos = update_matrix(board_dim, start_pos)
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
