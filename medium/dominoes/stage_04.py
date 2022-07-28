# Dominoes - Stage 04
# https://hyperskill.org/projects/146/stages/789/implement

'''
Description
You can't have a game without rules. It's time to introduce them!

Until now, the players were able to place their dominoes however they like. Now, it is considered a violation. According to the rules, the numbers on the ends of the two neighboring dominoes must match each other. This rule can also be described as a set of two requirements:

A player cannot add a domino to the end of the snake if it doesn't contain the matching number.
The orientation of the newly added domino ensures that the matching numbers are neighbors.
For example, consider the following situation:

We have a [3,4],[4,4],[4,2] snake and a [1,2] domino. The domino cannot be added to the left side of the snake because there is no 3 in [1,2]. However, the domino can be added to the right side of the snake because [1,2] contains a 2. If we were to place the domino on the right side of the snake, we would have to reorient it: [3,4],[4,4],[4,2],[2,1].

These two requirements are strict for both the player and the computer.

Objectives
Add the following functionality to your code. When it's a player's turn, the program should:

Verify that the move entered by the player is legal (requirement #1).
If not, request a new input with the following message: Illegal move. Please try again..
Place dominoes with the correct orientation (requirement #2).
When it's a computer's turn, the program should:

Try random moves until it finds a legal one.
A set of possible moves ranges from -computer_size to computer_size (where the computer_size is the number of dominoes the computer still has). Skipping a turn (move 0) is always legal.
Place dominoes with the correct orientation.
'''

print('Dominoes - Stage 04\n')

from  random import randint

def initial():
    global stock_pieces, computer_pieces, player_pieces, domino_snake, status
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

def handle_player_choice(domino_snake_str):
    while True:
        try:
            player_choice = int(input())
            if abs(player_choice) > len(player_pieces):
                print('Invalid input. Please try again.')
            elif player_choice == 0:
                pick_domino()
                return player_choice
            else:
                valid = validate_player_choice(player_choice, domino_snake_str)
                if valid:
                    return player_choice
        except (ValueError, IndexError):
            print('Invalid input. Please try again.')

def validate_player_choice(player_choice, domino_snake_str):
    while True:
        piece = player_pieces[abs(player_choice) - 1]
        if player_choice > 0:
            match = int(domino_snake_str[-2:-1])
            if piece[0] == match:
                return player_choice
            elif piece[1] == match:
                player_pieces[abs(player_choice) - 1].reverse()
                return player_choice
            else:
                print('Illegal move. Please try again..')
                break
        else:
            match = int(domino_snake_str[1:2])
            if piece[1] == match:
                return player_choice
            elif piece[0] == match:
                player_pieces[abs(player_choice) - 1].reverse()
                return player_choice
            else:
                print('Illegal move. Please try again..')
                break
        
def handle_computer_choice(domino_snake_str):
    match = [int(domino_snake_str[1:2]), int(domino_snake_str[-2:-1])]
    # print('match', match)
    # print('computer pieces', computer_pieces)
    for idx, computer_piece in enumerate(computer_pieces):
        # print('try: ', computer_piece)
        if computer_piece[0] == match[1]:
            computer_choice = idx + 1
            return computer_choice
        elif computer_piece[1] == match[0]:
            computer_choice = -idx - 1
            return computer_choice         
        elif computer_piece[0] == match[0]:
            computer_pieces[idx].reverse()
            computer_choice = -idx - 1
            return computer_choice
        elif computer_piece[1] == match[1]:
            computer_pieces[idx].reverse()
            computer_choice = idx + 1
            return computer_choice
                     
    computer_choice = 0
    pick_domino()
    return computer_choice

def pick_domino():
    if len(stock_pieces) > 0:
        piece = stock_pieces.pop(randint(0, len(stock_pieces) - 1))
        if status == 'player':
            player_pieces.append(piece)
        else:
            computer_pieces.append(piece)

def grow_snake(choice):
    global domino_snake
    if status == 'player':
        piece = player_pieces[abs(choice) - 1]
        player_pieces.pop(abs(choice) - 1)
    else:
        piece = computer_pieces[abs(choice) - 1]
        computer_pieces.pop(abs(choice) - 1)
    if int(choice) < 0:
        domino_snake.insert(0, piece)
    else:
        domino_snake.append(piece)

def print_snake(domino_snake):
    domino_snake_str = ''
    for piece in domino_snake:
        domino_snake_str += str(piece)
    if len(domino_snake) <= 6:
        print(f'\n{domino_snake_str}\n')
    else:
        print(f'\n{domino_snake_str[:18]}...{domino_snake_str[-18:]}\n')
    return domino_snake_str

def check_status(domino_snake_str):
    global status
    if len(player_pieces) == 0:
        status = 'win'
    elif len(computer_pieces) == 0:
        status = 'lose'
    elif domino_snake_str[1] == domino_snake_str[-2] and domino_snake_str.count(domino_snake_str[1]) == 8:
        # print('left', domino_snake_str[1])
        # print('right', domino_snake_str[-2])
        # print('count', domino_snake_str.count(domino_snake_str[1])
        status = 'draw'       
  
def main():
    global status
    initial()
    status_dict = {
        'computer':'Computer is about to make a move. Press Enter to continue...',
        'player': "It's your turn to make a move. Enter your command.",
        'win': 'The game is over. You won!',
        'lose': 'The game is over. The computer won!',
        'draw': "The game is over. It's a draw!"
    }

    while True:
        print('='* 70)
        print(f'Stock size: {len(stock_pieces)}')
        print(f'Computer pieces: {len(computer_pieces)}')
        domino_snake_str = print_snake(domino_snake)
        print('Your pieces:')
        for idx, piece in enumerate(player_pieces):
            print(f'{idx + 1}:{piece}')

        check_status(domino_snake_str)   
        print(f'\nStatus: {status_dict[status]}')
        if status == 'player':
            player_choice = handle_player_choice(domino_snake_str)
            if player_choice != 0:
                grow_snake(player_choice)
            status = 'computer'
        elif status == 'computer':
            input()
            computer_choice = handle_computer_choice(domino_snake_str)
            print('pc choice', computer_choice)
            if computer_choice != 0:
                grow_snake(computer_choice)
            status = 'player'
        else:
            break
    
main()