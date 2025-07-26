from env.connect4 import ConnectFour
from env.connect3 import ConnectThree
from model.model import ConvModel
from search.mcts import TreeSearch
from search.alpha import AlphaTreeSearch

game = ConnectFour()
mcts = TreeSearch(game)
model = ConvModel(input_channels=1, kernels=3, total_actions=4)
alpha = AlphaTreeSearch(game, model)

board = game.get_initial_state()
player = 1
while True:
    game.render(board)
    if player == 1:
        action = mcts.search(board, player, num_searches=10000)
    else:
        action = int(input("Choose your move."))
    board = game.get_next_state(board, player, action)
    if game.get_terminated(board, player):
        if game.get_draw(board, player):
            print(f"Game is a draw")
        else:
            print(f"Winner {player}")
        game.render(board)
        break
    player *= -1