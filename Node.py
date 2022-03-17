from math import *
from Frame import Frame

class Node:
    
    def __init__(self, frame: Frame, parent = None, action = -1):
        self.frame = frame
        self.parent = parent
        self.action = action
        self.ended = frame.is_ended()
        self.winner = frame.get_winner()
        self.player = frame.get_player()
        self.simulations = 0
        self.win_counter = 0
        self.children = {}
        
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


# not used
    def set_children(self, children):
        for child in children:
            self.children[child.action] = child
    
    def add_child(self, child):
        self.children[child.action] = child


# debugging
    def print_children(self):
        print()
        print("Inside Print Children")
        for child in self.children:
            self.children[child].print_node()
        print("Exiting Print Children")
        print()

    def print_node(self):
        print()
        print("Printing Node")
        #print("UCB:\t", self.get_UCB(2))
        print("Action:\t", self.action)
        print("Parent:\t",self.parent)
        print("Ended:\t",self.ended)
        print("Winner:\t",self.winner)
        print("Simulations:\t",self.simulations)
        print("Win Counter:\t",self.win_counter)
        print("Children:\t",self.children)
        for action in self.children:
            child: Node = self.children[action]
            print(child.action, child.simulations, child.win_counter)
        print()
    
    def other_name(self, level=0):
        file = open("DebugTree.txt", "a")
        file.writelines (['\t' * level + str(self.action) + " " + str(self.win_counter) + " " + str(self.simulations) + "\n"])
        file.close()
        for child in self.children:
            self.children[child].other_name(level+1)
    