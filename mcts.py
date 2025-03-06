import numpy as np
import math

class Node:

    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent

        self.children = {}
        self.visit_count = 0
        self.node_value = 0
    
    def is_fully_expanded(self):
        return len(self.children) == len(self.game.get_legal_actions())
    
    def uct_score(self, child, c_puct=1.41):
        if child.visit_count == 0:
            return float('inf')
        return child.node_value / child.visit_count + c_puct * math.sqrt(math.log(self.visit_count) / child.visit_count)
    
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
        legal_actions = self.game.get_legal_actions()
        unexplored_actions = [action for action in legal_actions if action not in self.children]
        if not unexplored_actions:
            return None
        action = np.random.choice(unexplored_actions)
        # Create new game object instead of reference to existing game
        expanded_game = self.game.copy()
        expanded_game.get_next_state(action)
        # Create the new child node and append it to children
        child_node = Node(expanded_game, parent=self)
        self.children[action] = child_node
        return child_node

class TreeSearch:
    
    def __init__(self, num_searches=1000):
        self.num_searches = num_searches
    
    def search(self, game):
        root = Node(game)
        for _ in range(self.num_searches):
            node = self.select(root)
            value = self.rollout(node.game)
            self.backpropagate(node, value)
        return max(root.children.items(), key=lambda item: item[1].visit_count)[0]
    
    def select(self, node):
        while not node.game.get_terminated():
            if not node.is_fully_expanded():
                return node.expand()
            node = node.select_child()
        return node

    def rollout(self, game):
        # Create new game object instead of reference to existing game
        rollout_game = game.copy()
        while not rollout_game.get_terminated():
            action = np.random.choice(rollout_game.get_legal_actions())
            rollout_game.get_next_state(action)
        if rollout_game.get_winner(1):
            return 1
        if rollout_game.get_winner(-1):
            return -1
        if rollout_game.get_draw():
            return 0
        print("rollout is over but there is no score?")

    def backpropagate(self, node, value):
        while node is not None:
            node.visit_count += 1
            node.node_value += value
            value = -value
            node = node.parent