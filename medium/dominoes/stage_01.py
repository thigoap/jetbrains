# Dominoes - Stage 01
# https://hyperskill.org/projects/146/stages/786/implement

'''
Objectives
Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer".
Stock pieces      # 14 domino elements
Computer pieces   # 7 or 6 domino elements
Player pieces     # 6 or 7 domino elements
Domino snake      # 1 starting domino
Status            # the player that goes first
If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
Output all five variables.

Examples
Example 1

The player makes the first move.

Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
Domino snake: [[6, 6]]
Status: player
'''

print('Dominoes - Stage 01\n')

from  random import randint

def distribute():
    domino_snake = []
    while domino_snake == []:
        pieces = [[i, j] for i in range(0,7) for j in range(0,7) if j >= i]
        stock_pieces = [pieces.pop(randint(0,len(pieces)-1)) for piece in range(0,14)]
        player_pieces = [pieces.pop(randint(0,len(pieces)-1)) for piece in range(0,7)]
        computer_pieces = pieces

        both_pieces = player_pieces + computer_pieces
        piece_sum = id = 0
        for idx, piece in enumerate(both_pieces):
            if piece[0] == piece[1]:
                c_piece_sum = sum(piece)
                if c_piece_sum > piece_sum:
                    piece_sum = c_piece_sum
                    id = idx

        domino_snake = [both_pieces[id]]
        if id < 7:
            status = 'computer'
            player_pieces.remove(both_pieces[id])
        else: 
            status = 'player'    
            computer_pieces.remove(both_pieces[id])

    print(f'Stock pieces: {stock_pieces}')
    print(f'Player pieces: {player_pieces}')
    print(f'Computer pieces: {computer_pieces}')
    print(f'Domino snake: {domino_snake}')
    print(f'Status: {status}')
    
distribute()