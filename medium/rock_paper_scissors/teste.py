import random
import sys


def check_outcome(move1, move2, game_list):
    half = int(len(game_list) / 2)
    # print(f"Half Value: {half}")
    wins = game_list[half:]
    # print(f"Wins: {wins}")
    losses = game_list[:half]
    # print(f"Losses: {losses}")
    if move1 == move2:
        return 0
    elif move2 in wins:
        return 1
    elif move2 in losses:
        return -1


def get_user_stats(username, file_contents):
    user_score = 0
    for line in file_contents:
        if username in line:
            user_score = int(line.strip().split()[1])
            return user_score
    return user_score


def generate_game_list(user_list, user_choice):
    right_half = choices[user_list.index(user_choice) + 1:]
    left_half = choices[:user_list.index(user_choice)]
    win_lose_order = right_half + left_half
    return win_lose_order


name = input("Enter your name: ")
print(f"Hello, {name}")

rating = open('C:/Users/thiag/Documents/prog/Python/py/jetbrains/medium/rock_paper_scissors/rating.txt', 'r')
lines = rating.readlines()
rating.close()

score = get_user_stats(name, lines)

choices = input()
if choices == '':
    choices = ["rock", "paper", "scissors"]
else:
    choices = choices.split(',')
    print(choices)

print("Okay, let's start")

while True:
    user = input()
    comp = random.choice(choices)

    if user in choices:
        reordered_list = generate_game_list(choices, user)
        result = check_outcome(user, comp, reordered_list)
        if result == 0:
            print(f"There is a draw ({comp})")
            score += 50
        elif result == 1:
            print(f"Well done. The computer chose {comp} and failed")
            score += 100
        elif result == -1:
            print(f"Sorry, but the computer chose {comp}")
        user_stats = f"{name} {score}"
    elif user == "!rating":
        print(f"Your rating: {score}")
    elif user == "!exit":
        print("Bye!")
        sys.exit()
    else:
        print("Invalid input")