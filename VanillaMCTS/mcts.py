import numpy as np
import math, time

class Node:

    def __init__(self, game, board, player, parent=None):
        self.game = game
        self.board = board
        self.player = player
        self.parent = parent

        self.children = {}
        self.visit_count = 0
        self.total_value = 0
    
    def is_fully_expanded(self):
        return len(self.children) == len(self.game.get_legal_actions(self.board))
    
    def uct_score(self, child, c_puct=2):
        if child.visit_count == 0:
            return float('inf')
        return - child.total_value / child.visit_count + c_puct * math.sqrt(math.log(self.visit_count) / child.visit_count)
    
    def select_child(self):
        best_child = None
        best_score = float('-inf')

        for child in self.children.values():
            score = self.uct_score(child)
            if score > best_score:
                best_score = score
                best_child = child
        return best_child
    
    def expand(self):
        # Choose a child node that hasn't been explored yet
        legal_actions = self.game.get_legal_actions(self.board)
        unexplored_actions = [action for action in legal_actions if action not in self.children]
        action = np.random.choice(unexplored_actions)
        # Move to the next state
        expanded_board = np.copy(self.board)
        expanded_board = self.game.get_next_state(expanded_board, self.player, action)
        # Save this new state-action pair as a new child and return it
        child_node = Node(self.game, expanded_board, self.player * -1, parent=self)
        self.children[action] = child_node
        return child_node
    
    def __repr__(self):
        return f"Board: {self.game.render(self.board)} Visits:{self.visit_count} Value: {self.total_value} Parent: {self.parent}"

class TreeSearch:
    
    def __init__(self, game):
        self.game = game

    def search(self, board, player, num_searches):
        start_time = time.process_time()
        root = Node(self.game, board, player, parent=None)
        for _ in range(num_searches):
            node = self.select(root)
            value = self.rollout(node)
            self.backpropagate(node, value)
        print(root)
        print(f"Process time: {time.process_time() - start_time} seconds")
        return max(root.children.items(), key=lambda item: item[1].visit_count)[0]
    
    def select(self, node):
        while not self.game.get_terminated(node.board, node.player):
            if not node.is_fully_expanded():
                return node.expand()
            # If the node is fully expanded move to the node with the highest uct score
            node = node.select_child()
        return node

    def rollout(self, node):
        if self.game.get_terminated(node.board, node.player):
            return self.game.get_result(node.board)
        rollout_player = node.player
        rollout_board = np.copy(node.board)
        while True:
            action = np.random.choice(self.game.get_legal_actions(rollout_board))
            rollout_board = self.game.get_next_state(rollout_board, rollout_player, action)
            if self.game.get_terminated(rollout_board, rollout_player):
                break
            rollout_player *= -1
        return self.game.get_result(rollout_board)

    def backpropagate(self, node, value):
        while node is not None:
            node.visit_count += 1
            if value == 1 and node.player == 1:
                node.total_value += 1
            elif value == -1 and node.player == 1:
                node.total_value += -1
            elif value == 1 and node.player == -1:
                node.total_value += -1
            elif value == -1 and node.player == -1:
                node.total_value += 1
            node = node.parent