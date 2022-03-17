from MonteCarloTreeSearch import MonteCarloTreeSearch
from Frame import Frame

class MC:

    def get_move(frame: Frame):
        
        iterations = 600
        exploratory_factor = 5
        
        MC = MonteCarloTreeSearch(frame, exploratory_factor)
        action = MC.monte_carlo_tree_search(iterations)
        
        return action
         