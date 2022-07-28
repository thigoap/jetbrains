# Knight's Tour Puzzle - Stage 01
# https://hyperskill.org/projects/141/stages/746/implement

'''
Description
The knight's tour problem uses a chessboard and a knight. Don't worry, you won't need to know the chess basics for this project, you only need to know how a knight moves on the board.

A standard chess board is an 8x8 square on which the chess pieces are placed. For this project, we will use a coordinate system (x,y) to label each square on the chessboard, where (1,1) is the bottom left, and (8,8) is the top right.
The rules of the knight's tour are as follows:

The knight can start at any square.
The knight must visit every square by moving in the L-shape.
The knight can visit each square only once.
The knight can finish anywhere on the board. This is called an 'open' tour of the board.
You win if you visit every square on the board.
You lose if you fail to visit every square only once without revisiting it.

Objectives
Let's get started by setting up the puzzle:

Ask the user for the knight's starting position.
If the user input contains non-integer numbers you should print Invalid dimensions!.
If the user input contains more than 2 numbers you should print Invalid dimensions!.
If the user input numbers out of bounds of the game field you should print Invalid dimensions!.
Display the 8x8 chessboard with the knight in this position. You should display a frame around the board and mark the column and row numbers. You should use an underscore _ for an empty cell with a space in between them, and an X for the knight's position.
'''

print("Knight's Tour Puzzle - Stage 01\n")

def display_board(position):
    print('', '-' * 19)
    for line in range(8, 0, -1):
        pos = ''
        for column in range(1, 9):
            pos = pos + 'X ' \
                if line == position[1] and column == position[0] \
                else pos + '_ '
        print(f'{line}| {pos}|')
    print('', '-' * 19)
    print('   1 2 3 4 5 6 7 8')


try:
    start = list(map(int, input('Enter the knight\'s starting position: ').split()))
    '''start = input('Enter the knight\'s starting position: ').split()
    start = [int(x) for x in start]'''
    assert len(start) == 2
    if start[0] not in range(1, 9) or start[1] not in range(1, 9):
        raise ValueError
    display_board(start)
except (ValueError, AssertionError):
    print('Invalid dimensions!')
