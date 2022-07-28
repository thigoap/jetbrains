# Dominoes - Stage 03
# https://hyperskill.org/projects/146/stages/788/implement

'''
Description
It's time to bring the game to life. In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.

In dominoes, you can make a move by taking one of the following actions:

Select a domino and place it on the right side of the snake.
Select a domino and place it on the left side of the snake.
Take an extra piece from the stock (if it's not empty) and skip a turn.
To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: {side_of_the_snake (+/-), domino_number (integer)} or {0}. For example:
-6 : Take the sixth domino and place it on the left side of the snake.
6 : Take the sixth domino and place it on the right side of the snake.
0 : Take an extra piece from the stock (if it's not empty) and skip a turn or simply skip a turn if the stock is already empty by this point.

When it's time for the player to make a move, your program must prompt the user for a number. If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. Once the valid input is received, your program must apply the move.

For now, don't bother about the AI, our goal is just to make the game playable. So, when it's time for the computer to make a move, make it choose a random number between -computer_size and computer_size (where the computer_size is the number of dominoes the computer has).

The end-game condition can be achieved in two ways:

One of the players runs out of pieces. The first player to do so is considered a winner.
The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake below will satisfy this condition:
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]
These two snakes, however, will not:
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]
[6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]
If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.

When the game ends, your program should print the result.

Throughout the gameplay, the snake will grow in length. If it gets too large, the interface might get ugly. To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, ..., for example, [3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4].


Objectives
Modify your Stage 2 code:

At the end of the game, print one of the following phrases:
Status: The game is over. You won!
Status: The game is over. The computer won!
Status: The game is over. It's a draw!

Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.
Add a game loop that will repeat the following steps until the game ends:
Display the current playing field (stage 2).
If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: Invalid input. Please try again..
If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.
Switch turns.
Keep in mind that at this stage we have no rules! Both the player and the computer can place their dominoes however they like.
'''

print('Dominoes - Stage 03\n')

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

def handle_player_choice():
    while True:
        try:
            player_choice = int(input())
            if abs(player_choice) > len(player_pieces):
                print('Invalid input. Please try again.')
            else:
                return player_choice
        except (ValueError, IndexError):
            print('Invalid input. Please try again.')

def handle_computer_choice():
    computer_choice = randint(-len(computer_pieces), len(computer_pieces))
    return computer_choice

def pick_dominoe():
    if len(stock_pieces) > 0:
        piece = stock_pieces.pop(randint(0, len(stock_pieces) - 1))
        if status == 'player':
            player_pieces.append(piece)
        else:
            computer_pieces.append(piece)

def grow_snake(choice):
    global domino_snake
    if status == 'player':
        piece = player_pieces[abs(int(choice)) - 1]
    else:
        piece = computer_pieces[abs(int(choice)) - 1]
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
            player_choice = handle_player_choice()
            if player_choice != 0:
                grow_snake(player_choice)
                piece = player_pieces.pop(abs(player_choice) - 1)
            else:
                pick_dominoe()
            status = 'computer'
        elif status == 'computer':
            input()
            computer_choice = handle_computer_choice()
            if computer_choice != 0:
                grow_snake(computer_choice)
                piece = computer_pieces.pop(abs(computer_choice) - 1)
            else:
                pick_dominoe()
            status = 'player'
        else:
            break
    
main()