# Dominoes - Stage 02
# https://hyperskill.org/projects/146/stages/787/implement

'''
Objectives
Print the header using seventy equal sign characters (=).
Print the number of dominoes remaining in the stock – Stock size: [number].
Print the number of dominoes the computer has – Computer pieces: [number].
Print the domino snake. At this stage, it consists of the only starting piece.
Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
Print the status of the game:
If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
If status = "player", print "Status: It's your turn to make a move. Enter your command."
Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.
'''

print('Dominoes - Stage 02\n')

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
        domino_snake = both_pieces[id]
        
        if id < 7:
            status = 'Computer is about to make a move. Press Enter to continue...'
            player_pieces.remove(both_pieces[id])
        else: 
            status = "It's your turn to make a move. Enter your command."
            computer_pieces.remove(both_pieces[id])

    print('='* 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}')
    print(f'\n{domino_snake}\n')
    print('Your pieces:')
    for idx, piece in enumerate(player_pieces):
        print(f'{idx + 1}:{piece}')    
    print(f'\nStatus: {status}')
    
distribute()