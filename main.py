import numpy as np
from mcts import TreeSearch
from connect import ConnectFour

mcts = TreeSearch(num_searches=50000)
game = ConnectFour()

while not game.get_terminated():
    game.render()
    if game.current_player == 1:
        action = mcts.search(game)
    else:
        action = int(input("Choose your move."))
    game.get_next_state(action)