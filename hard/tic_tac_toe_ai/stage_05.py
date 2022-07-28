# Tic Tac Toe with AI - Stage 05
# https://hyperskill.org/projects/82/stages/456/implement

'''
Description
Congratulations, you've almost reached the finish line! To complete the task, it's now time to turn the AI into a strong opponent by adding a hard difficulty level.

Unlike medium, when the AI is playing at hard level, it doesn't just look one move ahead to see an immediate win or prevent an immediate loss. At this level, it can look two moves ahead, three moves ahead, and even further. It can calculate all possible moves that might be played during the game, and choose the best one based on the assumption that its opponent will also play perfectly. So, it doesn't rely on the mistakes of its opponent and plays the game without fault from start to finish regardless of the opponent's skill!

The algorithm that implements this is called minimax. It's a brute force algorithm that maximizes the value of the AI's position and minimizes the worth of its opponent's. Minimax is not just for Tic-Tac-Toe. You can use it with any other game where two players make alternate moves, such as chess.

Objectives
In this last stage, you need to implement the hard difficulty level using the minimax algorithm.

You should also add a hard parameter so that it's possible to play against this level.
'''

print("Tic Tac Toe with AI - Stage 05\n")

# https://www.freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37/