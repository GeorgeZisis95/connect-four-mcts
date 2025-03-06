import numpy as np

class ConnectFour:
    
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.current_player = 1
        self.board = np.zeros((self.rows, self.columns))

    def get_legal_actions(self):
        """If the top row is empty it's a valid move"""
        return [action for action in range(self.columns) if self.board[0, action] == 0]

    def get_next_state(self, action):
        assert action in self.get_legal_actions(), "action is not legal"
        row = max(np.where(self.board[:, action] == 0)[0])
        self.board[row, action] = self.current_player
        if not self.get_terminated():
            self.current_player *= -1
    
    def get_winner(self, player):
        for row in range(self.rows):
            for column in range(self.columns - 3):
                if all(self.board[row, column+i] == player for i in range(4)):
                    return True
        for row in range(self.rows - 3):
            for column in range(self.columns):
                if all(self.board[row + i, column] == player for i in range(4)):
                    return True
        for row in range(self.rows - 3):
            for column in range(self.columns - 3):
                if all(self.board[row + i, column + i] == player for i in range(4)):
                    return True
        for row in range(3, self.rows):
            for column in range(self.columns - 3):
                if all(self.board[row - i, column + i] == player for i in range(4)):
                    return True
        return False
    
    def get_draw(self):
        return all(self.board[0, column] != 0 for column in range(self.columns))

    def get_terminated(self):
        return self.get_winner(self.current_player) or self.get_draw()

    def copy(self):
        new_game_object = ConnectFour()
        new_game_object.board = np.array([row.copy() for row in self.board])
        new_game_object.player = self.current_player
        return new_game_object

    def render(self):
        print("======================")
        for row in range(self.rows):
            for column in range(self.columns):
                icon = 'X' if self.board[row, column] == 1 else 'O' if self.board[row, column] == -1 else ' ' 
                print(f"| {icon}", end="")
            print("|")
        print("======================")
        print("|0 |1 |2 |3 |4 |5 |6 |")