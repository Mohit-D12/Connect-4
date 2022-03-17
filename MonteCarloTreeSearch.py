from Node import Node
from Frame import Frame
from math import *

class MonteCarloTreeSearch:
    score = { 'draw': 1, 'win': 1, 'lose': 0 } 
    
    def __init__(self, frame, exploratory_factor):
        self.frame : Frame = frame
        self.root : Node = Node(frame)
        self.exploratory_factor = exploratory_factor
        
    def monte_carlo_tree_search(self, iterations):

        #self.debug_frame()
        for iteration in range(iterations):
            if self.root.winner > 0 or self.root.ended:
                return -1
            self.iterate()
            #self.debug(iteration)
        
        action = self.get_best_move()
        return action

    def get_best_move(self):
        if self.root.winner > 0 or self.root.ended:
            return -1
        
        result = -1
        action = -1
        children = self.root.get_children_list()
        
        for child in children:
            current_average_wins = child.get_average_wins()
            if current_average_wins > result:
                result = current_average_wins
                action = child.action
                
        return action
       
    def iterate(self):
        
        if not self.root.has_children():
            self.expand(self.root)
        
        current = self.root
        
        while current.has_children():
            current = self.select(current)
        
        if current.winner > 0:
            if current.winner == self.root.player:
                self.backpropagate(current, MonteCarloTreeSearch.score['win'])
            else:
                self.backpropagate(current, MonteCarloTreeSearch.score['lose'])
            return

        if current.ended:
            self.backpropagate(current, MonteCarloTreeSearch.score['draw'])
            return
        
        if current.simulations:
            self.expand(current)
            current = self.select(current)
        
        winner = self.simulate(current)
        
        if winner == self.root.player:
            simulation_score = MonteCarloTreeSearch.score['win']
        elif winner <= 0:
            simulation_score = MonteCarloTreeSearch.score['draw']
        else:
            simulation_score = MonteCarloTreeSearch.score['lose']
            
        self.backpropagate(current, simulation_score)
    
    def select(self, node):
        children = node.get_children_list()
        ucb_score = {}
        selected_child, max_ucb_score = None, 0
        
        for child in children:
            ucb_score[child.action] = child.get_UCB(self.exploratory_factor)
            if ucb_score[child.action] == None:
                return child
            if ucb_score[child.action] > max_ucb_score:
                max_ucb_score = ucb_score[child.action]
                selected_child = child
        
        return selected_child
        
    def expand(self, node):
        
        base_frame = node.frame
        
        winner = base_frame.get_winner()
        if winner > 0:
            node.winner = winner
            return
            
        valid_moves = base_frame.get_valid_moves()
        if len(valid_moves) == 0:
            node.ended = True
            return
        
        for move in valid_moves:
            child = Node(base_frame.play_move(move), node, move)
            node.add_child(child)
    
    def simulate(self, node):
        #returns winner or 0 if drawn
        frame: Frame = node.frame
        
        while True:
            winner = frame.get_winner()
            if winner > 0:
                return winner
            move = frame.get_random_move()
            if move == -1:
                return 0
            frame = frame.play_move(move)
    
    def backpropagate(self, node: Node, score):
        while True:
            node.simulations += 1
            node.win_counter += score
            
            if node == self.root:
                return
            node = node.parent
  
# debugging 
    def debug(self, iteration):
        file = open("DebugTree.txt", "a")
        file.writelines (["Iteration: "+ str(iteration+1) + "\n"])
        file.close()
        self.root.other_name()
    
    def debug_frame(self):
        file = open("DebugTree.txt", "w")
        s = ""
        for i in self.frame.frame:
            for j in i:
                s += str(j) + " "
            s += "\n"
        file.write(s)
        file.close()
 