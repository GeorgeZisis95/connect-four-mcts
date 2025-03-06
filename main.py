import numpy as np
from mcts import TreeSearch
from connect import ConnectFour

mcts = TreeSearch(time_limit=40)
game = ConnectFour()

while True:
    game.render()
    if game.current_player == 1:
        action = mcts.search(game)
    else:
        action = int(input("Choose your move."))
    game.get_next_state(action) 
    if game.get_terminated():
        print(f"Winner {game.current_player}")
        game.render()
        break