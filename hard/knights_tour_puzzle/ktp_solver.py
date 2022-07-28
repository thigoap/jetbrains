def ktp_solver(board_dim, start_pos):
    columns, lines = list(map(int, board_dim.split()))
    col, line = list(map(int, start_pos.split()))

    board = [[0 for column in range(columns)] for line in range(lines)]
    board[lines - line][col - 1] = 1
    # print(f'\nSolving for a {columns}x{lines} board, starting in {col}x{line}...')
    solved = solve(board, lines - line, col - 1, lines, columns, 2)
    # print(solved)
    return solved
    

def validate(board, new_x, new_y, lines, columns):
    if new_x in range(0, lines) and new_y in range(0, columns) and board[new_x][new_y] == 0:
        return True


def solve(board, pos_x, pos_y, lines, columns, counter):
    deltas = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, -1], [-2, 1], [1, -2], [-1, -2]]
    for i in range(8):
        if counter >= (lines * columns) + 1:  
            return True
        new_x = pos_x + deltas[i][0]
        new_y = pos_y + deltas[i][1]
        if validate(board, new_x, new_y, lines, columns):
            board[new_x][new_y] = counter
            if solve(board, new_x, new_y, lines, columns, counter + 1):
                # return True
                return board
            board[new_x][new_y] = 0
    return False


# ktp_solver('4 3', '1 3')