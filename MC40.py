from MonteCarloTreeSearch import MonteCarloTreeSearch
from Frame import Frame

class MC40:

    def get_move(frame: Frame):
        
        iterations = 40
        exploratory_factor = 1.5
        
        MC40 = MonteCarloTreeSearch(frame, exploratory_factor)
        action = MC40.monte_carlo_tree_search(iterations)
        
        return action
        