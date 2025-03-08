import numpy as np
import sys

class ConnectThree:
    
    def __init__(self):
        self.rows = 4
        self.columns = 4

    def get_initial_state(self):
        return np.zeros((self.rows, self.columns))

    def get_legal_actions(self, board):
        """If the top row is empty it's a valid move"""
        return [action for action in range(self.columns) if board[0, action] == 0]

    def get_next_state(self, board, player, action):
        if action not in self.get_legal_actions(board):
            sys.exit("Invalid action chosen: connect.py line 19")
        row = max(np.where(board[:, action] == 0)[0])
        board_to_be_updated = np.copy(board)
        board_to_be_updated[row, action] = player
        return board_to_be_updated
        
    def get_winner(self, board, player):
        for row in range(self.rows):
            for column in range(self.columns - 2):
                if all(board[row, column+i] == player for i in range(3)):
                    return True
        for row in range(self.rows - 2):
            for column in range(self.columns):
                if all(board[row + i, column] == player for i in range(3)):
                    return True
        for row in range(self.rows - 2):
            for column in range(self.columns - 2):
                if all(board[row + i, column + i] == player for i in range(3)):
                    return True
        for row in range(2, self.rows):
            for column in range(self.columns - 2):
                if all(board[row - i, column + i] == player for i in range(3)):
                    return True
        return False
    
    def get_draw(self, board, player):
        return len(self.get_legal_actions(board)) == 0 and not self.get_winner(board, player)

    def get_terminated(self, board, player):
        return self.get_winner(board, player) or self.get_draw(board, player)
    
    def get_result(self, board):
        if self.get_winner(board, 1):
            return 1
        if self.get_winner(board, -1):
            return -1
        else:
            return 0

    def render(self, board):
        print("=============")
        for row in range(self.rows):
            for column in range(self.columns):
                icon = 'X' if board[row, column] == 1 else 'O' if board[row, column] == -1 else ' ' 
                print(f"| {icon}", end="")
            print("|")
        print("=============")
        print("|0 |1 |2 |3 |")

class ConnectFour:
    
    def __init__(self):
        self.rows = 6
        self.columns = 7

    def get_initial_state(self):
        return np.zeros((self.rows, self.columns))

    def get_legal_actions(self, board):
        """If the top row is empty it's a valid move"""
        return [action for action in range(self.columns) if board[0, action] == 0]

    def get_next_state(self, board, player, action):
        if action not in self.get_legal_actions(board):
            sys.exit("Invalid action chosen: connect.py line 19")
        row = max(np.where(board[:, action] == 0)[0])
        board_to_be_updated = np.copy(board)
        board_to_be_updated[row, action] = player
        return board_to_be_updated
        
    def get_winner(self, board, player):
        for row in range(self.rows):
            for column in range(self.columns - 3):
                if all(board[row, column+i] == player for i in range(4)):
                    return True
        for row in range(self.rows - 3):
            for column in range(self.columns):
                if all(board[row + i, column] == player for i in range(4)):
                    return True
        for row in range(self.rows - 3):
            for column in range(self.columns - 3):
                if all(board[row + i, column + i] == player for i in range(4)):
                    return True
        for row in range(3, self.rows):
            for column in range(self.columns - 3):
                if all(board[row - i, column + i] == player for i in range(4)):
                    return True
        return False
    
    def get_draw(self, board, player):
        return len(self.get_legal_actions(board)) == 0 and not self.get_winner(board, player)

    def get_terminated(self, board, player):
        return self.get_winner(board, player) or self.get_draw(board, player)
    
    def get_result(self, board):
        if self.get_winner(board, 1):
            return 1
        if self.get_winner(board, -1):
            return -1
        else:
            return 0

    def render(self, board):
        print("======================")
        for row in range(self.rows):
            for column in range(self.columns):
                icon = 'X' if board[row, column] == 1 else 'O' if board[row, column] == -1 else ' ' 
                print(f"| {icon}", end="")
            print("|")
        print("======================")
        print("|0 |1 |2 |3 |4 |5 |6 |")