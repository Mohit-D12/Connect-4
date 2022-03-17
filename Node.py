from math import *
from Frame import Frame

class Node:
    
    def __init__(self, frame: Frame, parent = None, action = -1):

        self.frame = frame
        self.parent = parent
        self.action = action
        
        self.simulations = 0
        self.win_counter = 0
        self.children = {}

        self.ended = frame.is_ended()
        self.winner = frame.get_winner()
        self.player = frame.get_player()
        
        
    def has_children(self):
        return len(self.children) > 0
     
    def get_average_wins(self):

        wins = self.win_counter
        node_simulations = self.simulations

        if node_simulations == 0:
            return 0
        
        return wins / node_simulations   
    
    def get_UCB(self, exploratory_factor):

        wins = self.win_counter
        node_simulations = self.simulations
        
        if self.parent == None:
            return None
        
        total_simulations = self.parent.simulations
        
        if node_simulations == 0:
            return None
        
        trust_value = wins / node_simulations
        exploratory_factor = sqrt((exploratory_factor * log2(total_simulations)) / node_simulations)
        
        ucb = trust_value + exploratory_factor
        
        return ucb

    def get_child_by_action(self, action):
        return self.children.get(action, None)

    def get_children_list(self):
        return list(self.children.values())