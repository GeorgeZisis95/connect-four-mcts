from mcts import TreeSearch
from connect import ConnectFour

game = ConnectFour()
mcts = TreeSearch(game)

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