from MonteCarloTreeSearch import MonteCarloTreeSearch
from Frame import Frame

class MC:

    def __init__(self, iterations, exploratory_factor) -> None:

        self.iterations = iterations
        self.exploratory_factor = exploratory_factor

    def get_move(self, frame: Frame):
    
        MC = MonteCarloTreeSearch(frame, self.exploratory_factor)
        action = MC.monte_carlo_tree_search(self.iterations)
        
        return action
        

# 600 1.5